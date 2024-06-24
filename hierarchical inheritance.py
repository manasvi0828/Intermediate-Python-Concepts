# we have only one parent class and multiple child class
class Parent:
    def __init__(self):
        print("inside parent class constructor")

class Child1(Parent):
    def __init__(self):
        print("inside child 1 class constructor")
        super().__init__()

class Child2(Parent):
    def __init__(self):
        print("inside child 2 class constructor")
        super().__init__()

print("----------- Creating child1 object----------")
obj1= Child1()
print("----------- Creating child2 object----------")
obj2= Child2()

print(Child1.mro())
print(Child1.__mro__)
print(Child2.mro())
print(Child2.__mro__)

