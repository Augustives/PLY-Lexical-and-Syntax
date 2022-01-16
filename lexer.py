import ply.lex as lex
import ply.yacc as yacc


# Reserved words
reserved_words =  [
    'DEF',
    'BREAK',
    'PRINT',
    'READ',
    'RETURN',
    'IF',
    'ELSE',
    'FOR',
    'NULL',
    'INT',
    'FLOAT',
    'STRING'
]

# Definig the name of the tokens we are going to use
tokens = reserved_words+[
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'OPEN_SQUARE_BRACKET',
    'CLOSE_SQUARE_BRACKET',
    'OPEN_CURLY_BRACKET',
    'CLOSE_CURLY_BRACKET',
    'COMMA',
    'SEMICOLON',
    'EQUAL',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULUS',
    'HIGHER',
    'LOWER',
    'HIGHER_EQUAL',
    'LOWER_EQUAL',
    'DOUBLE_EQUAL',
    'NOT_EQUAL',
    'IDENT',
    'INT_CONSTANT',
    'FLOAT_CONSTANT',
    # 'STRING_CONSTANT',
]

# Definig our grammar based on our tokens with the use of regular expressions
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_OPEN_SQUARE_BRACKET = r'\['
t_CLOSE_SQUARE_BRACKET = r'\]'
t_OPEN_CURLY_BRACKET = r'\{'
t_CLOSE_CURLY_BRACKET = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_MODULUS = r'%'
t_HIGHER = r'>'
t_LOWER = r'<'
t_HIGHER_EQUAL = r'>='
t_LOWER_EQUAL = r'<='
t_DOUBLE_EQUAL = r'=='
t_NOT_EQUAL = r'\!='

def t_FLOAT_CONSTANT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT_CONSTANT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_CONSTANT(t):
    r'''('\b.*\b')|("\b.*\b")'''
    t.type = 'STRING_CONSTANT'
    return t


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in reserved_words:
        t.value = t.value.upper()
        t.type = t.value
    else:
        t.type = 'IDENT'
    return t

# Which characters we are going to ignore
t_ignore = '\t \n'

# Treating errors
def t_error(t):
    print('Illegal character!')
    t.lexer.skip(1)


if __name__ == '__main__':
    # Reading our code to pass it through the lexer and generate the token list
    f = open('code_example.txt', 'r')
    lexer = lex.lex()
    lexer.input(f.read())

    token_list = []
    while True:
        token = lexer.token()
        if not token:
            break
        token_list.append(token.type)

    print(token_list)