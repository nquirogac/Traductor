grammar LatinoGrammar;

source : (sentencia)* ;
sentencia : assignableId sentenciaId
    | builtInFuncsSingleArg
    | builtInFuncsMultiArg
    | builtInFuncsNoArg
    | codeBlock
    | functionReturn
    | 'romper';
sentenciaConcat : (sentencia)*;
builtInFuncsSingleArg : BuiltInFuncWordsSingleArg functionCallSingleArg;
builtInFuncsMultiArg : BuiltInFuncWordsMultiArg functionCall;
builtInFuncsNoArg : BuiltInFuncWordsNoArg '(' ')' ;
codeBlock : functionBlock
    | conditionalBlock
    | switchBlock
    | forBlock
    | whileBlock
    | forRangeBlock
    | doWhileBlock;
functionBlock : FunctionKeyword ID '(' functionArgsDef ')' sentencia sentenciaConcat 'fin' ;
functionArgsDef : (ID functionArgsDefConcat)? ;
functionArgsDefConcat : (',' ID )*;
functionReturn : ReturnKeyword assignableExpr ;
conditionalBlock : 'si' expr sentencia sentenciaConcat alternateCondition noCondition 'fin';
alternateCondition : ('osi' expr sentencia sentenciaConcat)* ;
noCondition : ('sino' sentencia sentenciaConcat)? ;
switchBlock : 'elegir' expr switchCase switchCaseConcat defaultCase 'fin';
switchCase : caseDef concatCaseDef sentencia sentenciaConcat;
caseDef : 'caso' caseValidExpr ':';
caseValidExpr : Tkn_real | Tkn_str ;
concatCaseDef : (caseDef)* ;
switchCaseConcat : (switchCase)* ;
defaultCase : defaultCaseToken ':' sentencia sentenciaConcat;
defaultCaseToken : 'defecto'| 'otro' ;
forBlock : 'desde (' assignableId AssignOp expr ';' expr ;
whileBlock : 'mientras' expr sentencia sentenciaConcat 'fin' ;
forRangeBlock : 'para' ID 'en rango ' '(' expr forRangeArgs2 ')' sentencia sentenciaConcat 'fin';
forRangeArgs2 : (',' expr)* ;
doWhileBlock : 'repetir' sentencia sentenciaConcat 'hasta' expr;
assignableId : mutableId assignableIdConcat;
mutableId : ID mutableIdModifierConcat;
mutableIdModifierConcat : (mutableIdModifier)*;
assignableIdConcat : (',' assignableId)?;
sentenciaId : AssignOp assignableValue | functionCall | RUnaryOperator ;
assignableValue : assignableExpr | 'leer' '(' ')'; //se podra x, y = leer(), 5 ???
assignableExpr : expr assignExprConcat;
assignExprConcat : (',' assignableExpr)?;
functionCall : '(' functionCallArgs ')';
functionCallArgs : (expr functionCallArgsConcat)? ;
functionCallArgsConcat : (',' expr )*;
functionCallSingleArg : '(' expr ')';
expr : terminal binaryOperation | '(' expr ')' binaryOperation ;
binaryOperation : (binaryOp expr)?;
mutableIdModifier : objectProperty | listAcess ;
objectProperty : '.' ID;
listAcess : '[' expr ']';
listDefinition : '[' listBody ']';
listBody : (assignableExpr)? ;
dictDefinition : '{' dictBody '}';
dictBody : (dictProperty dictPropertyConcat)? ;
dictProperty : expr ':' dictAssignableExpr;
dictAssignableExpr : expr | FunctionKeyword '(' functionArgsDef ')' sentencia sentenciaConcat 'fin';
dictPropertyConcat : (',' dictProperty)* ;
binaryOp : NumericOp | StringOp | LogicOp;
idExp : ID idModifier ;
idModifier : (mutableIdModifier)* | (functionCall)*;
terminal : 'nulo'
    | 'falso'
    | 'cierto'
    | 'verdadero'
    | Tkn_real
    | Tkn_str
    | idExp
    | LUnaryOperator terminal
    | OperableBuiltInFuncWords functionCallSingleArg
    | listDefinition
    | dictDefinition;
BuiltInFuncWordsSingleArg : 'escribir'
    | 'imprimir'
    | 'poner';
BuiltInFuncWordsMultiArg : 'imprimirf' ;
BuiltInFuncWordsNoArg : 'limpiar';
FunctionKeyword : 'funcion' | 'fun' ;
ReturnKeyword : 'retorno' | 'retornar' | 'ret' ;
AssignOp : '%=' | '/=' | '*=' | '-=' | '+=' | '=' ;
NumericOp : '+' | '-' | '*' | '/' | '^' | '%' ;
StringOp : '..' | '~=' ;
LogicOp : '&&' | '||' | '==' | '!=' | '<=' | '>=' | '<' | '>' ;
RUnaryOperator : '++' | '--' ;
LUnaryOperator : '+' | '-' | '!' ;
OperableBuiltInFuncWords : 'anumero' | 'acadena' | 'alogico' | 'tipo' ;


ID : [a-zA-Z_][a-zA-Z0-9_]* ;
Tkn_real : ('-')? DIGIT+ ('.' DIGIT+)? ;
Tkn_str : SingleQuotedString | DoubleQuotedString  ;
SingleQuotedString
    : '\'' (EscapeSequence | ~('\'' | '\\'))* '\'';
DoubleQuotedString
    : '"' (EscapeSequence | ~('"' | '\\'))* '"';
fragment EscapeSequence
    : '\\' [btnfrva0"'\\];

fragment HEX: [0-9a-fA-F] ;
fragment DIGIT : [0-9] ;
ESP : [ \t\r\n]+ -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;