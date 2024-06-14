def enterListDefRule(self, ctx):
    self.jsCode += '['
    elements = ctx.optAssigExpConcatWithTrail().getText().split(',')
    for i in range(len(elements)):
        self.jsCode += '?~exp, '
    self.jsCode = self.jsCode[:-2]
    self.jsCode += ']'

