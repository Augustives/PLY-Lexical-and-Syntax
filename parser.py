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
    FUNCDEF: DEF IDENT ( PARAMLIST ) { STATELIST }
    """

def p_STATEMENT(p):
    """
    STATEMENT: (( int | float | string ) IDENT,
                PARAMLIST | ( int | float | string ) IDENT)?
    """


def p_VARDECL(p):
    """
    VARDECL: ( int | float | string ) ident ([INT_CONSTANT])∗
    """

def p_ATRIBSTAT(p):
    """
    ATRIBSTAT: LVALUE = ( EXP RESSION | ALLOCEXP RESSION | FUNCCALL)
    """

def p_FUNCCALL(p):
    """
    FUNCCALL: IDENT(PARAMLIST CALL)
    """

def p_PARAMLISTCALL(p):
    """
    PARAMLISTCALL: (IDENT, PARAMLISTCALL | IDENT)?
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
    IFSTAT: if( EXPRESSION ) ST AT EMENT (else STATEMENT)?
    """

def p_FORSTAT(p):
    """
    FORSTAT: for(ATRIBSTAT; EXPRESSION; ATRIBSTAT) STATEMENT
    """

def p_STATELIST(p):
    """
    STATELIST: STATEMENT (STATELIST)?

    """

def p_ALLOCEXPRESSION(p):
    """
    ALLOCEXPRESSION:  new (int | float | string) ([ NUMEXPRESSION ])+
    """

def p_EXPRESSION(p):
    """
    p_EXPRESSION: NUMEXPRESSION(( < | > | <= | >= | == | ! =) NUMEXPRESSION)?
    """

def p_NUMEXPRESSION(p):
    """
    NUMEXPRESSION:TERM ((+ |−) TERM)∗
    """

def p_TERM(p):
    """
    TERM: UNARYEXPR(( ∗ | / | %) UNARYEXPR)∗
    """

def p_UNARYEXPR(p):
    """
    UNARYEXPR: ((+ |−))? FACTOR
    """

def p_FACTOR(p):
    """
    FACTOR:  (int constant | float constant | string constant | null | | LV ALUE | (NUMEXPRESSION))
    """

def p_LVALUE(p):
    """
    p_LVALUE:
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
