from distutils.log import debug
import ply.lex as lex
import ply.yacc as yacc

from lexer import Lexer


class Parser():
    # Creating lexer and importing tokens
    lexer = Lexer()
    tokens = lexer.tokens
    lexer = lex.lex(module=lexer)

    # Defining the precedence
    precedence = (
        ('right', 'IDENT', 'IF'),
        ('right', 'ASSIGN'),
        ('left', 'LOWER', 'LOWER_EQUAL', 'HIGHER', 'HIGHER_EQUAL'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULTIPLY', 'DIVIDE'),
        ('left', 'OPEN_PAREN', 'CLOSE_PAREN')
    )

    # Defining the grammar
    def p_PROGRAM(self, p):
        '''PROGRAM : STATEMENT 
                   | FUNCLIST
                   | EMPTY'''
        p[0] = p[1]

    def p_FUNLIST(self, p):
        '''FUNCLIST : FUNCDEF FUNCLIST 
                    | FUNCDEF'''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    def p_FUNCDEF(self, p):
        '''FUNCDEF : DEF IDENT OPEN_PAREN PARAMLIST CLOSE_PAREN OPEN_CURLY_BRACKET STATELIST CLOSE_CURLY_BRACKET'''
        if p[4] is None:
            p[4] = ""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8]

    def p_INTFLOATSTRING(self, p):
        '''INTFLOATSTRING : INT
                          | FLOAT
                          | STRING'''
        p[0] = p[1]

    def p_PARAMLIST(self, p):
        '''PARAMLIST : INTFLOATSTRING IDENT COMMA PARAMLIST
                     | PARAMLIST1'''
        if len(p) == 5:
            if p[4] is None:
                p[0] = p[1] + p[2] + p[3]
            else:
                p[0] = p[1] + p[2] + p[3] + p[4]
        else:
            p[0] = p[1]

    def p_PARAMLIST1(self, p):
        '''PARAMLIST1 : INTFLOATSTRING IDENT
                      | EMPTY'''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

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
        if len(p) == 4:
            p[0] = p[1] + p[2] + p[3]
        elif len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    def p_VARDECL(self, p):
        '''VARDECL : INTFLOATSTRING IDENT VARDECL1'''
        if p[3] is None:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1] + p[2] + p[3]

    def p_VARDECL1(self, p):
        '''VARDECL1 : OPEN_SQUARE_BRACKET INT_CONSTANT CLOSE_SQUARE_BRACKET VARDECL1
                    | EMPTY'''
        if len(p) == 5:
            if p[4] is None:
                p[0] = p[1] + p[2] + p[3]
            else:
                p[0] = p[1] + p[2] + p[3] + p[4]
        else:
            p[0] = p[1]

    def p_ATRIBSTAT(self, p):
        '''ATRIBSTAT : LVALUE ASSIGN ATRIBSTAT1'''
        p[0] = p[1] + p[2] + p[3]
        
    def p_ATRIBSTAT1(self, p):
        ''' ATRIBSTAT1 : EXPRESSION 
                       | ALLOCEXPRESSION 
                       | FUNCCALL'''
        p[0] = p[1]

    def p_FUNCCALL(self, p):
        '''FUNCCALL : IDENT OPEN_PAREN PARAMLISTCALL CLOSE_PAREN'''
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_PARAMLISTCALL(self, p):
        '''PARAMLISTCALL : PARAMLISTCALL1
                         | EMPTY'''
        p[0] = p[1]

    def p_PARAMLISTCALL1(self, p):
        '''PARAMLISTCALL1 : IDENT COMMA PARAMLISTCALL 
                          | IDENT'''
        if len(p) == 4:
            p[0] = p[1] + p[2] + p[3]
        else:
            p[0] = p[1]

    def p_PRINTSTAT(self, p):
        '''PRINTSTAT : PRINT EXPRESSION'''
        p[0] = p[1] + p[2]

    def p_READSTAT(self, p):
        '''READSTAT : READ LVALUE'''
        p[0] = p[1] + p[2]

    def p_RETURNSTAT(self, p):
        '''RETURNSTAT : RETURN'''
        p[0] = p[1]

    def p_IFSTAT(self, p):
        '''IFSTAT : IF OPEN_PAREN EXPRESSION CLOSE_PAREN STATEMENT IFSTAT1'''
        if p[6] is None:
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        else:
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

    def p_IFSTAT1(self, p):
        '''IFSTAT1 : ELSE STATEMENT
                   | EMPTY'''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    def p_FORSTAT(self, p):
        '''FORSTAT : FOR OPEN_PAREN ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT CLOSE_PAREN STATEMENT'''
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9]

    def p_STATELIST(self, p):
        '''STATELIST : STATEMENT STATELIST1'''
        if p[2] is None:
            p[0] = p[1]
        else:
            p[0] = p[1] + p[2]

    def p_STATELIST1(self, p):
        '''STATELIST1 : STATELIST
                      | EMPTY'''
        p[0] = p[1]

    def p_ALLOCEXPRESSION(self, p):
        '''ALLOCEXPRESSION :  NEW INTFLOATSTRING ALLOCEXPRESSION1'''
        p[0] = p[1] + p[2] + p[3]

    def p_ALLOCEXPRESSION1(self, p):
        '''ALLOCEXPRESSION1 : OPEN_SQUARE_BRACKET NUMEXPRESSION CLOSE_SQUARE_BRACKET ALLOCEXPRESSION1
                            | OPEN_SQUARE_BRACKET NUMEXPRESSION CLOSE_SQUARE_BRACKET'''
        if p[4] is None:
            p[0] = p[1] + p[2] + p[3]
        else:
            p[0] = p[1] + p[2] + p[3] + p[4]

    def p_EXPRESSION(self, p):
        '''EXPRESSION : NUMEXPRESSION EXPRESSION1'''
        if p[2] is None:
            p[0] = p[1]
        else:
            p[0] = p[1] + p[2]

    def p_EXPRESSION1(self, p):
        '''EXPRESSION1 : COMPAREOPERANDS NUMEXPRESSION
                       | EMPTY'''
        p[0] = p[1]
    
    def p_COMPAREOPERANDS(self, p):
        '''COMPAREOPERANDS : LOWER 
                           | HIGHER 
                           | LOWER_EQUAL 
                           | HIGHER_EQUAL 
                           | EQUAL 
                           | NOT_EQUAL'''
        p[0] = p[1]

    def p_NUMEXPRESSION(self, p):
        ''' NUMEXPRESSION : TERM NUMEXPRESSION1'''
        if p[2] is None:
            p[0] = p[1]
        else:
            p[0] = p[1] + p[2]
        
    def p_NUMEXPRESSION1(self, p):
        ''' NUMEXPRESSION1 : NUMEXPRESSION2 TERM NUMEXPRESSION1
                           | EMPTY'''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]
    
    def p_NUMEXPRESSION2(self, p):
        ''' NUMEXPRESSION2 : PLUS 
                           | MINUS'''
        p[0] = p[1]

    def p_TERM(self, p):
        '''TERM : UNARYEXPR TERM1'''
        if p[2] is None:
             p[0] = p[1]
        else:
            p[0] = p[1] + p[2]

    def p_TERM1(self, p):
        '''TERM1 : MATHOPERANDS UNARYEXPR TERM1
                 | EMPTY'''
        if len(p) == 4:
            if p[3] is None:
                p[0] = p[1] + p[2]
            else:
                p[0] = p[1] + p[2] + p[3]
        else:
            p[0] = p[1]

    def p_MATHOPERANDS(self, p):
        '''MATHOPERANDS : MULTIPLY 
                        | DIVIDE 
                        | MODULUS'''
        p[0] = p[1]

    def p_UNARYEXPR(self, p):
        '''UNARYEXPR : UNARYEXPR1 FACTOR'''
        if p[1] is None:
            p[0] = p[2]
        else:
            p[0] = p[1] + p[2]

    def p_UNARYEXPR1(self, p):
        '''UNARYEXPR1 : PLUS 
                      | MINUS
                      | EMPTY'''
        p[0] = p[1]

    def p_FACTOR(self, p):
        '''FACTOR : INT_CONSTANT 
                  | FLOAT_CONSTANT 
                  | STRING_CONSTANT 
                  | NULL  
                  | LVALUE 
                  | OPEN_PAREN NUMEXPRESSION CLOSE_PAREN'''
        if len(p) == 4:
            p[0] = p[1] + p[2] + p[3]
        else:
            p[0] = p[1]

    def p_LVALUE(self, p):
        '''LVALUE : IDENT LVALUE1'''
        if p[2] is None:
            p[0] = p[1]
        else:
            p[0] = p[1] + p[2]

    def p_LVALUE1(self, p):
        '''LVALUE1 : OPEN_SQUARE_BRACKET NUMEXPRESSION CLOSE_SQUARE_BRACKET LVALUE1
                   | EMPTY'''
        if len(p) == 5:
            if p[4] is None:
                p[0] = p[1] + p[2] + p[3]
            else:
                p[0] = p[1] + p[2] + p[3] + p[4]
        else:
            p[0] = p[1]

    def p_EMPTY(self, p):
        '''EMPTY :'''
        p[0] = None

    def p_error(self, p):
        print(f"Syntax error at token {p.type} at line {p.lineno}" )

    def test(self, code_path, **kwargs):
        parser = yacc.yacc(module=self, **kwargs)

        # Reading code file and passing as input to lexer
        f = open(code_path, 'r')
        self.code_example = f.read()
        parser.parse(input=self.code_example, lexer=self.lexer)
        f.close()
    
if __name__ == '__main__':
    parser = Parser()
    parser.test(code_path='./code_example.lcc')
# yacc.yacc(debug=True)
