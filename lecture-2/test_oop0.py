class Dog:
    def __init__(self,name,color,age):
        self.name=name
        self.color=color
        self.age=age
    
    def bark(self):
        print(f'Woof!! I\'m {self.name} and I\'m {self.age} years old')


dog1=Dog("Milo","Café",2.5)
dog1.bark()
dog2=Dog("Nala","Blanco con Café",2.5)
dog2.bark()
dog3=Dog("Drogo","Negro con Blanco",2.5)
dog3.bark()

print(type(dog1))
        


