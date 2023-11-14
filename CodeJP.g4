grammar CodeJP;

program: decls stmts;
decls: (decl decls)? ;
decl: type ID ';';
type: BASIC ;

stmts: (stmt stmts)? ;
bool: join ('||' join)* ;
join: equality ('&&' equality)* ;
equality: rel (('==' | '!=') rel)? ;
rel: expr (('<' | '<=' | '>=' | '>') expr)? ;
expr: term (('+' | '-') term)* ;
term: unary (('*' | '/') unary)* ;
unary: '!' unary | factor ;
factor:  NUM | REAL | 'true' | 'false' | STRING | ID;

stmt: 'if' '(' bool ')' block ('else' block )? 
    | 'while' '(' bool ')' block 
    | 'do' block 'while' '(' bool ')' ';'
    | 'break' ';'
    | 'writeport' '(' factor ',' factor ')' ';'
    | 'readport' '(' factor ',' ID ')' ';'
    | 'ReadSerial' '(' ID ',' expr ')' ';'
    | 'WriteSerial' '(' ID ',' (STRING | NUM) ')' ';'
    | 'Writeanalog' '(' ID ',' expr ')' ';'
    | 'Readanalog' '(' ID ',' STRING ')' ';'
    | 'sleep' '(' expr ')' ';'
    | ID '=' expr ';'
    ;

block: '{' stmts '}' | stmt ;

BASIC: 'int' | 'float' | 'char' | 'bool' ;
ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUM: [0-9]+ ;
REAL: [0-9]+ '.' [0-9]* ;
CHAR: [0-9a-zA-Z!@#$%¨&*()_+={}] ;
STRING: '"' (~["\n\r])* '"' ;
WS: [ \t\r\n]+ -> skip ;