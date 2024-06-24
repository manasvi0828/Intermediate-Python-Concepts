class Parent:
    value= 10

    def __init__(self, num):
        #this wont be executed because child class has its own init
        self.value= num
        print(self.value)
        print(num)

    def parentfunc1(self):
        print(f"this is a parent class method and value is {self.value}")

    def func(self):
        print("this is parent function")


class Child(Parent):
    value= 20
    # if same variable is used then preference is given to child class

    def __init__(self):
        print("inside child class constructor")

    def childfunc1(self):
        print(f"this is the child class method and value is {self.value}")

    def func(self):
        print("this is child function")


obj1 = Child()
obj1.childfunc1()
obj1.parentfunc1()
obj1.func()