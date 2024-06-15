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
