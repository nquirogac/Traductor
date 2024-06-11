import antlr4
from antlr4 import *
from LatinoGrammarLexer import LatinoGrammarLexer
from LatinoGrammarParser import LatinoGrammarParser
from LatinoGrammarListenerTra import LatinoGrammarListenerTra

input_text = input("> ")
lexer = LatinoGrammarLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = LatinoGrammarParser(stream)
listener = LatinoGrammarListenerTra()
tree = parser.source()
walker = antlr4.ParseTreeWalker()
walker.walk(listener, tree)
# prin1t(tree.toStringTree(recog=parser))