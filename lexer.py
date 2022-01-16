import ply.lex as lex
import ply.yacc as yacc
from helpers.column_finder import find_column


class Lexer:
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

    def t_FLOAT_CONSTANT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INT_CONSTANT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_STRING_CONSTANT(self, t):
        r'''('\b.*\b')|("\b.*\b")'''
        t.type = 'STRING_CONSTANT'
        return t

    def t_IDENT(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        if t.value.upper() in self.reserved_words:
            t.value = t.value.upper()
            t.type = t.value
        else:
            t.type = 'IDENT'
        return t

    # Which characters we are going to ignore
    t_ignore = '\t '

    # Treating number of lines
    def t_newline(self, t):
            r'\n+'
            t.lexer.lineno += len(t.value)

    # Treating errors
    def t_error(self, t):
        # TODO: Add column of the error
        column = find_column(self.code_example, t.lineno, t.value[0])
        print(f'Illegal character: "{t.value[0]}"\nLine: {t.lineno}\nColumn: {column}')
        t.lexer.skip(1)

    # Reading our code to pass it through the lexer and generate the token list
    def test(self, **kwargs):
        lexer = lex.lex(module=self, **kwargs)
        f = open('code_example.txt', 'r')
        self.code_example = f.read()
        lexer.input(self.code_example)
        token_list = []
        while True:
            token = lexer.token()
            if not token:
                break
            token_list.append(token.type)

        print(token_list)

if __name__ == '__main__':
    lexer = Lexer()
    lexer.test()