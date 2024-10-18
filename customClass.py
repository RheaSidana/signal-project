class Rectangle: 
    def __init__(self, length: int, width: int): 
        self.length = length 
        self.width = width

    def __iter__(self):
        yield {'length': self.length} 
        yield {'width': self.width}


rectangles = [Rectangle(50, 10), Rectangle(50, 20), Rectangle(50, 30)]

for rectangle in rectangles:
    print("Rectangle: ")
    for rectangle_dimension in rectangle:
        print(rectangle_dimension)
    print("\n")

