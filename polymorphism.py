class Animals:
    def speaks(self):
        pass


class Dog(Animals):
    def speaks(self):
        print("barks")


class Cat(Animals):
    def speaks(self):
        print("meow")


dog= Dog()
cat= Cat()

dog.speaks()
cat.speaks()