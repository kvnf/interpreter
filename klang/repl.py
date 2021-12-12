from klang.ast import (
    Program
)
from klang.lexer import Lexer
from klang.parser import Parser
from klang.token import (
    TokenType,
    Token,
)

EOF_TOKEN: Token = Token(TokenType.EOF, '')

def start_repl():
    while (source := input('>> ')) != 'exit()':
        lexer: Lexer = Lexer(source)
        parser: Parser =  Parser(lexer)
        program: Program = parser.parse_program()
        
        for statement in program.statements:
            print(statement.name)
        print(program)
        print(len(parser.errors))
        while (token := lexer.next_token()) != EOF_TOKEN:
            print(token)    