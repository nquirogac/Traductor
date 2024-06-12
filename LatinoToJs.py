from grammar.gen.LatinoGrammarListener import LatinoGrammarListener
from grammar.gen.LatinoGrammarParser import LatinoGrammarParser
from translations.assignations import *


class LatinoToJs(LatinoGrammarListener):

    def __init__(self):
        self.symbolArray = [] # Used to keep track of defined variables
        self.indentationStack = [] # Use to keep indentation levels when nesting blocks
        self.jsCode = ''
        self.passSemiColon = [';', '/', '}','\n']
        self.boolean_and_null_translation = {
            'verdadero': 'true',
            'cierto': 'true',
            'falso': 'false',
            'nulo': 'null',
        }

    def enterSentence(self, ctx: LatinoGrammarParser.SentenceContext):
        enterSentenceFunc(self, ctx)

    def exitSentence(self, ctx: LatinoGrammarParser.SentenceContext):
        self.jsCode += '\n'

    def enterAssig(self, ctx:LatinoGrammarParser.AssigContext):
        enterAssignationFunc(self, ctx)

    def exitSource(self, ctx:LatinoGrammarParser.SourceContext):
        print("----------------------JS CODE----------------------")
        print(self.jsCode)