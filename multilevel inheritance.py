class Grandparent:
    def __init__(self):
        print("inside grandparent class")

class Parent1(Grandparent):
    def __init__(self):
        print("inside parent 1 contructor")
        super().__init__()


class Parent2():
    def __init__(self):
        print("inside parent 2 constructor")
        super().__init__()


class Child(Parent2, Parent1):
    def __init__(self):
        print("inside child class constructor")
        super().__init__()


print(Child.__mro__)
print(Child.mro())