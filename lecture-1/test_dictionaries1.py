# Crea diccionario con información de un perro
myDog={   
    "name": "Firulais", #name: clave, llave, atributo
    "sex": "male",
    "age": 4,   
}

# Imprime el nombre
print(myDog["name"])


# Modifica el nombre y lo imprime
newName=input('Ingrese el nombre del perro:')
myDog["name"]=newName
print(myDog["name"])

# Crea nuevo elemento en el diccionario
myDog["color"]="yellow"
print(myDog)

for item in myDog:
    print(f'{item}: {myDog[item]}')





