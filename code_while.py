import ply.lex as lex

# List of token names
tokens = (
    'WHILE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'IDENTIFIER',
    'GREATER',
    'LESS',
    'PLUS',
    'MINUS',
    'STAR',
    'SLASH',
    'NUMBER',
    'EQUALS',
)

# Regular expressions for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_GREATER = r'>'
t_LESS = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_EQUALS = r'='

# Ignore whitespace and tabs
t_ignore = ' \t'

def t_WHILE(t):
    r'while'
    return t

# Error handling for unrecognized characters
def t_error(t):
    print("Illegal character: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Sample input
data = 'while (x > 3) {;}'
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

import ply.yacc as yacc

# Grammar rules for a 'while' construct
def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN condition RPAREN LBRACE statements RBRACE
    '''
    p[0] = 'Valid Java while statement'

def p_condition(p):
    '''
    condition : expression GREATER expression
              | expression LESS expression
              | expression GREATER EQUALS expression
              | expression LESS EQUALS expression
              | expression EQUALS EQUALS expression
              | NUMBER
    '''
    pass

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
    statements :
               | statements
               | while_statement
               | expression SEMICOLON
    '''
    pass

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
    if not s:
        continue
    result = parser.parse(s)
    print(result)
