class Rectangles:
    def __init__(self, height, width):
        print(height, width)
        self.height= height
        self.width= width

rectangle11= Rectangles(5,5)
rectangle11.frequency= 45 #instance attribute
print(rectangle11.frequency)

rectangle12= Rectangles(9,5)
rectangle13= Rectangles(5,9)
