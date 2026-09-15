from cmath import sqrt

def myRoots(p: list):
    a=(-p[1]+sqrt(p[1]**2-4*p[0]*p[2]))/(2*p[0])
    b=(-p[1]-sqrt(p[1]**2-4*p[0]*p[2]))/(2*p[0])
    
    return a,b

p=[]

p.append(float(input('Ingrese coeficiente a: ')))
p.append(float(input('Ingrese coeficiente b: ')))
p.append(float(input('Ingrese coeficiente c: ')))
(r1,r2)=myRoots(p)
print(f'Raiz 1: {r1},Raiz 2: {r2}')
r=myRoots(p)
print(f'Raiz 1: {r[0]}\nRaiz 2: {r[1]}')



 