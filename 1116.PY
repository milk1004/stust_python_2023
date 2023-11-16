class MyShape:
    def __init__(self, square_side=None, length=None, width=None, radius=None):
        self.square_side = square_side
        self.length = length
        self.width = width
        self.radius = radius

    def getSquareArea(self):
        if self.square_side is not None:
            return self.square_side ** 2
        else:
            return "請輸入邊長"

    def getRectangleArea(self):
        if self.length is not None and self.width is not None:
            return self.length * self.width
        else:
            return "請輸入長寬"

    def getCircleArea(self):
        if self.radius is not None:
            return 3.14 * (self.radius ** 2)  
        else:
            return "請輸入半徑"



shape1 = MyShape(square_side=10)
print("Square Area:", shape1.getSquareArea())

shape2 = MyShape(length=9, width=7)
print("Rectangle Area:", shape2.getRectangleArea())

shape3 = MyShape(radius=6)
print("Circle Area:", shape3.getCircleArea())
