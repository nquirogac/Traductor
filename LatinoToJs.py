from grammar.gen.LatinoGrammarListener import LatinoGrammarListener
from grammar.gen.LatinoGrammarParser import LatinoGrammarParser
from translations.assignations import *
from translations.functions import *
from translations.structures import *

class LatinoToJs(LatinoGrammarListener):

    def __init__(self):
        self.symbolArray = []  # Used to keep track of defined variables
        self.indentationStack = []  # Use to keep indentation levels when nesting blocks
        self.jsCode = ''
        self.passSemiColon = [';', '/', '}','\n']
        self.boolean_and_null_translation = {
            'verdadero': 'true', '"verdadero"': '"true"',
            'cierto': 'true',
            'falso': 'false',
            'nulo': 'null',
        }

    def enterSentence(self, ctx: LatinoGrammarParser.SentenceContext):
        # Determine what function to use based on what rule will be applied
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
            print('R_UNARY_OPS need to go here')
        elif ctx.functionReturn():
            if '?~sentence' in self.jsCode:
                self.jsCode = self.jsCode.replace('?~sentence', '?~return', 1)
            else:
                self.jsCode += '?~return'
        elif ctx.doWhileBlock():
            print('Do while goes here')
        elif ctx.codeBlock():
            print('Do while goes here')
        

    def exitSentence(self, ctx: LatinoGrammarParser.SentenceContext):
        
        if self.jsCode != '' and self.jsCode[-1] not in self.passSemiColon:
            self.jsCode += ';'
        self.jsCode += '\n'

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
                operator = binary_op.STRING_OP().getText().replace('..', '+')

            string_replacement += f'{operator}?~terminal'
        if '?~skip' not in self.jsCode:
            self.jsCode = self.jsCode.replace('?~exp', string_replacement, 1)
        

    def enterTerminal(self, ctx:LatinoGrammarParser.TerminalContext):
        string_to_replace = ''
        # TODO: complete the cases, hopefully it won't become spaghetti
        if '?~skip' in self.jsCode:
            self.jsCode = self.jsCode.replace('?~skip', '')
        elif ctx.REAL():
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
        self.jsCode = self.jsCode.replace('?~terminal', string_to_replace, 1)

    def enterOpBuiltInTipo(self, ctx:LatinoGrammarParser.OpBuiltInTipoContext):
        enterOpBuiltInTipoRule(self, ctx)

    def enterFunctionBlock(self, ctx:LatinoGrammarParser.FunctionBlockContext):
        enterFunctionBlockRule(self, ctx)

    def exitFunctionBlock(self, ctx:LatinoGrammarParser.FunctionBlockContext):
        exitFunctionBlockRule(self, ctx)

    def enterFunctionReturn(self, ctx:LatinoGrammarParser.FunctionReturnContext):
        enterFunctionReturnRule(self, ctx)

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

    def exitSource(self, ctx:LatinoGrammarParser.SourceContext):
        print("----------------------JS CODE----------------------")
        print(self.jsCode)
