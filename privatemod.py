class ABC:
    def __init__(self):
        self._protected_attribute= 10

    def _protected_function(self):
        pass

object1= ABC()
print(object1._protected_attribute)
