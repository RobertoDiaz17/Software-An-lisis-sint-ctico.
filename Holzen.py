# lexer.py
import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IF',       # Opcional
    'ELSE',     # Opcional
    'WHILE'     # Opcional
)

# Expresiones regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Expresiones regulares con acciones
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = float(t.value)
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

# Regla para ignorar espacios en blanco y tabulaciones
t_ignore  = ' \t'

# Regla para manejar errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

if __name__ == '__main__':
    data = "3 + 4 * (10 - 2.5) if x"
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)