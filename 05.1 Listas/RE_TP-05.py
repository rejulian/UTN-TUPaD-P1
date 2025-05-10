# Ejercicio 1
lista_multiplos_cuatro = list(range(1,100,4))
print("Lista de múltiplos de 4:", lista_multiplos_cuatro)

# Ejercicio 2
lista_cinco_elementos = [1,2,3,4,5]
print("Penúltimo elemento:", lista_cinco_elementos[3])

# Ejercicio 3
lista_vacia = []
lista_vacia.append(1)
lista_vacia.append(2)
lista_vacia.append(3)
print("Lista vacía:", lista_vacia)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[3]="oso"
print("Lista de animales:", animales)

# Ejercicio 5
# El programa elimina el mayor valor de la lista

# Ejercicio 6
numeros_diez_al_treinta = list(range(10,31, 5))
print(numeros_diez_al_treinta[0:2])

# Ejercicio 7
autos=["sedan","polo","suran","gol"]
autos[1:3]=["fiesta","focus"]
print(autos)

# Ejercicio 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print("Lista de dobles:", dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Lista de compras:", compras)

# Ejercicio 10
lista_anidada=[15,True,[25.5,57.9,30.6], False]
print("Lista anidada:", lista_anidada)