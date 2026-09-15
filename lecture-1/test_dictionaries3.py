# Crea una lista de diccionarios
dogs=[
    {
    "name": "Guardián", #name: clave, llave, atributo
    "sex": "male",
    "age": 5,
    "color": "white"  
},

{
    "name": "Maxi",
    "sex":"male",
    "age":9,
    "color":"yellow"
}
]

print(dogs[1]["color"])

dogs.append({
    "name":"Negro",
    "age":1,
    "sex":"male",
    "color":"black",
    "vaccines":["rabies","parvovirus"]
})

for item in dogs:
    #print(item["age"])
    print(item)

print(dogs[2]["vaccines"][1])