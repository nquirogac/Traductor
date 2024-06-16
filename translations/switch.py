from grammar.gen.LatinoGrammarParser import LatinoGrammarParser


def enterSwitch(latinoToJSInstance, ctx: LatinoGrammarParser.SwitchBlockContext):
    exp = ctx.exp().getText()
    init_switch = f'switch '+'?~exp' if exp[0] == '(' and exp[-1] == ')' else f'switch ('+'?~exp'+')'
    latinoToJSInstance.jsCode += init_switch + '{\n'
    latinoToJSInstance.indentationStack.append(1)
def exitSwitch(latinoToJSInstance, ctx: LatinoGrammarParser.SwitchBlockContext):
    latinoToJSInstance.indentationStack.pop()
    latinoToJSInstance.jsCode += '}\n'

def enterSwitchCases(latinoToJSInstance, ctx: LatinoGrammarParser.SwitchCasesDefContext):
    init_case = ''
    if ctx.parentCtx.getRuleIndex() == LatinoGrammarParser.RULE_switchCasesDef:
        init_case += '    '*len(latinoToJSInstance.indentationStack)+'break;\n'
        latinoToJSInstance.indentationStack.pop()
    if len(ctx.CASE())>0:
        for i in range(len(ctx.CASE())):
            init_case += '    '*len(latinoToJSInstance.indentationStack)+ f'case {ctx.exp(i).getText()}:\n'
    elif ctx.DEF_CASE() != None:
        init_case += '    '*len(latinoToJSInstance.indentationStack)+f'default:\n'
    latinoToJSInstance.jsCode += init_case
    latinoToJSInstance.indentationStack.append(1)

def exitSwitchCases(latinoToJSInstance, ctx: LatinoGrammarParser.SwitchCasesDefContext):
    if len(ctx.switchCasesDef())==0:
        latinoToJSInstance.jsCode += '    '*len(latinoToJSInstance.indentationStack)+'break;\n'
        latinoToJSInstance.indentationStack.pop()
