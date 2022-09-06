cantantes = ["Limp Bizkit", "Korn", "Iron Maiden", "BMTH"]
numeros = [3, 5, 1, 6, 2, 4]

# Ordenar

numeros.sort() #Ordena la lista
print(numeros)

# Añadir elementos

cantantes.append("Metallica") # Agrega el elemento al final de la lista
cantantes.insert(5, "Amon Amarth") # Agrega el elemento en el indice que indicamos "si existe uno en el lugar lo reemplaza"

print(cantantes)

# Eliminar elementos

cantantes.pop(1) #Elimnina el elemento ubicado en el índice que indicamos
cantantes.remove("BMTH") # Elimina el elemento que describimos

print(cantantes)

# Dar vuelta una lista

numeros.reverse()
print(numeros) # Invierte la lista

# Buscar dentro de la lista

print("Metallica" in cantantes) # De esta manera buscamos elementos en ls listas, devuelve True o False

# Contar Elementos

print(len(cantantes)) # Cuenta la cantidad de elmentos que tiene una lista

# Cuantas veces aparece un elemento 

print(numeros.count(5)) # Cuenta la cantidad de veces que se encuentra un elemento en una lista, en este caso cuantas veces aparece el 5 en la lista numeros

# Conseguir indice

print(cantantes.index("Limp Bizkit")) # Muestra en que índice se encuentra el elemento

# Unir listas

cantantes.extend(numeros) # de esta forma unimos las listas

print(cantantes)





