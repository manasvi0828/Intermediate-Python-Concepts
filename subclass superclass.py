class Parent:
    value= 10
    def parentfunc1(self):
        print(f"this is a parent class method and value is {self.value}")

    def func(self):
        print("this is parent function")


class Child(Parent):
    value= 20
    # if same variable is used then preference is given to child class

    def childfunc1(self):
        print(f"this is the child class method and value is {self.value}")

    def func(self):
        print("this is child function")


obj1 = Child()

print(issubclass(Child, Parent))
print(issubclass(Parent,Child))
print(isinstance(obj1, Parent))
print(isinstance(obj1, Child))