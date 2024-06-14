from grammar.gen.LatinoGrammarParser import LatinoGrammarParser


def enterSwitch(latinoToJSInstance, ctx: LatinoGrammarParser.SwitchBlockContext):
    exp = ctx.exp().getText()
    init_switch = f'switch {exp}' if exp[0] == '(' and exp[-1] == ')' else f'switch ({exp})'
    latinoToJSInstance.jsCode += init_switch + '{\n'

def exitSwitch(latinoToJSInstance, ctx: LatinoGrammarParser.SwitchBlockContext):
    latinoToJSInstance.jsCode += '}\n'

def enterSwitchCases(latinoToJSInstance, ctx: LatinoGrammarParser.SwitchCasesDefContext):
    init_case = ''
    if ctx.parentCtx.getRuleIndex() == LatinoGrammarParser.RULE_switchCasesDef:
        init_case += 'break;\n'
    if len(ctx.CASE())>0:
        for i in range(len(ctx.CASE())):
            init_case += f'case {ctx.exp(i).getText()}:\n'
    elif ctx.DEF_CASE() != None:
        init_case += f'default:\n'
    latinoToJSInstance.jsCode += init_case

def exitSwitchCases(latinoToJSInstance, ctx: LatinoGrammarParser.SwitchCasesDefContext):
    if ctx.switchCasesDef() is None:
        latinoToJSInstance.jsCode += 'break;\n'

