import math

class Shape(object):
    def __init__(self, l, w):
        self.length = 1
        self.width = w

class Diamond(Shape):
    def __init__(self, l):
        Shape.__init__(self, l, l)

    def draw(self):        
        for i in range(self.width):
            print " " * (self.width - i) + "*" * (i) + "*" * (i - 1)

        for i in range(self.width):
            print " " * (i) + "*" * (self.width - i)  + "*" * (self.width - i - 1)
                
class Circle(Shape):
    def __init__(self, l):
        Shape.__init__(self, l, l)

    def draw(self):
        if (self.width == 2):
            for i in range(self.width):
                print "**"
        elif ((self.width % 2) == 0):
            for i in range(self.width):
                if (i == 0 or i == (self.width - 1)):
                    print (" ") + ("*" * (abs(self.width - 2)))
                else:
                    print ("*" * self.width)
        else:
            for i in range(self.width):
                if (i == 0 or i == (self.width - 1)):
                    print (" ") + ("*" * (abs(self.width - 2)))
                else:
                    print ("*" * self.width)


#d1 = Diamond(5)
#d1.draw()
c1 = Circle(1)
c2 = Circle(2)
c3 = Circle(3)
c4 = Circle(4)
c5 = Circle(5)
c6 = Circle(6)
c7 = Circle(7)
c8 = Circle(8)

c1.draw()
print
c2.draw()
print
c3.draw()
print
c4.draw()
print
c5.draw()
print
c6.draw()
print
c7.draw()
print
c8.draw()

