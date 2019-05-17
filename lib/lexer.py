from sys import exit
from ply.lex import lex
from os import EX_DATAERR

IGNORECASE = 0b10

literals = [ '+', '-', '*', '/' ]
reserved = {
    "alfred":   "ALFRED",
    "di":       "PRINTLN",
    "en":       "IN",
    "escribe":  "PRINT",
    "guardalo": "STORE",
    "pregunta": "INPUT",

    "mas": "ADD",
    "menos": "SUB",
    "por": "BY",
    "entre": "BTWN"
}
tokens = [
    "ID",
    "STRING",
    "INTEGER"
] + list(reserved.values())

def Lexer():
    t_ignore = ".,y"

    t_ignore_COMMENT = r'\(([^\)])*\)'
    t_ignore_WHITESPACE = r'\s+'

    def t_ID(t):
        r'[a-zA-Z][a-zA-Z0-9_]*'
        t.value = t.value.lower()
        t.type = reserved.get(t.value,"ID")
        return t

    def t_STRING(t):
        r'"([^"\\]|\\.)*"'
        t.value = t.value[1:-1]
        t.value = t.value.replace("\\\"", "\"")
        t.type = reserved.get(t.value,"STRING")
        return t

    def t_INTEGER(t):
        r'[+-]?[0-9]+'
        t.value = int(t.value)
        t.type = reserved.get(t.value,"INTEGER")
        return t

    def t_error(t):
        print("[🐛] Caracter inválido ({},~{}): {}".format(
            lexer.lineno, lexer.lexpos, t.value[0]))
        t.lexer.skip(1)
        exit(EX_DATAERR)


    return lex(
        optimize=0,
        debug=False,
        reflags=IGNORECASE,
        lextab="alfredtab.py"
    )

lexer = Lexer()
