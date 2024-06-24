class Parent:
    value= 10

    def __init__(self, num):
        self.value= num
        print(f"this is parent class constructor {self.value}")
        print(num)
        print("in parent class the value of parent", Parent.value)

    def parentfunc1(self):
        print(f"this is a parent class method and value is {self.value}")

    def func(self):
        print("this is parent function")


class Child(Parent):
    value= 20
    # if same variable is used then preference is given to child class

    def __init__(self):
        print("inside child class constructor")

        # we can call parent class constructor from here
        super().__init__(self.value)

    def childfunc1(self):
        print(f"this is the child class method and value is {self.value}")

    def func(self):
        print("this is child function")
        super().func()


obj1 = Child()
obj1.childfunc1()
obj1.parentfunc1()
obj1.func()

#in python the order of resolving the call to constructors and methods of inherited
# class is called MRO-> METHOD RESOLUTION ORDER