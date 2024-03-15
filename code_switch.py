import ply.lex as lex

# List of token names
tokens = (
    'SWITCH',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COLON',
    'IDENTIFIER',
    'NUMBER',
    'CASE',
    'DEFAULT',
    'BREAK',
    'PLUS',
    'MINUS',
    'STAR',
    'SLASH',
    'EQUALS'
)

# reg ex

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COLON = r':'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_EQUALS = r'='


t_ignore = ' \t\n'

def t_SWITCH(t):
    r'switch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_error(t):
    print("Illegal character: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
data = '''switch (x) {
        case 1:
            ;
        case 2:
            ;
    }''' # this is a sample construct

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok: 
        break    
    print(tok)

import ply.yacc as yacc

# Grammar rules for an 'if' construct
def p_switch_statement(p):
    '''
    switch_statement : SWITCH LPAREN IDENTIFIER RPAREN LBRACE cases RBRACE
    '''
    p[0] = 'Valid Java switch statement'

def p_cases(p):
    '''
    cases : CASE NUMBER COLON statements BREAK SEMICOLON
          | DEFAULT COLON statements BREAK SEMICOLON
          | cases cases
    '''

def p_expression(p):
    '''
    expression : IDENTIFIER
               | expression PLUS expression
               | NUMBER
               | expression MINUS expression
               | expression STAR expression
               | expression SLASH expression
               | expression EQUALS expression
    '''
    pass

def p_statements(p):
    '''
    statements : switch_statement
               | SEMICOLON
               | expression SEMICOLON
    '''


# Error handling
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('construct > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)