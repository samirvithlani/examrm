#2 type of polymorphism
#1compile time polymorphism : method overloading
#2run time polymorphism : method overriding

#method overloading : same name of function but different no of arguments in same class is called method overloading


class Test:
    
    
    def add(self, a, b, c):
        print("Addition is", a+b+c)
    
    def add(self, a, b):
        print("Addition is", a+b)
        



t = Test()
t.add(10, 20,30)            