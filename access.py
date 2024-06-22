#public modifier

class ABC:
    def __init__(self):
        self.public_attribute= None

    def public_function(self):
        pass

object1= ABC()
object1.public_attribute
object1.public_function()