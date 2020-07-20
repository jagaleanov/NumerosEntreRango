# Escribir un programa que sume los números comprendidos 
# entre un rango suministrado por el usuario

a = int(input("inicio del rango: "))
b = int(input("fin del rango: "))

y = 0

for x in range(a,b+1):
    y += x

print(y)

