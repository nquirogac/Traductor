def enterListDefRule(self, ctx):
    string_replacement = '['
    elements = [i.getText() for i in ctx.optAssigExpConcatWithTrail().assignableExp()]

    for i in range(len(elements)):
        if elements[i] != '':
            string_replacement += '?~exp, ' if i < len(elements)-1 else '?~exp'

    string_replacement += ']'

    if '?~listDef' in self.jsCode:
        self.jsCode = self.jsCode.replace('?~listDef', string_replacement)
    else:
        self.jsCode += string_replacement

def enterDictDefRule(self, ctx):
    string_replacement = '{\n'
    self.indentationStack.append(self.indentationStack[-1]+1)

    for i in range(len(ctx.exp())):
        string_replacement += (self.indentationStack[-1])*'\t' + '?~exp : ?~exp'
        string_replacement += ',\n' if i < len(ctx.exp())-1 else '\n'

    # At this point the extra indentation hasn't been removed, thus we use -1
    string_replacement += (self.indentationStack[-1]-1)*'\t' + '}'

    self.jsCode = self.jsCode.replace('?~dictDef', string_replacement)

def exitDictDefRule(self, ctx):
    self.indentationStack.pop()
