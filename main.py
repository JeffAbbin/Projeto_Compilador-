#Jefferson Abbin
#Pedro Henrique Cavalhieri Contessoto

import re
import sys



from CodeJPLexer import CodeJPLexer
from CodeJPParser import CodeJPParser
from CodeJPListener import CodeJPListener
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker

from antlr4.tree.Trees import Trees

variables = {}

arquivo = open('codigoAssembly.txt', 'w')

class LexicalAnalyzerFSM:
    def __init__(self):
        self.state = 'START'
        self.lexeme = ''
        self.tokens = []
        self.position = 0

    def transition(self, char):
        if self.state == 'START':
            if char in [' ', '\n', '\t']:  # Skip whitespace
                self.position += 1
                return
            elif char.isalpha() or char == '_':
                self.state = 'IDENTIFIER'
            elif char.isdigit():
                self.state = 'NUMBER'
            elif char in ['=', '!', '<', '>', '+', '-', '*', '/']:
                self.state = 'OPERATOR'
            elif char in ['(', ')', '{', '}', '[', ']', ',', ';']:
                self.state = 'MARKERS'
            else:
                print(f"Invalid token: {char}")
                return

            self.lexeme += char
        elif self.state == 'IDENTIFIER':
            if char.isalpha() or char.isdigit() or char == '_':
                self.lexeme += char
            elif self.lexeme in ["if", "while", "break", "do", "sleep", "WritePort", "ReadPort", "ReadSerial", "WriteSerial", "Writeanalog", "Readanalog"]:
              self.emit('KEYWORD')
              self.transition(char)
            else:
                self.emit('IDENTIFIER')
                self.transition(char)  # reprocess the current character
        elif self.state == 'NUMBER':
            if char.isdigit():
                self.lexeme += char
            elif char == '.':
                self.state = 'REAL'
                self.lexeme += char
            else:
                self.emit('NUMBER')
                self.transition(char)  # reprocess the current character
        elif self.state == 'REAL':
            if char.isdigit():
                self.lexeme += char
            else:
                self.emit('REAL')
                self.transition(char)  # reprocess the current character
        elif self.state == 'OPERATOR':
            self.lexeme += char
            if not self.lexeme in ['==', '!=', '<=', '>=']:
                self.lexeme = self.lexeme[:-1]
                self.emit('OPERATOR')
                self.transition(char)  # reprocess the current character
        
        elif self.state == 'MARKERS':
            self.lexeme += char
            self.lexeme = self.lexeme[:-1]
            self.emit('MARKERS')
            self.transition(char)  # reprocess the current character
              
    def emit(self, token_type):
        self.tokens.append((token_type, self.lexeme, self.position))
        self.position += len(self.lexeme)
        self.lexeme = ''
        self.state = 'START'

    def tokenize(self, code):
        for char in code:
            self.transition(char)
        if self.lexeme:  # handle the last token
            self.emit(self.state)
        return self.tokens

def read_code_from_file(file_name):
    with open(file_name, 'r') as file:
        code = file.read()
    return code

def create_token_table(tokens, file_name):
    with open(file_name, 'w') as file:
        for token_type, token, position in tokens:
            file.write(f"Token: {token}, Classe: {token_type}, Posição: {position}\n")

  # Função para verificar se uma variável foi declarada
def is_variable_declared(variable_name):
    return variable_name in variables

  # Função para verificar se os tipos das variáveis são compatíveis
def are_types_compatible(type1, type2):
  if not variables:
    return False

  if type1.isnumeric():
    return variables[type2] == 'int' or variables[type2] == 'float'

  if type2.isnumeric():
    return variables[type1] == 'int' or variables[type1] == 'float'
    
  return variables[type1] == variables[type2]


def tokenizeTable(code):
  token_pattern = r"(\b[a-zA-Z_][a-zA-Z0-9_]*\b|[0-9]+\.[0-9]*|[0-9]+|==|!=|<=|>=|<|>|\+|-|\*|/|=|\(|\)|\{|\}|\[|\]|,|;)"
  tokens = re.findall(token_pattern, code)
  return tokens

