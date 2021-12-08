from klang.lexer import Lexer
from klang.token import (
    TokenType,
    Token,
)

EOF_TOKEN: Token = Token(TokenType.EOF, '')

def start_repl():
    while (source := input('>> ')) != 'exit()':
        lexer: Lexer = Lexer(source)
        
        while (token := lexer.next_token()) != EOF_TOKEN:
            print(token)    