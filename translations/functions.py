def enterOpBuiltInTipoRule(self, ctx):

    operation = ctx.OP_BUILTIN_FUNCS_ARG().getText()
    if operation == 'anumero':
        operation = 'parseFloat(?~exp)'
    elif operation == 'acadena':
        operation = '(?~exp).toString()'
    elif operation == 'alogico':
        operation = 'Boolean(?~exp)'
    elif operation == 'tipo':
        operation = 'typeof(?~exp)'
    
    if '?~opBT' in self.jsCode:
        self.jsCode = self.jsCode.replace('?~opBT', operation)
    else:
        self.jsCode += f'{operation}'


def enterBuiltInFuncSentenceRule(self,ctx):
    if ctx.BUILTIN_FUNC_SINGLE_ARG():
        self.jsCode += 'console.log(?~exp)'
    elif ctx.BUILTIN_FUNC_NO_ARG():
        self.jsCode += 'clear()'
    elif ctx.BUILTIN_FUNC_MULTI_ARG():
        self.jsCode += 'console.log(?~PrintArgs)'

def enterFunctionBlockRule(self, ctx):
    number_ids = len([i.getText() for i in ctx.ID()])
    self.jsCode += 'function ' + ctx.ID(0).getText() + '('
    self.indentationStack.append(1)
    if number_ids == 1:
        self.jsCode += '){ \n'
    else:
        for i in range(1, number_ids):
            self.jsCode += ctx.ID(i).getText() + ', '
        self.jsCode = self.jsCode[:-2]
        self.jsCode += '){ \n'

def enterFunctionReturnRule(self, ctx):
    if '?~return' in self.jsCode:
        self.jsCode = self.jsCode.replace('?~return', f'return ?~exp')
    else:
        self.jsCode += 'return ?~exp'

def exitFunctionBlockRule(self, ctx):
    if len(self.indentationStack)>0:
        for i in range(len(self.indentationStack)-1):
            self.jsCode += '    '
    self.jsCode += '}'
    self.indentationStack.pop()


def enterFunctionCallRule(self, ctx):
    replacement_string = ''

    if '?~funCall' in self.jsCode:
        if ctx.optionalAssignableExpConcat().getText() == '':
            self.jsCode = self.jsCode.replace('?~funCall', replacement_string)
        else:
            n_expressions = len(ctx.optionalAssignableExpConcat().assignableExp())
            for i in range(n_expressions):
                replacement_string += '?~exp, ' if i < n_expressions-1 else '?~exp'
            self.jsCode = self.jsCode.replace('?~funCall', f'{replacement_string}')
    elif '?~nestedFunCall' in self.jsCode:
        n_expressions = len(ctx.optionalAssignableExpConcat().assignableExp())
        for i in range(n_expressions):
            replacement_string += '?~exp, ' if i < n_expressions - 1 else '?~exp'
        self.jsCode = self.jsCode.replace('?~nestedFunCall', replacement_string)
    else:    
        self.jsCode += f'({replacement_string})'


def enterAnonymousFuncDefRule(self, ctx):
    expression = 'function ('
    ids = [i.getText() for i in ctx.ID()]
    for i in range(len(ids)):
        expression += f'{ids[i]}, ' if i < len(ids) - 1 else f'{ids[i]}'
    expression += ') { \n'
    n_sentences = len(ctx.sentence())

    for i in range(n_sentences):
        expression += '?~sentence'
    expression += '\n}'
    self.jsCode = self.jsCode.replace('?~anonFunc', expression)
    

def defineArgsPrint(self, ctx):
    args = ctx.getText()
    
    if len(args) <= 4:
        if '%i' in args or '%d' in args:
            self.jsCode = self.jsCode.replace('?~PrintArgs', 'parseInt(?~skip?~exp)')
        elif '%f' in args:
            self.jsCode = self.jsCode.replace('?~PrintArgs', 'parseFloat(?~skip?~exp)')
        elif '%o' in args or '%x' in args:
            self.jsCode = self.jsCode.replace('?~PrintArgs', 'parseInt(?~skip?~exp, ' + ('8' if '%o' in args else '16') + ')')
        elif '%%' in args:
            self.jsCode = self.jsCode.replace('?~PrintArgs', '?~skip?~exp /* no hay una traduccion directa */ ')
        elif '%c' in args:
            self.jsCode = self.jsCode.replace('?~PrintArgs', 'String.fromCharCode(?~skip?~exp)')
        elif '%s' in args:
            self.jsCode = self.jsCode.replace('?~PrintArgs', '(?~skip?~exp).toString()')
        elif '%e' in args:
            self.jsCode = self.jsCode.replace('?~PrintArgs', '/* Error: Expected number \n the translate will be like this: \n (?~skip?~exp).toExponential()\n */')
    else:
        num_arg = args.count('%')
        expression = 'String.fromCharCode(?~skip?~exp'
        
        for i in range(num_arg-1):
            expression += ', ?~exp'
        expression += ')'
        self.jsCode = self.jsCode.replace('?~PrintArgs', expression)
    