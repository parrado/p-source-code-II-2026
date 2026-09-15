# Crea conjunto 
thisSet1 = {"apple", "banana", "cherry"}

# Imprime el conjunto completo
print(thisSet1)

# Recorre el conjunto con ciclo for
# e imprime cada elemento
for item in thisSet1:
    print(item)

# Throw error, sets are not subscriptabls
# for i in range(len(thisSet1)):
#     print(thisSet1[i])

# Pregunta si el elemento "pineapple" está en el conjunto
if "pineapple" in thisSet1:
    print("There's pineapple")

# Pregunta si el elemento "apple" está en el conjunto
if "apple" in thisSet1:
    print("There's apple")
