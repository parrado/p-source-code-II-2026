from math import pi

class Circulo:
    def __init__(self,radius,centerX,centerY):
        self.radius=radius
        self.centerX=centerX
        self.centerY=centerY

    def area(self):
        return pi*self.radius**2

    def perimetro(self):
        return 2*pi*self.radius

    def showInfo(self):
        print(f'My radius is {self.radius} and my center coordinates are ({self.centerX},{self.centerY}) ')
        