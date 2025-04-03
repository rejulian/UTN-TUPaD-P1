from random import randint
from statistics import multimode, median, mean

# Ejercicio 1
edad = int(input("Ingrese su edad: "))

if(edad > 18):
    print("Es mayor de edad")

# Ejercicio 2
nota = int(input("Ingrese su nota: "))
if(nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
numero = int(input("Ingrese un numero: "))
es_par = numero % 2 == 0

while(not es_par):
    print(f"El numero {numero} no es par")
    numero = int(input("Por favor, ingrese un numero par: "))
    es_par = numero % 2 == 0

print("Ha ingresado un número par")

# Ejercicio 4
edad = int(input("Ingrese su edad: "))

if(edad < 12):
    print("Pertenece a la categoria: Niño")
elif(edad >= 12 and edad < 18):
    print("Pertenece a la categoria: Adolescente")
elif(edad >= 18 and edad < 30):
    print("Pertenece a la categoria: Adulto joven")
else:
    print("Pertenece a la categoria: Adulto")

# Ejercicio 5
password = input("Ingrese una contraseña: ")
password_len = len(password)

if(password_len >= 8 and password_len <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
numeros_aleatorios = [randint(1,100) for i in range(50)]
moda = multimode(numeros_aleatorios)[0]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

if(media > mediana and mediana > moda):
    print("Sesgo positivo")
elif(media < mediana and mediana < moda):
    print("Sesgo negativo")
elif(media == mediana == moda):
    print("Sin sesgo")

# Ejercicio 7
frase = input("Ingrese una frase: ")
ultimo_caracter = frase[len(frase) - 1].lower()

if(ultimo_caracter == 'a' or ultimo_caracter == 'e' or ultimo_caracter == 'i' or ultimo_caracter == 'o' or ultimo_caracter == 'u'):
    print(f'{frase}!')
else:
    print(frase)

# Ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opcion: 1, 2 o 3. \n 1.Nombre en mayusculas. Ej: PEDRO. \n 2. Nombre en minusculas. Ej: pedro. \n 3. Nombre con la primera letra en mayuscula. Ej: Pedro."))

match opcion:
    case 1:
        print(nombre.upper())
    case 2:
        print(nombre.lower())
    case 3: 
        print(nombre.title())
    case _:
        print("Opción no válida")

# Ejercicio 9
magnitud = float(input("Ingrese magnitud de terremoto: "))

if(magnitud < 3):
    print("Muy Leve")
elif(magnitud >= 3 and magnitud < 4):
    print("Leve")
elif(magnitud >= 4 and magnitud < 5):
    print("Moderado")
elif(magnitud >= 5 and magnitud < 6):
    print("Fuerte")
elif(magnitud >= 6 and magnitud < 7):
    print("Muy fuerte")
else:
    print("Extremo")

# Ejercicio 10
hemisferio = input("Ingrese su hemisferio (N/S): ").strip().upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"La estación correspondiente es: {estacion}")