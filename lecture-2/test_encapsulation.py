class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    # Define age como una propiedad de solo lectura (decorador property)
    @property
    def age(self): # Método getter para obtener el valor del atríbuto
        return self.__age

    # Con el setter se puede tener control de qué valores
    # son válidos para la propiedad
    @age.setter
    def age(self,age):
        if age>=0:
            self.__age=age

    def sayHI(self):
        print(self.__build_string())

    # Helper method
    def __build_string(self):
         return f'Hi I\'m {self.__name} and I\'m {self.__age} years old'



p0=Person("Gerardo",44)
p0.age=-89
p0.sayHI()
#print(p0.__build_string())







