
def enterAssignationSentence(self, ctx):
    variable = ctx.assignableID().getText()
    is_assig = bool(ctx.assig().ASSIGN())
    if is_assig and variable not in self.symbolArray:
        self.symbolArray.append(variable)
        self.jsCode += 'let '

    if variable:
        self.jsCode += variable

def enterAssignationRule(self, ctx):
    variables = [i.getText() for i in ctx.assignableID()]
    operator = ctx.ASSIGN().getText() if ctx.ASSIGN() else ctx.ASSIGN_OP().getText()

    assignable_expressions = ctx.assignableExp()

    if not self.infor:
        for i in range(len(variables)+1):
            if i > 0:
                self.jsCode += ', ' + variables[i-1]

                if variables[i-1] not in self.symbolArray:
                    self.symbolArray.append(variables[i-1])
            if len(assignable_expressions) > i:
                self.jsCode += f' {operator} ?~exp'

        self.jsCode += ';'

    if self.infor:
        for i in range(len(variables)+1):
            if i > 0:
                self.jsCode += ', ' + variables[i-1]

                if variables[i-1] not in self.symbolArray:
                    self.symbolArray.append(variables[i-1])
            if len(assignable_expressions) > i:
                self.jsCode += f' {operator} ?~exp'

        self.jsCode += '){\n'








def enterWhileBlockRule(self, ctx):
    exp = ctx.exp().getText()
    #print(f"la expresion del while es: {exp}")
    self.jsCode += f'while {exp}' if exp[0] == '(' and exp[-1] == ')' else f'while ({exp})'
    self.jsCode += '{\n'
    self.indentationStack.append(1)

def exitWhileBlockRule(self, ctx):
    if len(self.indentationStack) > 0:
        for i in range(len(self.indentationStack) - 1):
            self.jsCode += '    '
    self.jsCode += '}'
    self.indentationStack.pop()

def enterDoWhileBlockRule(self, ctx):
    self.jsCode += 'do {\n'
    self.indentationStack.append(1)

def exitDoWhileBlockRule(self, ctx):
    exp = ctx.exp().getText()
    if len(self.indentationStack) > 0:
        for i in range(len(self.indentationStack) - 1):
            self.jsCode += '    '
    self.jsCode += '} '
    self.jsCode += f'while {exp}' if exp[0] == '(' and exp[-1] == ')' else f'while ({exp})'
    self.indentationStack.pop()

def enterForBlockRule(self, ctx):
    is_assig = ctx.ASSIGN() != None

    variable = ctx.assignableID().getText()
    if is_assig and variable not in self.symbolArray:
        self.symbolArray.append(variable)
        self.jsCode += f'for (let {ctx.assignableID().getText()} {ctx.ASSIGN().getText()} ?~exp; ?~exp; '
    elif is_assig and variable in self.symbolArray:
        self.jsCode += f'for ({ctx.assignableID().getText()}{ctx.ASSIGN().getText()}?~exp; ?~exp; '
    elif not is_assig:
        self.jsCode += f'for ({ctx.assignableID().getText()}{ctx.ASSIGN_OP().getText()}?~exp; ?~exp; '

    self.infor = True

    #self.jsCode += '{\n'
    self.indentationStack.append(1)


def exitForBlockRule(self, ctx):
    if len(self.indentationStack) > 0:
        for i in range(len(self.indentationStack) - 1):
            self.jsCode += '    '
    self.jsCode += '}'
    self.indentationStack.pop()

def enterForRangeBlockRule(self, ctx):
    inicio = False
    fin = False
    salto = False

    if len(ctx.exp()) == 1:
        inicio = True
    elif len(ctx.exp()) == 2:
        inicio = True
        fin = True
    elif len(ctx.exp()) == 3:
        inicio = True
        fin = True
        salto = True

    if not self.rangeCreated:
        self.jsCode += 'function range(start, end, step) {\n'
        self.jsCode += '    if (end === undefined) {\n'
        self.jsCode += '        end = start;\n'
        self.jsCode += '        start = 0;\n'
        self.jsCode += '    }\n'
        self.jsCode += '    if (step === undefined) {\n'
        self.jsCode += '        step = 1;\n'
        self.jsCode += '    }\n'
        self.jsCode += '    let result = [];\n'
        self.jsCode += '    if (step > 0) {\n'
        self.jsCode += '        for (let i = start; i < end; i += step) {\n'
        self.jsCode += '            result.push(i);\n'
        self.jsCode += '        }\n'
        self.jsCode += '    } else {\n'
        self.jsCode += '        for (let i = start; i > end; i += step) {\n'
        self.jsCode += '            result.push(i);\n'
        self.jsCode += '        }\n'
        self.jsCode += '    }\n'
        self.jsCode += '    return result;\n'
        self.jsCode += '}\n'

        self.rangeCreated = True

    if inicio and fin and salto:
        #self.jsCode += f'hay 3 parametros, inicio: ?~exp, fin: ?~exp, salto: ?~exp'
        self.jsCode += f'for (let i of range(?~exp, ?~exp, ?~exp))'
        self.jsCode += '{\n'
    elif inicio and fin:
        #elf.jsCode += f'hay 2 parametros, inicio: ?~exp, fin: ?~exp'
        self.jsCode += f'for (let i of range(?~exp, ?~exp))'
        self.jsCode += '{\n'
    elif inicio:
        #elf.jsCode += f'hay 1 parametro, inicio: ?~exp'
        self.jsCode += f'for (let i of range(?~exp))'
        self.jsCode += '{\n'

    self.indentationStack.append(1)

def exitForRangeBlockRule(self, ctx):
    if len(self.indentationStack) > 0:
        for i in range(len(self.indentationStack) - 1):
            self.jsCode += '    '
    self.jsCode += '}'
    self.indentationStack.pop()