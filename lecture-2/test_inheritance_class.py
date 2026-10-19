from math import pi

# Parent class Shape
# Abstract class
class Shape:
    def __init__(self,centerX,centerY):
        self._centerX=centerX
        self._centerY=centerY

    # Abstract method
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self,centerX,centerY,base,height):
         super().__init__(centerX,centerY)
         self.__base=base
         self.__height=height

    def area(self):
        return self.__base*self.__height/2

    def showInfo(self):
        print(f'I\'m a triangle with center coordinates ({self._centerX},{self._centerY})')


class Circle(Shape):
    def __init__(self,centerX,centerY,radius):
         super().__init__(centerX,centerY)
         self.__radius=radius         

    def area(self):
        return pi*self.__radius**2

    def showInfo(self):
        print(f'I\'m a circle with center coordinates ({self._centerX},{self._centerY})')


t0=Triangle(0,0,2,1)
print(t0.area())
t0.showInfo()

c0=Circle(-1,-1,2)
print(c0.area())
c0.showInfo()
        



