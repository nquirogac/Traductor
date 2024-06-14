
from grammar.gen.LatinoGrammarParser import LatinoGrammarParser

def enterConditional(latinoToJSInstance, ctx: LatinoGrammarParser.ConditionalBlockContext):
    exp = ctx.exp().getText()
    init_if = 'if '+'?~exp' if exp[0] == '(' and exp[-1] == ')' else f'if ('+'?~exp'+')'
    latinoToJSInstance.jsCode += init_if + '{\n'
    latinoToJSInstance.indentationStack.append(1)

def exitConditional(latinoToJSInstance, ctx: LatinoGrammarParser.ConditionalBlockContext):
    latinoToJSInstance.indentationStack.pop()
    latinoToJSInstance.jsCode += '    '*len(latinoToJSInstance.indentationStack)+'}'

    pass

def enterAltConditional(latinoToJSInstance, ctx: LatinoGrammarParser.AltConditionContext):
    exp = ctx.exp().getText()
    init_else_if = f' else if '+'?~exp' if exp[0] == '(' and exp[-1] == ')' else f'else if ('+'?~exp'+')'
    latinoToJSInstance.jsCode += '}' + init_else_if + '{\n'

def enterNoConditional(latinoToJSInstance, ctx: LatinoGrammarParser.NoConditionContext):
    latinoToJSInstance.jsCode += '} else {\n'


