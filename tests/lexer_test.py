from unittest import TestCase
from typing import List
from unittest.case import expectedFailure 
from klang.token import (
    Token,
    TokenType,
)
from klang.lexer import Lexer


class LexerTest(TestCase):
    def test_illegal(self) -> None:
        source: str = '¿¡@'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())
            
        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '@'),
        ]        
        
        self.assertEquals(tokens, expected_tokens)
    
    def test_one_character_operator(self) -> None:
        source: str = '=+-*/<>!'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        
        for i in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.SUB, '-'),
            Token(TokenType.PROD, '*'),
            Token(TokenType.DIV, '/'),
            Token(TokenType.LT, '<'),
            Token(TokenType.GT, '>'),
            Token(TokenType.NEG, '!'),
            
        ]
        
        self.assertEquals(tokens, expected_tokens)
        
    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(len(source) + 1 ):
            tokens.append(lexer.next_token())
            
        
        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, ''),
        ]            
        
        self.assertEquals(tokens, expected_tokens)
        
    def test_delimiters(self):
        source: str = '(){},;'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),            
        ]
        
        self.assertEquals(tokens, expected_tokens)
    
    def test_assignment(self):
        source: str = 'var cinco = 5;'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(5):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'var'),
            Token(TokenType.IDENT, 'cinco'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';'),
        ]
        self.assertEquals(tokens, expected_tokens)
        
    def test_function_declaration(self) -> None:
        source: str = '''
        var adder = func(x, y){
            x+y;
        }; 
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(16):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET ,'var' ),
            Token(TokenType.IDENT , 'adder'),
            Token(TokenType.ASSIGN , '=' ),
            Token(TokenType.FUNCTION , 'func' ),
            Token(TokenType.LPAREN , '('),
            Token(TokenType.IDENT , 'x' ),
            Token(TokenType.COMMA , ',' ),
            Token(TokenType.IDENT , 'y'),
            Token(TokenType.RPAREN , ')'),
            Token(TokenType.LBRACE , '{' ),
            Token(TokenType.IDENT , 'x' ),
            Token(TokenType.PLUS , '+' ),
            Token(TokenType.IDENT , 'y'),
            Token(TokenType.SEMICOLON , ';' ),
            Token(TokenType.RBRACE , '}' ),
            Token(TokenType.SEMICOLON , ';' ),
        ] 
        
        self.assertEquals(tokens, expected_tokens)
    
    def test_function_call(self) -> None:
        source: str = 'var result = adder(dos, tres);'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(10):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'var'),
            Token(TokenType.IDENT, 'result'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.IDENT, 'adder'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'dos'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'tres'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.SEMICOLON, ';'),
        ]
        
        self.assertEquals(tokens, expected_tokens)
        
    def test_control_statement(self) -> None:
        source: str = '''
        if (5 < 10) {
            return true;   
        } else {
            return false;
        }
        '''
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(17):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] =[
            Token(TokenType.IF, 'if'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.INT, '5'),
            Token(TokenType.LT, '<'),
            Token(TokenType.INT, '10'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.TRUE, 'true'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.ELSE, 'else'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.FALSE, 'false'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
        ]
        
        self.assertEquals(tokens, expected_tokens)
    
    def test_two_character_operator(self) -> None:
        source:str = '''
        1 == 1;
        1 != 2;
        '''        
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(8):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.INT, '1'),
            Token(TokenType.EQ, '=='),
            Token(TokenType.INT, '1'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.INT, '1'),
            Token(TokenType.NOT_EQ, '!='),
            Token(TokenType.INT, '2'),
            Token(TokenType.SEMICOLON, ';')
        ]
        
        self.assertEquals(tokens, expected_tokens)
        