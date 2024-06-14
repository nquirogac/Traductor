
def enterAssignationSentence(LatinoToJSInstance, ctx):
    variable = ctx.assignableID().getText()
    is_assig = bool(ctx.assig().ASSIGN())
    
    if is_assig and variable not in LatinoToJSInstance.symbolArray:
        LatinoToJSInstance.symbolArray.append(variable)
        LatinoToJSInstance.jsCode += 'let '

    if variable:
        LatinoToJSInstance.jsCode += variable

def enterAssignationRule(LatinoToJSInstance, ctx):
    variables = [i.getText() for i in ctx.assignableID()]
    operator = ctx.ASSIGN().getText() if ctx.ASSIGN() else ctx.ASSIGN_OP().getText()

    assignable_expressions = ctx.assignableExp()

    for i in range(len(variables)+1):
        if i > 0:
            LatinoToJSInstance.jsCode += ', ' + variables[i-1]
            #print(LatinoToJSInstance.jsCode)
        
            if variables[i-1] not in LatinoToJSInstance.symbolArray:
                LatinoToJSInstance.symbolArray.append(variables[i-1])

        if len(assignable_expressions) > i:
            LatinoToJSInstance.jsCode += f' {operator} ?~exp'
            #print(LatinoToJSInstance.jsCode)

    LatinoToJSInstance.jsCode += ';'
    #print(LatinoToJSInstance.jsCode)
