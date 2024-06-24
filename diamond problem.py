# grandparent
# /          \
# Parent1    parent2
#  \           /
#    child class

class Grandparent:
    def func(self):
        print("inside grandparent func")

class Parent1(Grandparent):
    def func(self):
        print("inside parent 1 func")

class Parent2(Grandparent):
    def func(self):
        print("inside parent 2 func")

class Child(Parent1,Parent2):
    def func(self):
        print("inside child class function")


obj1= Child()
obj1.func()