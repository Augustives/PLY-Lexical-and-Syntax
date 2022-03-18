from distutils.log import debug
import ply.lex as lex
import ply.yacc as yacc

from lexer import Lexer


class Parser():
    def __init__(self):
        self.error = False

    # Creating lexer and importing tokens
    lexer = Lexer()
    tokens = lexer.tokens
    lexer = lex.lex(module=lexer)

    # Defining the precedence
    precedence = (
        ('left', 'LOWER', 'LOWER_EQUAL', 'HIGHER', 'HIGHER_EQUAL'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULTIPLY', 'DIVIDE'),
        ('left', 'OPEN_PAREN', 'CLOSE_PAREN')
    )

    # Defining the grammar LCC-2021-2
    def p_PROGRAM(self, p):
        '''PROGRAM : STATEMENT 
                   | FUNCLIST
                   | EMPTY'''
        pass

    def p_FUNCLIST(self, p):
        '''FUNCLIST : FUNCDEF FUNCLIST1'''
        pass

    def p_FUNCLIST1(self, p):
        '''FUNCLIST1 : FUNCLIST 
                     | EMPTY'''
        pass

    def p_FUNCDEF(self, p):
        '''FUNCDEF : DEF IDENT OPEN_PAREN PARAMLIST CLOSE_PAREN OPEN_CURLY_BRACKET STATELIST CLOSE_CURLY_BRACKET'''
        pass

    def p_INT_FLOAT_STRING(self, p):
        '''INT_FLOAT_STRING : INT
                            | FLOAT
                            | STRING'''
        pass

    def p_PARAMLIST(self, p):
        '''PARAMLIST : PARAMLIST1
                     | EMPTY'''
        pass

    def p_PARAMLIST1(self, p):
        '''PARAMLIST1 : INT_FLOAT_STRING IDENT PARAMLIST2'''
        pass

    def p_PARAMLIST2(self, p):
        '''PARAMLIST2 : COMMA PARAMLIST
                      | EMPTY'''
        pass

    def p_STATEMENT(self, p):
        '''STATEMENT : VARDECL SEMICOLON 
                     | ATRIBSTAT SEMICOLON 
                     | PRINTSTAT SEMICOLON 
                     | READSTAT SEMICOLON 
                     | RETURNSTAT SEMICOLON 
                     | IFSTAT FORSTAT 
                     | OPEN_CURLY_BRACKET STATELIST CLOSE_CURLY_BRACKET 
                     | BREAK SEMICOLON 
                     | SEMICOLON'''
        pass

    def p_VARDECL(self, p):
        '''VARDECL : INT_FLOAT_STRING IDENT VARDECL1'''
        pass

    def p_VARDECL1(self, p):
        '''VARDECL1 : OPEN_SQUARE_BRACKET INT_CONSTANT CLOSE_SQUARE_BRACKET VARDECL1
                    | EMPTY'''
        pass

    def p_ATRIBSTAT(self, p):
        '''ATRIBSTAT : LVALUE ASSIGN ATRIBSTAT1'''
        pass
        
    def p_ATRIBSTAT1(self, p):
        ''' ATRIBSTAT1 : EXPRESSION_FUNCCALL 
                       | ALLOCEXPRESSION'''
        pass

    def p_EXPRESSION_FUNCCALL(self, p):
        '''EXPRESSION_FUNCCALL : PLUS FACTOR TERM1 NUMEXPRESSION1 EXPRESSION1
                               | MINUS FACTOR TERM1 NUMEXPRESSION1 EXPRESSION1
                               | INT_CONSTANT TERM1 NUMEXPRESSION1 EXPRESSION1
                               | FLOAT_CONSTANT TERM1 NUMEXPRESSION1 EXPRESSION1
                               | STRING_CONSTANT TERM1 NUMEXPRESSION1 EXPRESSION1
                               | NULL TERM1 NUMEXPRESSION1 EXPRESSION1
                               | OPEN_PAREN NUMEXPRESSION CLOSE_PAREN TERM1 NUMEXPRESSION1 EXPRESSION1
                               | FUNCCALL'''
        pass

    def p_FUNCCALL(self, p):
        '''FUNCCALL : IDENT FUNCCALL1'''
        pass

    def p_FUNCCALL1(self, p):
        '''FUNCCALL1 : ALLOCEXPRESSION1 TERM1 NUMEXPRESSION1 EXPRESSION1
                     | OPEN_PAREN PARAMLISTCALL CLOSE_PAREN'''
        pass

    def p_PARAMLISTCALL(self, p):
        '''PARAMLISTCALL : IDENT PARAMLISTCALL1
                         | EMPTY'''
        pass

    def p_PARAMLISTCALL1(self, p):
        '''PARAMLISTCALL1 : COMMA PARAMLISTCALL 
                          | EMPTY'''
        pass

    def p_PRINTSTAT(self, p):
        '''PRINTSTAT : PRINT EXPRESSION'''
        pass

    def p_READSTAT(self, p):
        '''READSTAT : READ LVALUE'''
        pass

    def p_RETURNSTAT(self, p):
        '''RETURNSTAT : RETURN'''
        pass

    def p_IFSTAT(self, p):
        '''IFSTAT : IF OPEN_PAREN EXPRESSION CLOSE_PAREN STATEMENT IFSTAT1'''
        pass

    def p_IFSTAT1(self, p):
        '''IFSTAT1 : ELSE STATEMENT
                   | EMPTY'''
        pass

    def p_FORSTAT(self, p):
        '''FORSTAT : FOR OPEN_PAREN ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT CLOSE_PAREN STATEMENT'''
        pass

    def p_STATELIST(self, p):
        '''STATELIST : STATEMENT STATELIST1'''
        pass

    def p_STATELIST1(self, p):
        '''STATELIST1 : STATELIST
                      | EMPTY'''
        pass

    def p_ALLOCEXPRESSION(self, p):
        '''ALLOCEXPRESSION :  NEW INT_FLOAT_STRING OPEN_SQUARE_BRACKET NUMEXPRESSION CLOSE_SQUARE_BRACKET ALLOCEXPRESSION1'''
        pass

    def p_ALLOCEXPRESSION1(self, p):
        '''ALLOCEXPRESSION1 : OPEN_SQUARE_BRACKET NUMEXPRESSION CLOSE_SQUARE_BRACKET ALLOCEXPRESSION1
                            | EMPTY'''
        pass

    def p_EXPRESSION(self, p):
        '''EXPRESSION : NUMEXPRESSION EXPRESSION1'''
        pass

    def p_EXPRESSION1(self, p):
        '''EXPRESSION1 : COMPAREOPERANDS NUMEXPRESSION
                       | EMPTY'''
        pass
    
    def p_COMPAREOPERANDS(self, p):
        '''COMPAREOPERANDS : LOWER 
                           | HIGHER 
                           | LOWER_EQUAL 
                           | HIGHER_EQUAL 
                           | EQUAL 
                           | NOT_EQUAL'''
        pass

    def p_NUMEXPRESSION(self, p):
        '''NUMEXPRESSION : TERM NUMEXPRESSION1'''
        pass
        
    def p_NUMEXPRESSION1(self, p):
        '''NUMEXPRESSION1 : NUMEXPRESSION2 TERM NUMEXPRESSION1
                          | EMPTY'''
        pass
    
    def p_NUMEXPRESSION2(self, p):
        '''NUMEXPRESSION2 : PLUS 
                          | MINUS'''
        pass

    def p_TERM(self, p):
        '''TERM : UNARYEXPR TERM1'''
        pass

    def p_TERM1(self, p):
        '''TERM1 : MULT_DIV_MOD TERM
                 | EMPTY'''
        pass

    def p_MULT_DIV_MOD(self, p):
        '''MULT_DIV_MOD : MULTIPLY 
                        | DIVIDE 
                        | MODULUS'''
        pass

    def p_UNARYEXPR(self, p):
        '''UNARYEXPR : NUMEXPRESSION2 FACTOR
                     | FACTOR'''
        pass

    def p_FACTOR(self, p):
        '''FACTOR : INT_CONSTANT 
                  | FLOAT_CONSTANT 
                  | STRING_CONSTANT 
                  | NULL  
                  | LVALUE 
                  | OPEN_PAREN NUMEXPRESSION CLOSE_PAREN'''
        pass

    def p_LVALUE(self, p):
        '''LVALUE : IDENT ALLOCEXPRESSION1'''
        pass

    def p_EMPTY(self, p):
        '''EMPTY :'''
        pass

    def p_error(self, p):
        self.error = True
        self.parser.errok()
        print(
            f'Entry Token: {p.type}\n'
            # f'Left Non Terminal: {}\n'
            # f'Sentencial Form: {}\n'
            '--------------------------------------------------------------------------------'
        )

    def test(self, code_path, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

        # Reading code file and passing as input to lexer
        f = open(code_path, 'r')
        self.code_example = f.read()
        self.parser.parse(input=self.code_example, lexer=self.lexer)
        f.close()

        if not self.error:
            print("Code is correct, no parsing errors")
    
if __name__ == '__main__':
    # arg_parser = argparse.ArgumentParser(description='Running Lexer')
    # arg_parser.add_argument("--code_path", help="This is the path for the lcc archive")
    # args = arg_parser.parse_args()

    parser = Parser()
    parser.test(code_path='./code_example.lcc')
    # parser.test(code_path=args.code_path)