def Semanticanalyzer(tokens):
  for token in tokens:
    if(token == '+' or token == '-' or token == '*' or token == '/'):
      var1 = tokens[tokens.index(token) - 1]
      op = token
      var2 = tokens[tokens.index(token) + 1]
      if not var1.isnumeric():
        if not is_variable_declared(var1) :
          print(f"Erro: Variável '{var1}' não foi declarada.")
      if not var2.isnumeric():
        if not is_variable_declared(var2) :
          print(f"Erro: Variável '{var2}' não foi declarada.")
      if not are_types_compatible(var2, var1) :
        print(f"Erro: Variável '{var2}' e '{var1}' são de tipos difrentes .")
    
      
    if(token == '==' or token == '<' or token == '>' or token == '>=' or token == '<='):
      var1 = tokens[tokens.index(token) - 1]
      op = token
      var2 = tokens[tokens.index(token) + 1]
      if not var1.isnumeric():
          if not is_variable_declared(var1) :
            print(f"Erro: Variável '{var1}' não foi declarada.")
      if not var2.isnumeric():
        if not is_variable_declared(var2) :
          print(f"Erro: Variável '{var2}' não foi declarada.")
      if not are_types_compatible(var2, var1) :
        print(f"Erro: Variável '{var2}' e '{var1}' são de tipos difrentes .")

    
    if(token == '='):
    # Divide a linha em partes usando o sinal de igual
      var1 = tokens[tokens.index(token) - 1]
      op = token
      var2 = tokens[tokens.index(token) + 1]
      
      if not is_variable_declared(var1) :
          print(f"Erro: Variável '{var1}' não foi declarada.")
      if not are_types_compatible(var1, var2) :
          print(f"Erro: Variável '{var2}' e '{var1}' são de tipos difrentes .")
        
    if(token == 'int' or token == 'float' or token == 'bool' or token == 'char'):
            op = token
            var2 = tokens[tokens.index(token) + 1]
            variables[var2] = op

def create_asm(tokens, file_name):
  cochetes = 0
  with open(file_name, 'w') as file:
      for token in tokens:
          file.write(token + '\n')
          if(token == 'if'):
            num1 = tokens[tokens.index(token) + 2]
            op = tokens[tokens.index(token) + 3]
            num2 = tokens[tokens.index(token) + 4]
            cochetes = cochetes + 1
            isIf(num1,op, num2)
          if(token == 'WritePort'):
            num1 = tokens[tokens.index(token) + 2]
            bool = tokens[tokens.index(token) + 4]
            isWritePort(num1, bool)
          if(token == 'readPort'):
            num1 = tokens[tokens.index(token) + 2]
            bool = tokens[tokens.index(token) + 4]
            isreadPort(num1, bool)
          if(token == 'while'):
            num1 = tokens[tokens.index(token) + 2]
            op = tokens[tokens.index(token) + 3]
            num2 = tokens[tokens.index(token) + 4]
            cochetes = cochetes + 1
            iswhile(num1, op, num2)
          if(token == ('+' or '-' or '*')):
            num1 = tokens[tokens.index(token) - 1]
            op = token
            num2 = tokens[tokens.index(token) + 1]
            IsOperação(num1, op, num2)
          if(token == '}'):
            cochetes = cochetes - 1
          if(cochetes == 0 and token == '}'):
            arquivo.write('end_if:\n')
            arquivo.write('end_loop:\n ')
          if(token == 'int'):
            X = tokens[tokens.index(token) + 1]
            variavelbyte(X)  
          if(token == 'char'):
            X = tokens[tokens.index(token) + 1]
            variavelword(X) 
          if(token == '='):
            X = tokens[tokens.index(token) - 1]
            IsAtribuicao(X)
          if(token == 'sleep'):
            num = tokens[tokens.index(token) + 2]
            isSleep(num)

def conf():
  arquivo.write('#include <avr/io.h>\n')
  arquivo.write('#include <util/delay.h>\n')
  arquivo.write('.device ATmega328P\n')
  arquivo.write('.org 0x0000\n')


