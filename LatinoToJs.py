from grammar.gen.LatinoGrammarListener import LatinoGrammarListener
from grammar.gen.LatinoGrammarParser import LatinoGrammarParser
from translations.assignations import *


class LatinoToJs(LatinoGrammarListener):

    def __init__(self):
        self.symbolArray = []  # Used to keep track of defined variables
        self.indentationStack = []  # Use to keep indentation levels when nesting blocks
        self.jsCode = ''
        self.passSemiColon = [';', '/', '}','\n']
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

    def enterAssig(self, ctx:LatinoGrammarParser.AssigContext):
        enterAssignationRule(self, ctx)

    def enterExp(self, ctx:LatinoGrammarParser.ExpContext):

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

            string_replacement += f' {operator} ?~terminal'

        self.jsCode = self.jsCode.replace('?~exp', string_replacement, 1)

    def enterTerminal(self, ctx:LatinoGrammarParser.TerminalContext):

        string_to_replace = ''
        # TODO: complete the cases, hopefully it won't become spaghetti
        if ctx.REAL():
            string_to_replace = ctx.REAL().getText()
        elif ctx.STRING():
            string_to_replace = ctx.STRING().getText()
        elif ctx.BOOLEAN_VALS():
            string_to_replace = self.boolean_and_null_translation[ctx.BOOLEAN_VALS().getText()]
        elif ctx.NULL_VAL():
            string_to_replace = self.boolean_and_null_translation[ctx.NULL_VAL().getText()]
        elif ctx.OPENING_PAR():
            string_to_replace = f'(?~exp)'
        elif ctx.L_UNARY_OP():
            string_to_replace = f'{ctx.L_UNARY_OP().getText()} ?~exp'

        self.jsCode = self.jsCode.replace('?~terminal', string_to_replace, 1)

    def exitSource(self, ctx:LatinoGrammarParser.SourceContext):
        print("----------------------JS CODE----------------------")
        print(self.jsCode)
