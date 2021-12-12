from unittest import TestCase
from typing import (
    cast,
    List
)

from klang.ast import (
    Statement,
    LetStatement,
    Program,
    ReturnStatement,
)
from klang.lexer import Lexer
from klang.parser import Parser

class ParserTest(TestCase):
    
    def test_parse_program(self) -> None:
        source: str = 'variable x = 5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        
        program: Program = parser.parse_program()
        
        self.assertIsNotNone(program)
        self.assertIsInstance(program, Program)
        
    def test_let_statement(self) -> None:
        source: str = '''
            var x = 5;
            var y = 10;
            var foo = 20;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        program: Program = parser.parse_program()
        
        self.assertEqual(len(program.statements), 3)
        
        identifiers: List[str] = []
        for statement in program.statements:
            self.assertEqual(statement.token_literal(), 'var')
            self.assertIsInstance(statement, LetStatement)
            let_statement = cast(LetStatement, statement)
            identifiers.append(str(let_statement.name))
        
        expected_identifiers: List[str] = ['x', 'y', 'foo']
        
        self.assertEquals(identifiers, expected_identifiers)
        
    def test_names_in_let_statement(self) -> None:
        source: str = '''
            var x = 5;
            var y = 10;
            var foo = 20;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        program: Program = parser.parse_program()
        
        self.assertEqual(len(program.statements), 3)
        
        identifiers: List[str] = []
        for statement in program.statements:
            statement = cast(LetStatement, statement)
            assert statement.name is not None
            identifiers.append(statement.name.value)
        expected_identifiers: List[str] = ['x', 'y', 'foo']
        
        self.assertEquals(identifiers, expected_identifiers)
        
    def test_parse_errors(self) -> None:
        source:str = 'var x 5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        program: Program = parser.parse_program()
        
        self.assertEquals(len(parser.errors),  1)
    
    def test_return_statement(self) -> None:
        source: str = '''
            return 5;
            return foo;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        program: Program = parser.parse_program()
        
        self.assertEquals(len(program.statements), 2) # sanity check
        for statement in program.statements:
            self.assertEquals(statement.token_literal(), 'return')
            self.assertIsInstance(statement, ReturnStatement)
        
        
        
        
        
        
        
        
        
        
        
        