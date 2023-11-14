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
lacos = {}
cochetes = 0
vareg = {}



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
  
  if type1.isnumeric() and type2.isnumeric():
    return True

  if type1.isnumeric():
    return variables[type2] == 'int' or variables[type2] == 'float'

  if type2.isnumeric():
    return variables[type1] == 'int' or variables[type1] == 'float'

  if not variables:
    return False
    
  return variables[type1] == variables[type2]


def tokenizeTable(code):
  token_pattern = r"(\b[a-zA-Z_][a-zA-Z0-9_]*\b|[0-9]+\.[0-9]*|[0-9]+|==|!=|<=|>=|<|>|\+|-|\*|/|=|\(|\)|\{|\}|\[|\]|,|;)"
  tokens = re.findall(token_pattern, code)
  return tokens

def Semanticanalyzer(tokens):
  position = 0
  for token in tokens:

    if(token == '+' or token == '-' or token == '*' or token == '/'):
      var1 = tokens[position - 1]
      op = token
      var2 = tokens[position + 1]
      if not var1.isnumeric():
        if not is_variable_declared(var1) :
          print(f"Erro: Variável '{var1}' não foi declarada.")
      if not var2.isnumeric():
        if not is_variable_declared(var2) :
          print(f"Erro: Variável '{var2}' não foi declarada.")
      if not are_types_compatible(var2, var1) :
        print(f"Erro: Variável '{var2}' e '{var1}' são de tipos difrentes .")
    
      
    if(token == '==' or token == '<' or token == '>' or token == '>=' or token == '<='):
      var1 = tokens[position - 1]
      op = token
      var2 = tokens[position + 1]
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
      var1 = tokens[position - 1]
      op = token
      var2 = tokens[position + 1]
      
      if not is_variable_declared(var1) :
          print(f"Erro: Variável '{var1}' não foi declarada.")
      if not are_types_compatible(var1, var2) :
          print(f"Erro: Variável '{var2}' e '{var1}' são de tipos difrentes .")
        
    if(token == 'int' or token == 'float' or token == 'bool' or token == 'char'):
            op = token
            var2 = tokens[position + 1]
            variables[var2] = op

    position += 1

def create_asm(tokens):
  cochetes = 0
  contSleep = 0
  contVar= 0
  conf()
  position = 0
  contIf = 0
  for token in tokens:
      if token == 'if':
          contIf += 1 
          num1 = tokens[position + 2]
          op = tokens[position + 3]
          num2 = tokens[position + 4]
          lacos[cochetes] = token
         
          if num1.isnumeric():
            arquivo.write('ldi r16, {}\n'.format(num1))
          if num2.isnumeric():
            arquivo.write('ldi r17, {}\n'.format(num2))
          
          arquivo.write('rjmp if{}\n'.format(cochetes + contIf))
          arquivo.write('shorif{}:\n'.format(cochetes + contIf))
          arquivo.write('jmp end_if{}\n'.format(cochetes + contIf))
          arquivo.write('if{}:\n'.format(cochetes + contIf))
          arquivo.write('cp ')
          if num1.isnumeric():
            arquivo.write('r16,')
          else:
            arquivo.write('{},'.format(vareg[num1]))
          if num2.isnumeric():
            arquivo.write(' r17\n')
          else:
            arquivo.write(' {}\n'.format(vareg[num2]))
          if op == '==':
              arquivo.write('brne shorif{}\n'.format(cochetes + contIf))
          elif op == '>':
              arquivo.write('brlo shorif{}\n'.format(cochetes + contIf))
          elif op == '<':
              arquivo.write('brsh shorif{}\n'.format(cochetes + contIf))
          
          cochetes += 1
      elif token == 'writeport':
          
          num1 = tokens[position + 2]
          bool_val = tokens[position + 4]
        
          isWritePort(num1, bool_val)
      elif token == 'readport':
          num1 = tokens[position + 2]
          var = tokens[position + 4]
          isreadPort(num1, var)
      elif token == 'while':
          num1 = tokens[position + 2]
          op = tokens[position + 3]
          num2 = tokens[position + 4]
          lacos[cochetes] = token
        
          arquivo.write('ldi r20, {}\n'.format(num1))
          arquivo.write('ldi r21, {}\n'.format(num2))
          arquivo.write('rjmp while{}\n'.format(cochetes))
          arquivo.write('shorloop{}:\n'.format(cochetes))
          arquivo.write('jmp end_loop{}\n'.format(cochetes))
          arquivo.write('while{}:\n'.format(cochetes))
          arquivo.write('cp r20, r21\n')
          if op == '==':
              arquivo.write('brne shorloop{}\n'.format(cochetes))
          elif op == '>':
              arquivo.write('brlo shorloop{}\n'.format(cochetes))
          elif op == '<':
              arquivo.write('brsh shorloop{}\n'.format(cochetes))
          # Continuar com a lógica para o corpo do loop aqui
          
          cochetes += 1
      elif token in ['+', '-', '*']:
          num1 = tokens[position - 1]
          op = token
          num2 = tokens[position + 1]
          IsOperacao(num1, op, num2)


      elif token == '}':
        cochetes -= 1
        if lacos[cochetes] == 'if':
          arquivo.write('end_if{}:\n'.format(cochetes + contIf))
        elif lacos[cochetes] == 'while':
          arquivo.write('rjmp while{}\n'.format(cochetes))
          arquivo.write('end_loop{}:\n'.format(cochetes))
        
      elif token == '=':
          X = tokens[position - 1]
          valor = tokens[position + 1]
          IsAtribuicao(X, valor)
      elif token == 'bool' or token == 'int':
        var = tokens[position + 1]
        r = 22 + contVar
        reg = 'r{}'.format(r)
        vareg[var] = reg
      elif token == 'sleep':
          contSleep += 1
          num = tokens[position + 2]
          isSleep(num, contSleep)
      position += 1

