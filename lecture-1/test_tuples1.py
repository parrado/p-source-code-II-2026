# Crea tupla con 3 nombres de fruta
thisTuple1 = ("apple", "banana", "cherry")
thisTuple2=("carro",3.141592654,[1,2,3,4])

# Imprime el primer elemento de la tupla
print(thisTuple1[0])

# Recorre la tupla con ciclo for
# e imprime cada uno de los elementos
for item in thisTuple1:
    print(item)

for i in range(len(thisTuple1)):
    print(thisTuple1[i])


thisTuple1[2]='Strawberry'