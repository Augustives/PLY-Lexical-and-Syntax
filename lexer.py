import argparse

import ply.lex as lex
import ply.yacc as yacc

from utils.column_finder import find_column


class Lexer:
    def __init__(self):
        self.code_example = None
        # Symbol table
        self.symbol_table = {}

    # Reserved words
    reserved_words = [
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
        'STRING',
        'NEW'
    ]

    # Definig the name of the tokens we are going to use
    tokens = reserved_words + [
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
        'ASSIGN',
        'NOT_EQUAL',
        'IDENT',
        'INT_CONSTANT',
        'FLOAT_CONSTANT',
        'STRING_CONSTANT'
    ]

    # Definig our regular expressions based on our tokens
    t_OPEN_PAREN = r'\('
    t_CLOSE_PAREN = r'\)'
    t_OPEN_SQUARE_BRACKET = r'\['
    t_CLOSE_SQUARE_BRACKET = r'\]'
    t_OPEN_CURLY_BRACKET = r'\{'
    t_CLOSE_CURLY_BRACKET = r'\}'
    t_COMMA = r','
    t_SEMICOLON = r';'
    t_ASSIGN = r'\='
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_MULTIPLY = r'\*'
    t_DIVIDE = r'\/'
    t_MODULUS = r'%'
    t_HIGHER = r'>'
    t_LOWER = r'<'
    t_HIGHER_EQUAL = r'>='
    t_LOWER_EQUAL = r'<='
    t_EQUAL = r'=='
    t_NOT_EQUAL = r'\!='

    def t_FLOAT_CONSTANT(self, t):
        r'\d+\.\d+'
        t.value = str(t.value)
        return t

    def t_INT_CONSTANT(self, t):
        r'\d+'
        t.value = str(t.value)
        return t

    def t_STRING_CONSTANT(self, t):
        r'"([\w\d]|[^"])*"'
        t.type = 'STRING_CONSTANT'
        return t

    # Here we check for the Reserved Words and also the IDENT
    def t_IDENT(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        if (t.value.upper() in self.reserved_words and t.value == t.value.lower()):
            t.value = t.value.upper()
            t.type = t.value
        else:
            t.type = 'IDENT'
            # Adding IDENT to symbol table
            if t.value not in self.symbol_table:
                self.symbol_table[t.value] = {'Lines': []}
            self.symbol_table[t.value]['Lines'].append(t.lineno)
        return t

    # Which characters we are going to ignore
    t_ignore = '\t '

    # Treating number of lines
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += 1

    # Treating errors
    def t_error(self, t):
        column = find_column(self.code_example, t.lineno, t.value[0])
        print(f'Illegal character: "{t.value[0]}"\nLine: {t.lineno}\nColumn: {column}')
        # t.lexer.skip(1)
        raise Exception

    # Opening and reading our code to pass it through the lexer and generate the token list
    def test(self, code_path, **kwargs):
        lexer = lex.lex(module=self, **kwargs)

        # Reading code file and passing as input to lexer
        f = open(code_path, 'r')
        self.code_example = f.read()
        lexer.input(self.code_example)
        f.close()

        # Tokenizing the code
        token_list = []
        result = True
        while result:
            try:
                token = lexer.token()
            except Exception:
                result = False
                break
            if not token:
                break
            token_list.append(token.type)

        if result:
            print(
                f'Token List: {token_list}\n\n',
                f'Symbol Table: {self.symbol_table}'
            )


if __name__ == '__main__':
    # arg_parser = argparse.ArgumentParser(description='Running Lexer')
    # arg_parser.add_argument("--code_path", help="This is the path for the lcc archive")
    # args = arg_parser.parse_args()

    lexer = Lexer()
    lexer.test(code_path='./code_example.lcc')
    # lexer.test(code_path=args.code_path)
