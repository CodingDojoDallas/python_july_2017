class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        if type(args) is tuple:
            for arg in args:
                self.result = self.result + arg

        return self

    def subtract(self, *args):
        if type(args) is tuple:
            for arg in args:
                self.result = self.result - arg
        return self

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result
