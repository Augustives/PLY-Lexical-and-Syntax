from lexer import Lexer

import ply.yacc as yacc
from utils.column_finder import find_column

# Precisa importar os tokens do Lexer
lexer = Lexer()
tokens = lexer.tokens


# Aqui tem que ser definido a ordem dos operadores
# precedence = (
#     ('nonassoc', 'LESSTHAN', 'GREATERTHAN'),  # Nonassociative operators
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'TIMES', 'DIVIDE'),
#     ('right', 'UMINUS'),  # Unary minus operator
# )

# Funções que definem a predecencia
def p_PROGRAM(p):
    """
    PROGRAM: (STATEMENT | FUNCLIST)?
    """

def p_FUNLIST(p):
    """
    FUNCLIST: FUNCDEF FUNCLIST | FUNCDEF
    """

def p_FUNCDEF(p):
    """
    FUNCDEF: DEF IDENT OPEN_PAREN PARAMLIST CLOSE_PAREN OPEN_CURLY_BRACKET STATELIST CLOSE_CURLY_BRACKET
    """

def p_PARAMLIST(p):
    """
    PARAMLIST: (( int | float | string ) IDENT COMMA PARAMLIST | ( int | float | string ) IDENT)?
    """

def p_STATEMENT(p):
    """
    STATEMENT:
            (VARDECL SEMICOLON |
            ATRIBSTAT SEMICOLON |
            PRINTSTAT SEMICOLON |
            READSTAT SEMICOLON |
            RETURNSTAT SEMICOLON |
            IFSTAT |
            FORSTAT |
            OPEN_CURLY_BRACKET STATELIST CLOSE_CURLY_BRACKET |
            BREAK SEMICOLON | SEMICOLON)
    """


def p_VARDECL(p):
    """
    VARDECL: ( int | float | string ) IDENT (OPEN_SQUARE_BRACKET INT_CONSTANT CLOSE_SQUARE_BRACKET)∗
    """

def p_ATRIBSTAT(p):
    """
    ATRIBSTAT: LVALUE ASSIGN ( EXPRESSION | ALLOCEXPRESSION | FUNCCALL)
    """

def p_FUNCCALL(p):
    """
    FUNCCALL: IDENT OPEN_PAREN PARAMLISTCALL CLOSE_PAREN)
    """

def p_PARAMLISTCALL(p):
    """
    PARAMLISTCALL: (IDENT COMMA PARAMLISTCALL | IDENT)?
    """

def p_PRINTSTAT(p):
    """
    PRINTSTAT: print EXPRESSION
    """

def p_READSTAT(p):
    """
    READSTAT: read LVALUE
    """

def p_RETURNSTAT(p):
    """
    RETURNSTAT: return
    """

def p_IFSTAT(p):
    """
    IFSTAT: if OPEN_PAREN EXPRESSION CLOSE_PAREN STATEMENT (ELSE STATEMENT)?
    """

def p_FORSTAT(p):
    """
    FORSTAT: FOR OPEN_PAREN ATRIBSTAT; EXPRESSION; ATRIBSTAT CLOSE_PAREN STATEMENT
    """

def p_STATELIST(p):
    """
    STATELIST: STATEMENT (STATELIST)?
    """

def p_ALLOCEXPRESSION(p):
    """
    ALLOCEXPRESSION:  new (int | float | string) (OPEN_SQUARE_BRACKET NUMEXPRESSION CLOSE_SQUARE_BRACKET)+
    """

def p_EXPRESSION(p):
    """
    p_EXPRESSION: NUMEXPRESSION(( LOWER | HIGHER | LOWER_EQUAL | HIGHER_EQUAL | EQUAL | NOT_EQUAL) NUMEXPRESSION)?
    """

def p_NUMEXPRESSION(p):
    """
    NUMEXPRESSION:TERM ((PLUS | MINUS) TERM)∗
    """

def p_TERM(p):
    """
    TERM: UNARYEXPR(( MULTIPLY | DIVIDE | MODULUS) UNARYEXPR)∗
    """

def p_UNARYEXPR(p):
    """
    UNARYEXPR: ((PLUS | MINUS))? FACTOR
    """

def p_FACTOR(p):
    """
    FACTOR:  (INT_CONSTANT | FLOAT_CONSTANT | STRING_CONSTANT | NULL | | LVALUE | OPEN_PAREN NUMEXPRESSION CLOSE_PAREN )
    """

def p_LVALUE(p):
    """
    p_LVALUE: IDENT( OPEN_SQUARE_BRACKET NUMEXPRESSION CLOSE_SQUARE_BRACKET )∗
    """

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc()
