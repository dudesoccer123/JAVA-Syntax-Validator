import ply.lex as lex

# List of token names
tokens = (
    'INT',
    'CHAR',
    'FLOAT',
    'DOUBLE',
    'LSQPAREN',
    'RSQPAREN',
    'SEMICOLON',
    'IDENTIFIER',
    'NUMBER',
    'EQUALS',
    'NEW'
)

# reg ex
t_LSQPAREN = r'\['
t_RSQPAREN = r'\]'
t_SEMICOLON = r';'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_EQUALS = r'='
t_ignore = ' \t\n'

def t_INT(t):
    r'int'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_NEW(t):
    r'new'
    return t

def t_error(t):
    print("Illegal character: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
data = 'int[] arr = new int[50];'  # this is a sample construct
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

import ply.yacc as yacc

# Grammar rules for an 'if' construct
def p_arr_statement(p):
    '''
    arr_statement : INT LSQPAREN RSQPAREN LSQPAREN RSQPAREN IDENTIFIER EQUALS NEW INT LSQPAREN NUMBER RSQPAREN LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | INT LSQPAREN RSQPAREN IDENTIFIER EQUALS NEW INT LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | CHAR LSQPAREN RSQPAREN IDENTIFIER EQUALS NEW CHAR LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | FLOAT LSQPAREN RSQPAREN IDENTIFIER EQUALS NEW FLOAT LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | DOUBLE LSQPAREN RSQPAREN IDENTIFIER EQUALS NEW DOUBLE LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | INT IDENTIFIER LSQPAREN RSQPAREN EQUALS NEW INT LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | CHAR IDENTIFIER LSQPAREN RSQPAREN EQUALS NEW CHAR LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | FLOAT IDENTIFIER LSQPAREN RSQPAREN EQUALS NEW FLOAT LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | DOUBLE IDENTIFIER LSQPAREN RSQPAREN EQUALS NEW DOUBLE LSQPAREN NUMBER RSQPAREN SEMICOLON
    '''
    p[0] = 'Valid Java ARRAY statement'



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
