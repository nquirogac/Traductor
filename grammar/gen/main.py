from antlr4 import *
from LatinoGrammarLexer import LatinoGrammarLexer
from LatinoGrammarParser import LatinoGrammarParser


input_text = input("> ")
lexer = LatinoGrammarLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = LatinoGrammarParser(stream)

tree = parser.inicio()

print(tree.toStringTree(recog=parser))