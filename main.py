import re
import sys

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

if __name__ == "__main__":
    if sys.argv[1] != "code1.txt" and sys.argv[1] != "code2.txt" and sys.argv[1] != "code3.txt":
      print("Arquivo nao existe, escolha: code1.txt, code2.txt ou code3.txt")
      exit(1)

    code = read_code_from_file(sys.argv[1])
    analyzer = LexicalAnalyzerFSM()
    tokens = analyzer.tokenize(code)
    create_token_table(tokens, "token_table.txt")