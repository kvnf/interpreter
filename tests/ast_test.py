from unittest import TestCase

from klang.ast import (
    Expression,
    Identifier,
    LetStatement,
    Program,
    ReturnStatement
)
from klang.token import (
    Token,
    TokenTypels
    
)

class ASTTest(TestCase):
    
    def test_let_statement(self) -> None:
        # 'var my_var = other_var;'
        program: Program = Program(statements = [
            LetStatement(
                token=Token(TokenType.LET, literal='var'),
                name=Identifier(
                    token=Token(TokenType.IDENT, literal='my_var'),
                    value='my_var'
                ),
                value=Identifier(
                    token=Token(TokenType.IDENT, literal='other_var'),
                    value='other_var'
                )
            )
        ])
        
        program_str = str(program)
        
        self.assertEqual(program_str, 'var my_var = other_var;')
    
    def test_return_statement(self) -> None:

        program: Program = Program(statements = [
            ReturnStatement(
                token=Token(TokenType.RETURN, literal='return'),
                return_value=Identifier(
                    token=Token(TokenType.INT, literal='0'),
                    value='0'   
                )
            )
        ])
        program_str = str(program)
        self.assertEqual(program_str, 'return 0;')