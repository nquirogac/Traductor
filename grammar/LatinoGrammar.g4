grammar LatinoGrammar;

inicio  : 'hola' terminal (',' ID)* ;
source : (sentencia)* ;
sentencia: assignableId sentenciaId | 'romper';

assignableId : mutableId assignableIdConcat;
mutableId : ID mutableIdModifierConcat;
mutableIdModifierConcat : (mutableIdModifier)*;
assignableIdConcat : (',' assignableId)*;

sentenciaId : AssignOp assignableValue | functionCall | RUnaryOperator ;
assignableValue : assignableExpr | 'leer' '(' ')'; //se podra x, y = leer(), 5 ???
assignableExpr : expr assignExprConcat;
assignExprConcat : (',' assignableExpr)*;

functionCall : '(' functionCallArgs ')';
functionCallArgs : (expr functionCallArgsConcat)* ;
functionCallArgsConcat : (',' expr )*;
functionCallSingleArg : '(' expr ')';
expr :  expr binaryOp expr  | '(' expr ')' binaryOp expr | terminal ;

mutableIdModifier : objectProperty | listAcess ;
objectProperty : '.' ID;
listAcess : '[' expr ']';

binaryOp : NumericOp | StringOp | LogicOp;
idExp : ID idModifier ;
idModifier : (mutableIdModifier)* | (functionCall)*;
terminal : 'nulo'
         | 'falso'
         | 'cierto'
         | 'verdadero'
         | Tkn_real
         | idExp
         | LUnaryOperator terminal
         | OperableBuiltInFuncWords functionCallSingleArg; //falta str, ListDefinition, DictDefinition
AssignOp : '%=' | '/=' | '*=' | '-=' | '+=' | '=' ;
NumericOp : '+' | '-' | '*' | '/' | '^' | '%' ;
StringOp : '..' | '~=' ;
LogicOp : '&&' | '||' | '==' | '!=' | '<=' | '>=' | '<' | '>' ;
RUnaryOperator : '++' | '--' ;
LUnaryOperator : '+' | '-' | '!' ;
OperableBuiltInFuncWords : 'anumero' | 'acadena' | 'alogico' | 'tipo' ;


ID : [a-zA-Z_][a-zA-Z0-9_]* ;
Tkn_real : DIGIT+ ('.' DIGIT+)?;
fragment DIGIT : [0-9] ;
ESP : [ \t\r\n]+ -> skip ;
