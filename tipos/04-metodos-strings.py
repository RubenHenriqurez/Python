animal = "    chanCHito feliz   "
print(animal.upper())#metodos, transforma todo en mayusculas
print(animal.lower())# pasa todo a minusculas
print(animal.strip().capitalize())#primera letra en minusculas todo lo demás en mayusculas--se combinan 2 metodos 
print(animal.title())#toma cada palabra de cada inicio y la pasa a mayusculas, parecido al anterior
print(animal.strip())#se usa para los espacios
print(animal.lstrip())#quita espacios ala derecha
print(animal.rstrip())#quita espacios ala izquierda
print(animal.find("cH"))#va a buscar una cadena de caracteres y busca el indice, un número positivo es que lo encontro y un numeros negativo -1 significa que no se encontro
print(animal.replace("nCH", "j"))# se usa para remplazar texto, necesita 2 argumentos si o si 
print("nCH" in animal)#find devuelve indice, in devuelve un boolean 
print("nCH" not in animal)# esta es para ver si no esta lo eatamos negando