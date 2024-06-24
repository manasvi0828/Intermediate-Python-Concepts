class Parent1:

    def __init__(self):
        print("this is parent 1 constructor")

class Parent2:
     def __init__(self):
        print("this is parent 2 constructor")
        super().__init__()


class Child(Parent1,Parent2):  # whichever class is declared will be called first
    def __init__(self):
        print("inside child constructor")
        super().__init__()

obj1= Child()
print(Child.__mro__)
print(Child.mro())