def isIf(num1,op, num2):
  if(op == '=='):
    arquivo.write('ldi r16, ',num1,'\n')
    arquivo.write('ldi r20, ',num2,'\n')
    arquivo.write('cp r20,r16\n ')
    arquivo.write('brne if_block\n ')
    arquivo.write('jmp end_if\n')
    arquivo.write('if_block:\n')


  if(op == '>'):
    arquivo.write('ldi r16, '+ num1 +'\n')
    arquivo.write('ldi r20, ' + num2 +'\n')
    arquivo.write('cp r20,r16\n ')
    arquivo.write('brlt if_block\n ')
    arquivo.write('jmp end_if\n')
    arquivo.write('if_block:\n')

  if(op == '<'):
    arquivo.write('ldi r16, '+ num1 +'\n')
    arquivo.write('ldi r20, ' + num2 +'\n')
    arquivo.write('cp r20,r16\n ')
    arquivo.write('brlo if_block\n ')
    arquivo.write('jmp end_if\n')
    arquivo.write('if_block:\n')


def isSleep(num):
  arquivo.write('delay_loop:\n')
  arquivo.write('ldi r16, '+ num + '\n')
  arquivo.write('inner_delay_loop:\n')
  arquivo.write('call _delay_ms\n')
  arquivo.write('dec r16\n')
  arquivo.write('brne inner_delay_loop\n')
  arquivo.write('dec r16\n')
  arquivo.write('brne delay_loop\n')


def isWritePort(num, bool):
  if(bool == 'true'):
    arquivo.write('sbi DDRB, '+ num +'\n')
    arquivo.write('sbi PORTB, '+ num +'\n')
  if(bool == 'false'):
    arquivo.write('sbi DDRB, '+ num +'\n')
    arquivo.write('cbi PORTB, '+ num +'\n')

def isreadPort(num, num2):
  arquivo.write('in r16, PINB\n')
  arquivo.write('andi r16, (1 << PB0)\n')

def iswhile(num1, op, num2):
  if(op == '=='):
    arquivo.write('ldi r16, '+ num1 +'\n')
    arquivo.write('ldi r20, '+ num2 +'\n')
    arquivo.write('loop:\n')
    arquivo.write('cp r20,r16\n ')
    arquivo.write('brne end_loop\n ')
    arquivo.write('jmp loop\n')
  if(op == '>'):
    arquivo.write('ldi r16, '+ num1 +'\n')
    arquivo.write('ldi r20, '+ num2 +'\n')
    arquivo.write('loop:\n')
    arquivo.write('cp r20,r16\n ')
    arquivo.write('jmp loop\n')

  if(op == '<'):
    arquivo.write('ldi r16, '+ num1 +'\n')
    arquivo.write('ldi r20, '+ num2 +'\n')
    arquivo.write('loop:\n')
    arquivo.write('cp r20,r16\n ')
    arquivo.write('brlo end_loop\n ')
    arquivo.write('jmp loop\n')

def IsOperação(num1, op, num2):

  if(op == '+'):
    arquivo.write('ldi r16, '+ num1 +'\n')
    arquivo.write('ldi r20, ' + num2 +'\n')
    arquivo.write('add r16, r20\n')

  if(op == '-'):
    arquivo.write('ldi r16, '+ num1 +'\n')
    arquivo.write('ldi r20, '+ num2 +'\n')
    arquivo.write('sub r16, r20\n')
  if(op == '*'):
    arquivo.write('ldi r16, '+ num1 +'\n')
    arquivo.write('ldi r20, ' + num2 +'\n')
    arquivo.write('mul r16, r20\n')

def IsAtribuicao(X):
   arquivo.write('mov '+ X + ', r16\n')

def variavelbyte(X):
  arquivo.write('.section .data\n')
  arquivo.write(X +': .byte 0\n')

def variavelword(X):
  arquivo.write('.section .data\n')
  arquivo.write(X +': .word 0\n')

if __name__ == "__main__":
    if sys.argv[1] != "code1.txt" and sys.argv[1] != "code2.txt" and sys.argv[1] != "code3.txt":
      print("Arquivo nao existe, escolha: code1.txt, code2.txt ou code3.txt")
      exit(1)

    code = read_code_from_file(sys.argv[1])
    analyzer = LexicalAnalyzerFSM()
    tokens = analyzer.tokenize(code)
    create_token_table(tokens, "token_table.txt")

    

  # print(tokens)
    
    input_stream = FileStream(sys.argv[1])
    lexer = CodeJPLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CodeJPParser(token_stream)
    tree = parser.program()

    print(Trees.toStringTree(tree, None, parser))

    # Separação dos tokens 
    token_index = tokenizeTable(code)

    print()

    Semanticanalyzer(token_index)

    create_asm(token_index, code)
  
   

    