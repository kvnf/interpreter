from unittest import TestCase
from typing import List

from klang.ast import (
    LetStatement,
    Program,
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
        
        identifiers: List[LetStatement] = []
        for statement in program.statements:
            # identifiers.append(statement)
            self.assertEqual(statement.token_literal(), 'var')
            self.assertIsInstance(statement, LetStatement)
        
        expected_identifiers: List[str] = ['x', 'y', 'foo']
        
        # self.assertEquals(identifiers, expected_identifiers)
        