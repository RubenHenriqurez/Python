Buscar = 10


for numero in range(5):#Iterable, cualquier cosa que sea iterable, listas, tuplas todas son iterables, strings
    print(numero)#crea una secuencia de numeros que devuelve un listado, 0,1,2,3,4. 
    if numero == Buscar:
        print("Encontrado", Buscar)
        break# se usa para detener el ciclo

else:
    print(" no encontre el número buscado")
#Itera una lista de elememtos, nombre y apellido=nombre completo, otro uso para buscar elementos y operaciones amtematicas

for char in "Ultimte python":
    print(char)

