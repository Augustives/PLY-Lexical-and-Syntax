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
    """PROGRAM : '(' STATEMENT '|' FUNCLIST ')' '?' """
    pass

def p_FUNLIST(p):
    """FUNCLIST : FUNCDEF FUNCLIST '|' FUNCDEF"""
    pass

def p_FUNCDEF(p):
    """FUNCDEF : def IDENT OPEN_PAREN PARAMLIST CLOSE_PAREN OPEN_CURLY_BRACKET STATELIST CLOSE_CURLY_BRACKET"""
    pass

def p_PARAMLIST(p):
    """PARAMLIST : '(' '(' int '|' float '|' string ')' IDENT COMMA PARAMLIST '|' '(' int '|' float '|' string ')' IDENT ')' '?' """
    pass

def p_STATEMENT(p):
   """STATEMENT : '(' VARDECL SEMICOLON '|' ATRIBSTAT SEMICOLON '|' PRINTSTAT SEMICOLON '|' READSTAT SEMICOLON '|' RETURNSTAT SEMICOLON '|' IFSTAT '|' FORSTAT '|' OPEN_CURLY_BRACKET STATELIST CLOSE_CURLY_BRACKET '|' break SEMICOLON '|' SEMICOLON ')' """
   pass

def p_VARDECL(p):
    """VARDECL : '(' int '|' float '|' string ')' IDENT '(' OPEN_SQUARE_BRACKET INT_CONSTANT CLOSE_SQUARE_BRACKET ')' '∗' """
    pass

def p_ATRIBSTAT(p):
    """ATRIBSTAT : LVALUE ASSIGN '(' EXPRESSION '|' ALLOCEXPRESSION '|' FUNCCALL ')' """
    pass

def p_FUNCCALL(p):
    """FUNCCALL : IDENT OPEN_PAREN PARAMLISTCALL CLOSE_PAREN """
    pass

def p_PARAMLISTCALL(p):
    """PARAMLISTCALL : '(' IDENT COMMA PARAMLISTCALL '|' IDENT ')' '?' """
    pass

def p_PRINTSTAT(p):
    """PRINTSTAT : print EXPRESSION"""
    pass

def p_READSTAT(p):
    """READSTAT : read LVALUE"""
    pass

def p_RETURNSTAT(p):
    """RETURNSTAT : return"""
    pass

def p_IFSTAT(p):
    """IFSTAT : if OPEN_PAREN EXPRESSION CLOSE_PAREN STATEMENT '(' else STATEMENT ')' '?' """
    pass

def p_FORSTAT(p):
    """FORSTAT : for OPEN_PAREN ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT CLOSE_PAREN STATEMENT"""
    pass


def p_STATELIST(p):
    "STATELIST : STATEMENT '(' STATELIST ')' '?'"
    pass

def p_ALLOCEXPRESSION(p):
    """ALLOCEXPRESSION :  new '(' int '|' float '|' string ')' '(' OPEN_SQUARE_BRACKET NUMEXPRESSION CLOSE_SQUARE_BRACKET ')' '+'  """
    pass

def p_EXPRESSION(p):
    """EXPRESSION : NUMEXPRESSION '(' '(' LOWER '|' HIGHER '|' LOWER_EQUAL '|' HIGHER_EQUAL '|' EQUAL '|' NOT_EQUAL ')' NUMEXPRESSION ')' '?' """
    pass

def p_NUMEXPRESSION(p):
    """ NUMEXPRESSION : TERM '(' '(' PLUS '|' MINUS ')' TERM ')' '∗' """
    pass

def p_TERM(p):
    """TERM : UNARYEXPR '(' '('  MULTIPLY '|' DIVIDE '|' MODULUS ')' UNARYEXPR ')' '∗' """
    pass

def p_UNARYEXPR(p):
    """UNARYEXPR : '(' '(' PLUS '|' MINUS ')' ')' '?' FACTOR """
    pass

def p_FACTOR(p):
    """FACTOR :  '(' INT_CONSTANT '|' FLOAT_CONSTANT '|' STRING_CONSTANT '|' null '|' '|' LVALUE '|' OPEN_PAREN NUMEXPRESSION CLOSE_PAREN ')' """
    pass

def p_LVALUE(p):
    """LVALUE : IDENT '(' OPEN_SQUARE_BRACKET NUMEXPRESSION CLOSE_SQUARE_BRACKET ')' '∗'"""
    pass

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")


# Build the parser
try:
    parser = yacc.yacc(debug=True)
except:
    print('Yacc error')
