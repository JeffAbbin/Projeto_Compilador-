//# alunos: ISA STOHLER BERTOLACCINI e JEFFERSON SOBRINHO ABBIN
grammar PythonCode;

// Tokens não terminais
program : statement+ ;

statement : assignmentStatement
          | ifStatement
          | whileStatement
          | functionDeclaration
          | expressionStatement
          | returnStatement
          | printStatement
          | WritePortStatement
          | ReadPortStatement
          | WriteSerialStatement
          | sleepStatement
          | ReadSerialStatement
          | ReadanalogStatement;

assignmentStatement : variable '=' expression ;

ifStatement : 'if' '(' equality ')' '{' statement+ '}' ('else' '{' statement+ '}')? ;

whileStatement : 'while' '(' equality ')' '{' statement+ '}' ;

functionDeclaration : 'def' functionName '(' parameterList? ')' '{' statement+ '}' ;

expressionStatement : expression ';' ;

returnStatement : 'return' expression? ';' ;

printStatement : 'print' expressionList ';' ;

WritePortStatement : 'WritePort(' IDENTIFIER ',' BOOL ')\n';

ReadPortStatement : 'ReadPort(' IDENTIFIER ',' IDENTIFIER ')\n';

WriteSerialStatement : 'WriteSerial(' IDENTIFIER ',' IDENTIFIER ')\n';

ReadSerialStatement : 'ReadSerial(' IDENTIFIER ',' INT ')\n';

ReadanalogStatement : 'Readanalog(' IDENTIFIER ',' INT ')\n';

sleepStatement : 'sleep(' expression ')\n';

expressionList : expression (',' expression)* ;

parameterList : parameter (',' parameter)* ;

parameter : variable ;

equality : equality '==' rel | equality '!=' rel | rel | BOOL ;

rel : expression '<' expression | expression '<=' expression | expression '>=' expression | expression '>' expression ;

expression : primaryExpression (binaryOperator primaryExpression)* ;

primaryExpression : variable
                  | functionCall
                  | '(' expression ')' ;

functionCall : functionName '(' expressionList? ')' ;

variable : IDENTIFIER ;

functionName : IDENTIFIER ;

binaryOperator : '+' | '-' | '*' | '/' ;

IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ;

BOOL : 'true' | 'false' ;

INT : [0-9]+ ;

FLOAT : [0-9]+ '.' [0-9]* ;

WS : [ \t\n\r]+ -> skip ;


