from grammar.gen.LatinoGrammarListener import LatinoGrammarListener
from grammar.gen.LatinoGrammarParser import LatinoGrammarParser
from translations.assignations import *

from translations.conditional import *
from translations.switch import *

from translations.functions import *
from translations.structures import *


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
        self.infor = False
        self.rangeCreated = False

    def enterSentence(self, ctx: LatinoGrammarParser.SentenceContext):
        # Determine what function to use based on what rule will be applied

        if not self.infor:
            if self.indentationStack:
                for i in range(len(self.indentationStack)):
                    self.jsCode += '    '


        if ctx.assig():
            enterAssignationSentence(self, ctx)
        elif ctx.assignableID():
            if '.' not in ctx.assignableID().getText():
                self.jsCode += ctx.assignableID().getText()
            
        elif ctx.functionCall():
            print('Function calls need to go here')
        elif ctx.R_UNARY_OP():
            #print('R_UNARY_OPS need to go here')
            if not self.infor:
                self.jsCode += f'{ctx.assignableID().getText()}{ctx.R_UNARY_OP().getText()}'
            else:
                self.jsCode += f'{ctx.assignableID().getText()}{ctx.R_UNARY_OP().getText()})'
                self.jsCode += '{\n'

        elif ctx.builtInFuncSentence():
            print('Built in sentences go here')
        elif ctx.functionReturn():
            if '?~sentence' in self.jsCode:
                self.jsCode = self.jsCode.replace('?~sentence', '?~return', 1)
            else:
                self.jsCode += '?~return'
        elif ctx.doWhileBlock():
            print('Do while goes here')
        elif ctx.codeBlock():
            print('Do while goes here')

        elif ctx.opBuiltInTipo():
            print('Do while goes here')
        else:
            print('BREAK goes here')


    def exitSentence(self, ctx: LatinoGrammarParser.SentenceContext):
        
        if self.jsCode != '' and self.jsCode[-1] not in self.passSemiColon:
            self.jsCode += ';'
        self.jsCode += '\n'

        if not self.infor:
            self.jsCode += '\n'
        self.infor = False


    def enterAssig(self, ctx:LatinoGrammarParser.AssigContext):
        enterAssignationRule(self, ctx)

    def enterAssignableID(self, ctx:LatinoGrammarParser.AssignableIDContext):
        self.jsCode += ctx.ID().getText()

    def enterExp(self, ctx:LatinoGrammarParser.ExpContext):
        if '?~PrintArgs' in self.jsCode:
            defineArgsPrint(self, ctx)

        string_replacement = f'?~terminal'
        # Add terminal placeholders if there are binary operations
        operator = ''
        # TODO: translation of string operators
        for binary_op in ctx.binaryOp():
            if binary_op.L_UNARY_OP():
                operator = binary_op.L_UNARY_OP().getText()
            elif binary_op.NUMERIC_OP():
                operator = binary_op.NUMERIC_OP().getText()
            elif binary_op.LOGIC_OP():
                operator = binary_op.LOGIC_OP().getText()
            else:
                operator = binary_op.STRING_OP().getText()


            string_replacement += f'{operator}?~terminal'
        if '?~skip' not in self.jsCode:
            self.jsCode = self.jsCode.replace('?~exp', string_replacement, 1)
        


        self.jsCode = self.jsCode.replace('?~exp', string_replacement, 1)


    def enterTerminal(self, ctx:LatinoGrammarParser.TerminalContext):

        string_to_replace = ''
        # Complete the cases for terminal values including IDs
        if ctx.REAL():
            string_to_replace = ctx.REAL().getText()
        elif ctx.STRING():
            string_to_replace = ctx.STRING().getText()

        elif ctx.ID():
            if ctx.assignableIDModifiers():
                if ctx.functionCall():
                    string_to_replace = ctx.ID().getText() + '[?~exp](?~exp)?~nestedFunCall' 
                else:
                    string_to_replace = ctx.ID().getText() + '?~modifier'
            elif ctx.functionCall() and not ctx.assignableIDModifiers():
                string_to_replace = ctx.ID().getText() + '(?~funCall)'
            else:
                string_to_replace = ctx.ID().getText()

        elif ctx.BOOLEAN_VALS():
            string_to_replace = self.boolean_and_null_translation[ctx.BOOLEAN_VALS().getText()]
        elif ctx.NULL_VAL():
            string_to_replace = self.boolean_and_null_translation[ctx.NULL_VAL().getText()]
        elif ctx.OPENING_PAR():
            string_to_replace = f'(?~exp)'
        elif ctx.L_UNARY_OP():

            string_to_replace = f'{ctx.L_UNARY_OP().getText()}?~exp'
        elif ctx.opBuiltInTipo():
            string_to_replace = '?~opBT'
        elif ctx.listDefinition():
            string_to_replace = '?~listDef'

        elif ctx.ID():
            string_to_replace = ctx.ID().getText()

        self.jsCode = self.jsCode.replace('?~terminal', string_to_replace, 1)

    def exitSource(self, ctx:LatinoGrammarParser.SourceContext):
        print("----------------------JS CODE----------------------")
        print(self.jsCode)

    def enterWhileBlock(self, ctx: LatinoGrammarParser.WhileBlockContext):
        enterWhileBlockRule(self, ctx)

    def exitWhileBlock(self, ctx: LatinoGrammarParser.WhileBlockContext):
        exitWhileBlockRule(self, ctx)

    def enterDoWhileBlock(self, ctx: LatinoGrammarParser.DoWhileBlockContext):
        enterDoWhileBlockRule(self, ctx)


    def enterFunctionCall(self, ctx:LatinoGrammarParser.FunctionCallContext):
        enterFunctionCallRule(self, ctx)

    def enterBuiltInFuncSentence(self, ctx:LatinoGrammarParser.BuiltInFuncSentenceContext):
        enterBuiltInFuncSentenceRule(self, ctx)


    def enterListDefinition(self, ctx:LatinoGrammarParser.ListDefinitionContext):
        enterListDefRule(self, ctx)


    def enterAnonymousFuncDef(self, ctx:LatinoGrammarParser.AnonymousFuncDefContext):
        enterAnonymousFuncDefRule(self, ctx)


    def enterListAccess(self, ctx:LatinoGrammarParser.ListAccessContext):
        self.jsCode = self.jsCode.replace('?~modifier', '[?~exp]')

    def enterPropertyAccess(self, ctx:LatinoGrammarParser.PropertyAccessContext):
        if '?~modifier' in self.jsCode:
            self.jsCode = self.jsCode.replace('?~modifier', ctx.getText())
        else:
            self.jsCode += f'.{ctx.ID().getText()}'
        
    def enterAssignableID(self, ctx:LatinoGrammarParser.AssignableIDModifiersContext):
        if ctx.assignableIDModifiers():
            self.jsCode += ctx.ID().getText()

    def enterAssignableExp(self, ctx:LatinoGrammarParser.AssignableExpContext):
        if ctx.anonymousFuncDef():
            self.jsCode = self.jsCode.replace('?~exp', '?~anonFunc', 1)

  

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
        exitSwitchCases(self,ctx)
        pass

    

    def exitDoWhileBlock(self, ctx: LatinoGrammarParser.DoWhileBlockContext):
        exitDoWhileBlockRule(self, ctx)

    def enterForBlock(self, ctx:LatinoGrammarParser.ForBlockContext):
        enterForBlockRule(self, ctx)

    def exitForBlock(self, ctx:LatinoGrammarParser.ForBlockContext):
        exitForBlockRule(self, ctx)

    def enterForRangeBlock(self, ctx:LatinoGrammarParser.ForRangeBlockContext):
        enterForRangeBlockRule(self, ctx)

    def exitForRangeBlock(self, ctx:LatinoGrammarParser.ForRangeBlockContext):
        exitForRangeBlockRule(self, ctx)


