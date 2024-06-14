def enterOpBuiltInTipoRule(self, ctx):
    #print('OpBuiltInTipo')
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
        self.jsCode +=  f'{operation}'
    #print(3, self.jsCode)


def enterBuiltInFuncSentenceRule(self,ctx):
    if ctx.BUILTIN_FUNC_SINGLE_ARG():
        self.jsCode += 'console.log(?~exp)'
    elif ctx.BUILTIN_FUNC_NO_ARG():
        self.jsCode += 'clear()'
    elif ctx.BUILTIN_FUNC_MULTI_ARG():
        self.jsCode += 'console.log(?~PrintArgs)'

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
    