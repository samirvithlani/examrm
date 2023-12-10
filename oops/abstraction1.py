class Shape:
    def getArea(self):
        pass


class Rectangle(Shape):
    
    #constructor
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth    
     
    def getArea(self):
        return self.length * self.breadth



r = Rectangle(10, 20)

print("area of rectangle",r.getArea())        