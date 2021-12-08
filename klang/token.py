from enum import (
    auto,
    Enum,
    unique,
)
from typing import (
    Dict, 
    NamedTuple,
)

@unique
class TokenType(Enum):
    ASSIGN      =       auto()
    COMMA       =       auto()
    DIV         =       auto()
    ELSE        =       auto()
    EOF         =       auto()
    EQ          =       auto()
    FALSE       =       auto()   
    FUNCTION    =       auto()   
    GT          =       auto()   
    IDENT       =       auto()
    IF          =       auto()
    ILLEGAL     =       auto()
    INT         =       auto()
    LBRACE      =       auto()
    LET         =       auto()
    LPAREN      =       auto()
    LT          =       auto()
    NEG         =       auto()
    NOT_EQ      =       auto()
    PLUS        =       auto()
    PROD        =       auto()
    RBRACE      =       auto()    
    RETURN      =       auto()    
    RPAREN      =       auto()
    SEMICOLON   =       auto()
    SUB         =       auto()
    TRUE        =       auto()
    
class Token(NamedTuple):
    token_type  : TokenType
    literal     : str
    
    def __str__(self) -> str:
        return f'Type:{self.token_type}, Literal:{self.literal}'
    
def get_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'else':TokenType.ELSE,
        'false':TokenType.FALSE,
        'func':TokenType.FUNCTION,
        'if':TokenType.IF,
        'return':TokenType.RETURN,
        'true':TokenType.TRUE,
        'var':TokenType.LET
    }
    return keywords.get(literal, TokenType.IDENT)