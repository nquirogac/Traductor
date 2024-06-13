from grammar.gen.LatinoGrammarListener import LatinoGrammarListener
from grammar.gen.LatinoGrammarParser import LatinoGrammarParser
from translations.assignations import *
from translations.conditional import *
from translations.switch import *


class LatinoToJs(LatinoGrammarListener):

    def __init__(self):
        self.symbolArray = []  # Used to keep track of defined variables
        self.indentationStack = []  # Use to keep indentation levels when nesting blocks
        self.jsCode = ''
        self.passSemiColon = [';', '/', '}', '\n']
        self.boolean_and_null_translation = {
            'verdadero': 'true',
            'cierto': 'true',
            'falso': 'false',
            'nulo': 'null',
        }

    def enterSentence(self, ctx: LatinoGrammarParser.SentenceContext):
        # Determine what function to use based on what rule will be applied

        if ctx.assig():
            enterAssignationSentence(self, ctx)
        elif ctx.functionCall():
            print('Function calls need to go here')
        elif ctx.R_UNARY_OP():
            print('R_UNARY_OPS need to go here')
        elif ctx.builtInFuncSentence():
            print('Built in sentences go here')
        elif ctx.functionReturn():
            print('Function return goes here')
        elif ctx.doWhileBlock():
            print('Do while goes here')
        elif ctx.codeBlock():
            print('Do while goes here')
        elif ctx.opBuiltInTipo():
            print('Do while goes here')
        else:
            print('BREAK goes here')

    def exitSentence(self, ctx: LatinoGrammarParser.SentenceContext):
        self.jsCode += '\n'

    def enterAssig(self, ctx: LatinoGrammarParser.AssigContext):
        enterAssignationRule(self, ctx)

    def enterConditionalBlock(self, ctx: LatinoGrammarParser.ConditionalBlockContext):
        enterConditional(self, ctx)

    def exitConditionalBlock(self, ctx: LatinoGrammarParser.ConditionalBlockContext):
        exitConditional(self, ctx)

    def enterAltCondition(self, ctx: LatinoGrammarParser.AltConditionContext):
        enterAltConditional(self, ctx)

    def enterNoCondition(self, ctx: LatinoGrammarParser.NoConditionContext):
        enterNoConditional(self, ctx)

    def enterSwitchBlock(self, ctx: LatinoGrammarParser.SwitchBlockContext):
        enterSwitch(self, ctx)

    def exitSwitchBlock(self, ctx: LatinoGrammarParser.SwitchBlockContext):
        exitSwitch(self, ctx)

    def enterSwitchCasesDef(self, ctx: LatinoGrammarParser.SwitchCasesDefContext):
        enterSwitchCases(self, ctx)

    def exitSwitchCasesDef(self, ctx: LatinoGrammarParser.SwitchCasesDefContext):
        pass

    def exitSource(self, ctx: LatinoGrammarParser.SourceContext):
        print("----------------------JS CODE----------------------")
        print(self.jsCode)
