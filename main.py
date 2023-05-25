# alunos: ISA STOHLER BERTOLACCINI e JEFFERSON SOBRINHO ABBIN
#
from antlr4 import *

from PythonCodeLexer import PythonCodeLexer
from PythonCodeParser import PythonCodeParser

arquivo = open('codigo1.txt', 'r')
               
codigo = arquivo.read()

# Criar um input stream com a expressão a ser analisada
input_stream = InputStream(codigo)

# Criar um lexer com o input stream
lexer = PythonCodeLexer(input_stream)

# Criar um token stream com o lexer
token_stream = CommonTokenStream(lexer)

# Criar um parser com o token stream
parser = PythonCodeParser(token_stream)

# Chamar a regra sintática inicial
tree = parser.program()

# Realizar alguma ação com a árvore sintática resultante
print(tree.toStringTree(recog=parser))