def conf():
  arquivo.write('#define __SFR_OFFSET 0x00\n')
  arquivo.write('#include <avr/io.h>\n')
  arquivo.write('.global program\n')
  arquivo.write('program:\n')
  arquivo.write('ldi   r18,0xFF          ;carrega FFh no registrador auxiliar 18\n')
  arquivo.write('out   DDRA,r18          ;configura portA como saída\n')
  arquivo.write('out   PORTC,r18         ;configura o PC com pull-up interno. inicializa PC, em low\n')



def isIf(num1, op, num2):
  # Implementação da lógica para a instrução if
  arquivo.write('ldi r10, {}\n'.format(num1))
  arquivo.write('ldi r12, {}\n'.format(num2))
  arquivo.write('cp r10, r12\n')
  if op == '==':
      arquivo.write('brne else_block\n')
  elif op == '>':
      arquivo.write('brlo else_block\n')
  elif op == '<':
      arquivo.write('brsh else_block\n')
  # Continuar com a lógica para o bloco if aqui
  arquivo.write('rjmp endif_block\n')
  arquivo.write('else_block:\n')
  # Continuar com a lógica para o bloco else aqui
  arquivo.write('endif_block:\n')

def isSleep(num, contSleep):
  # Implementação da lógica para a função sleep
  arquivo.write('ldi   r17,200\n')
  arquivo.write('ldi r18, {}\n' .format(int(float(num)//0.2)))
  arquivo.write('aux1{}:\n'.format(contSleep))
  arquivo.write('ldi   r16,250\n')
  arquivo.write('aux2{}:\n'.format(contSleep))
  arquivo.write('nop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\nnop\n')
  arquivo.write('dec   r16\n')
  arquivo.write('breq  dec_r17{}\n'.format(contSleep))
  arquivo.write('rjmp  aux2{}\n'.format(contSleep))
  arquivo.write('dec_r17{}:\n'.format(contSleep))
  arquivo.write('dec  r17\n')
  arquivo.write('breq  dec_r18{}\n'.format(contSleep))
  arquivo.write('rjmp  aux1{}\n'.format(contSleep))
  arquivo.write('dec_r18{}:\n'.format(contSleep))
  arquivo.write('dec  r18\n')
  arquivo.write('breq  endloopSleep{}\n'.format(contSleep))
  arquivo.write('rjmp  aux1{}\n'.format(contSleep))
  arquivo.write('endloopSleep{}:\n'.format(contSleep))
  

def isWritePort(num, bool_val):
  if bool_val == 'true':
      arquivo.write('sbi PORTA, {}\n'.format(num))  # Configura o pino em alto
  else:
      arquivo.write('cbi PORTA, {}\n'.format(num))  # Configura o pino em baixo

def isreadPort(num, var):
  # Implementação da lógica para ler de uma porta
  
  arquivo.write('readPort{}:\n'.format(num))
  arquivo.write('sbis PINC, {}; Testa o bit correspondente ao pino\n'.format(num))
  arquivo.write('rjmp pinLow          ; Se o bit for 0, o pino está em nível baixo\n')
  arquivo.write('pinHigh:\n')
  arquivo.write('ldi {}, 1 \n'. format(vareg[var]))
  arquivo.write('rjmp EndreadPort{}\n'.format(num))
  arquivo.write('pinLow:\n')
  arquivo.write('ldi {}, 0 \n'. format(vareg[var]))
  arquivo.write('EndreadPort{}:\n'.format(num))



def IsOperacao(num1, op, num2):
  # Implementação da lógica para operações aritméticas
  arquivo.write('ldi r16, {}\n'.format(num1))
  arquivo.write('ldi r17, {}\n'.format(num2))
  if op == '+':
      arquivo.write('add r16, r17\n')
  elif op == '-':
      arquivo.write('sub r16, r17\n')
  elif op == '*':
      arquivo.write('mul r16, r17\n')

def IsAtribuicao(X, valor):
  # Implementação da lógica para atribuição
  arquivo.write('ldi r16, {}\n'.format(valor))
  arquivo.write('sts {}, r16\n'.format(X))




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


    Semanticanalyzer(token_index)

    create_asm(token_index)
  
   

    