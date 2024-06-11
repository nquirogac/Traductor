# Generated from P:/Universidad/8 Semestre 2024-1/Lenguajes de Programacion/Trabajos en grupo/Traductor/grammar/LatinoGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LatinoGrammarParser import LatinoGrammarParser
else:
    from LatinoGrammarParser import LatinoGrammarParser

# This class defines a complete listener for a parse tree produced by LatinoGrammarParser.
class LatinoGrammarListenerTra(ParseTreeListener):

    # Enter a parse tree produced by LatinoGrammarParser#source.
    def enterSource(self, ctx:LatinoGrammarParser.SourceContext):
        self.jsCode=''
        self.expr=''
        pass

    # Exit a parse tree produced by LatinoGrammarParser#source.
    def exitSource(self, ctx:LatinoGrammarParser.SourceContext):
        print("----JS CODE----")
        print(self.jsCode)
        pass


    # Enter a parse tree produced by LatinoGrammarParser#sentence.
    def enterSentence(self, ctx:LatinoGrammarParser.SentenceContext):
        self.sent = ''
        pass

    # Exit a parse tree produced by LatinoGrammarParser#sentence.
    def exitSentence(self, ctx:LatinoGrammarParser.SentenceContext):
        if ctx.parentCtx.getRuleIndex() == 26:
            self.sentence.append(self.sent+'\n')
        elif ctx.parentCtx.getRuleIndex() == 27:
            self.altSentences.append(self.sent+'\n')
        elif ctx.parentCtx.getRuleIndex() == 28:
            self.altSentences.append(self.sent+'\n')
        else:
            self.jsCode += self.sent+'\n'
        self.sent=''
        pass


    # Enter a parse tree produced by LatinoGrammarParser#assignableID.
    def enterAssignableID(self, ctx:LatinoGrammarParser.AssignableIDContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#assignableID.
    def exitAssignableID(self, ctx:LatinoGrammarParser.AssignableIDContext):
        #Temporal a la espera de asignaciones multiples
        self.sent+= ctx.getText()
        pass


    # Enter a parse tree produced by LatinoGrammarParser#assignableIDModifiers.
    def enterAssignableIDModifiers(self, ctx:LatinoGrammarParser.AssignableIDModifiersContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#assignableIDModifiers.
    def exitAssignableIDModifiers(self, ctx:LatinoGrammarParser.AssignableIDModifiersContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#listAccess.
    def enterListAccess(self, ctx:LatinoGrammarParser.ListAccessContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#listAccess.
    def exitListAccess(self, ctx:LatinoGrammarParser.ListAccessContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#propertyAccess.
    def enterPropertyAccess(self, ctx:LatinoGrammarParser.PropertyAccessContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#propertyAccess.
    def exitPropertyAccess(self, ctx:LatinoGrammarParser.PropertyAccessContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#assig.
    def enterAssig(self, ctx:LatinoGrammarParser.AssigContext):
        self.sent+=ctx.ASSIGN_OP().getText()
        pass

    # Exit a parse tree produced by LatinoGrammarParser#assig.
    def exitAssig(self, ctx:LatinoGrammarParser.AssigContext):

        pass


    # Enter a parse tree produced by LatinoGrammarParser#exp.
    def enterExp(self, ctx:LatinoGrammarParser.ExpContext):

        if ctx.parentCtx.getRuleIndex() == 26 or ctx.parentCtx.getRuleIndex() == 27:
            self.expr='('

        pass

    # Exit a parse tree produced by LatinoGrammarParser#exp.
    def exitExp(self, ctx:LatinoGrammarParser.ExpContext):
        if ctx.parentCtx.getRuleIndex() == 26:
            self.exprBool = self.expr + ')'
        elif ctx.parentCtx.getRuleIndex() == 27:
            self.altExpBool = self.expr + ')'
        else:
            self.sent += self.expr
        self.expr = ''
        pass


    # Enter a parse tree produced by LatinoGrammarParser#binaryOp.
    def enterBinaryOp(self, ctx:LatinoGrammarParser.BinaryOpContext):
        self.expr += ctx.getChild(0).getText()+' '
        pass

    # Exit a parse tree produced by LatinoGrammarParser#binaryOp.
    def exitBinaryOp(self, ctx:LatinoGrammarParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#terminal.
    def enterTerminal(self, ctx:LatinoGrammarParser.TerminalContext):
        #TODO verificar cada caso de los terminales
        term = ctx.getText()
        if term == 'verdadero' or term == 'cierto':
            term = 'true'
        if term == 'falso':
            term = 'false'
        self.expr += term+' '
        pass

    # Exit a parse tree produced by LatinoGrammarParser#terminal.
    def exitTerminal(self, ctx:LatinoGrammarParser.TerminalContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#opBuiltInTipo.
    def enterOpBuiltInTipo(self, ctx:LatinoGrammarParser.OpBuiltInTipoContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#opBuiltInTipo.
    def exitOpBuiltInTipo(self, ctx:LatinoGrammarParser.OpBuiltInTipoContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#assignableExp.
    def enterAssignableExp(self, ctx:LatinoGrammarParser.AssignableExpContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#assignableExp.
    def exitAssignableExp(self, ctx:LatinoGrammarParser.AssignableExpContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#functionCall.
    def enterFunctionCall(self, ctx:LatinoGrammarParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#functionCall.
    def exitFunctionCall(self, ctx:LatinoGrammarParser.FunctionCallContext):
        self.sent+=ctx.getText()
        pass


    # Enter a parse tree produced by LatinoGrammarParser#anonymousFuncDef.
    def enterAnonymousFuncDef(self, ctx:LatinoGrammarParser.AnonymousFuncDefContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#anonymousFuncDef.
    def exitAnonymousFuncDef(self, ctx:LatinoGrammarParser.AnonymousFuncDefContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#listDefinition.
    def enterListDefinition(self, ctx:LatinoGrammarParser.ListDefinitionContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#listDefinition.
    def exitListDefinition(self, ctx:LatinoGrammarParser.ListDefinitionContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#dictDefinition.
    def enterDictDefinition(self, ctx:LatinoGrammarParser.DictDefinitionContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#dictDefinition.
    def exitDictDefinition(self, ctx:LatinoGrammarParser.DictDefinitionContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#optionalAssignableExpConcat.
    def enterOptionalAssignableExpConcat(self, ctx:LatinoGrammarParser.OptionalAssignableExpConcatContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#optionalAssignableExpConcat.
    def exitOptionalAssignableExpConcat(self, ctx:LatinoGrammarParser.OptionalAssignableExpConcatContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#optAssigExpConcatWithTrail.
    def enterOptAssigExpConcatWithTrail(self, ctx:LatinoGrammarParser.OptAssigExpConcatWithTrailContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#optAssigExpConcatWithTrail.
    def exitOptAssigExpConcatWithTrail(self, ctx:LatinoGrammarParser.OptAssigExpConcatWithTrailContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#functionReturn.
    def enterFunctionReturn(self, ctx:LatinoGrammarParser.FunctionReturnContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#functionReturn.
    def exitFunctionReturn(self, ctx:LatinoGrammarParser.FunctionReturnContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#builtInFuncSentence.
    def enterBuiltInFuncSentence(self, ctx:LatinoGrammarParser.BuiltInFuncSentenceContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#builtInFuncSentence.
    def exitBuiltInFuncSentence(self, ctx:LatinoGrammarParser.BuiltInFuncSentenceContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#codeBlock.
    def enterCodeBlock(self, ctx:LatinoGrammarParser.CodeBlockContext):
        self.codeBlock=''
        pass

    # Exit a parse tree produced by LatinoGrammarParser#codeBlock.
    def exitCodeBlock(self, ctx:LatinoGrammarParser.CodeBlockContext):
        self.sent+=self.codeBlock
        pass


    # Enter a parse tree produced by LatinoGrammarParser#functionBlock.
    def enterFunctionBlock(self, ctx:LatinoGrammarParser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#functionBlock.
    def exitFunctionBlock(self, ctx:LatinoGrammarParser.FunctionBlockContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#whileBlock.
    def enterWhileBlock(self, ctx:LatinoGrammarParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#whileBlock.
    def exitWhileBlock(self, ctx:LatinoGrammarParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#forBlock.
    def enterForBlock(self, ctx:LatinoGrammarParser.ForBlockContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#forBlock.
    def exitForBlock(self, ctx:LatinoGrammarParser.ForBlockContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#forRangeBlock.
    def enterForRangeBlock(self, ctx:LatinoGrammarParser.ForRangeBlockContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#forRangeBlock.
    def exitForRangeBlock(self, ctx:LatinoGrammarParser.ForRangeBlockContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#doWhileBlock.
    def enterDoWhileBlock(self, ctx:LatinoGrammarParser.DoWhileBlockContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#doWhileBlock.
    def exitDoWhileBlock(self, ctx:LatinoGrammarParser.DoWhileBlockContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#conditionalBlock.
    def enterConditionalBlock(self, ctx:LatinoGrammarParser.ConditionalBlockContext):
        print(ctx.getChildCount())
        self.exprBool = ''
        self.sentence = []
        self.altConditions = []
        self.noCond = ''
        pass

    # Exit a parse tree produced by LatinoGrammarParser#conditionalBlock.
    def exitConditionalBlock(self, ctx:LatinoGrammarParser.ConditionalBlockContext):
        if ctx.IF() is not None:
            self.codeBlock += (f'if {self.exprBool}' + "{\n\t" + "\t".join(self.sentence)+"}"
                               + ''.join(self.altConditions) + self.noCond)
        pass

    # Enter a parse tree produced by LatinoGrammarParser#altCondition.
    def enterAltCondition(self, ctx:LatinoGrammarParser.AltConditionContext):
        self.altSentences = []
        self.altExpBool = ''
        pass

    # Exit a parse tree produced by LatinoGrammarParser#altCondition.
    def exitAltCondition(self, ctx:LatinoGrammarParser.AltConditionContext):
        self.altConditions.append(f'else if {self.altExpBool}' + '{\n\t' + "\t".join(self.altSentences)+"}")
        pass


    # Enter a parse tree produced by LatinoGrammarParser#noCondition.
    def enterNoCondition(self, ctx:LatinoGrammarParser.NoConditionContext):
        self.altSentences = []

        pass

    # Exit a parse tree produced by LatinoGrammarParser#noCondition.
    def exitNoCondition(self, ctx:LatinoGrammarParser.NoConditionContext):
        self.noCond+='else' + '{\n\t' + "\t".join(self.altSentences)+"}"
        pass

    # Enter a parse tree produced by LatinoGrammarParser#switchBlock.
    def enterSwitchBlock(self, ctx:LatinoGrammarParser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#switchBlock.
    def exitSwitchBlock(self, ctx:LatinoGrammarParser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by LatinoGrammarParser#switchCasesDef.
    def enterSwitchCasesDef(self, ctx:LatinoGrammarParser.SwitchCasesDefContext):
        pass

    # Exit a parse tree produced by LatinoGrammarParser#switchCasesDef.
    def exitSwitchCasesDef(self, ctx:LatinoGrammarParser.SwitchCasesDefContext):
        pass



del LatinoGrammarParser