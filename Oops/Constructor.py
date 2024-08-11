class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Hello this is constructor")
        print("memory of self", id(self))


    def add(self):
        print("Hello this is add method")
        return self.a+self.b
obj = Calc(a:4,b:5)

print("memory of obj", id(obj))

