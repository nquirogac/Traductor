# Generated from /Users/nataliaquiroga/Desktop/Traductor/grammar/LatinoGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,4,12,2,0,7,0,1,0,1,0,1,0,1,0,5,0,7,8,0,10,0,12,0,10,9,0,1,0,
        0,0,1,0,0,0,11,0,2,1,0,0,0,2,3,5,1,0,0,3,8,5,3,0,0,4,5,5,2,0,0,5,
        7,5,3,0,0,6,4,1,0,0,0,7,10,1,0,0,0,8,6,1,0,0,0,8,9,1,0,0,0,9,1,1,
        0,0,0,10,8,1,0,0,0,1,8
    ]

class LatinoGrammarParser ( Parser ):

    grammarFileName = "LatinoGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hola'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "ESP" ]

    RULE_inicio = 0

    ruleNames =  [ "inicio" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    ESP=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LatinoGrammarParser.ID)
            else:
                return self.getToken(LatinoGrammarParser.ID, i)

        def getRuleIndex(self):
            return LatinoGrammarParser.RULE_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicio" ):
                listener.enterInicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicio" ):
                listener.exitInicio(self)




    def inicio(self):

        localctx = LatinoGrammarParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(LatinoGrammarParser.T__0)
            self.state = 3
            self.match(LatinoGrammarParser.ID)
            self.state = 8
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 4
                self.match(LatinoGrammarParser.T__1)
                self.state = 5
                self.match(LatinoGrammarParser.ID)
                self.state = 10
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





