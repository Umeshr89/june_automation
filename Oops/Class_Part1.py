class Calc:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

obj = Calc(a: 4, b: 5):

print(obj.add)
