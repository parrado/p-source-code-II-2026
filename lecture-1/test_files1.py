from json import dumps

# Abre archivo
file=open('data/my_data.txt','a')
#file=open('C:/Users/samae/Documents/docencia-uq/II-2025/Programming/slides/lecture-1-sources/data/my_data.txt','a')
# Solicita datos al usuario
name=input('Ingrese su nombre: ')
id=int(input('Ingrese su cédula: '))

data={"name":name,"id":id}

# Escribe el texto en el archivo
file.write(dumps(data)+"\n")

# Cierra el archivo
file.close()

