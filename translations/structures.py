def enterListDefRule(self, ctx):
    self.jsCode += '['
    elements = [i.getText() for i in ctx.optAssigExpConcatWithTrail().assignableExp()]

    for i in range(len(elements)):
        if elements[i] != '':
            self.jsCode += '?~exp, ' if i < len(elements)-1 else '?~exp'
    self.jsCode += ']'

