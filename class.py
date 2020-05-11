class Base1:
    def __init__(self):
        self.str1="Hello"
        print("Base1")
class Base2:
    def __init__(self):
        self.str2="Python"
        print("Base2")
class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    def printString(self):
        print(self.str1,self.str2)
ob=Derived()
ob.printString()