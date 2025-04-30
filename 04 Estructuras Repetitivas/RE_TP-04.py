from random import randint

# Actividad 1
def mostrar_numeros():
    for i in range(0, 101):
        print(i)
# mostrar_numeros()

# Actividad 2
def contador_digitos():
    numero = int(input("Ingrese un numero entero: "))
    contador = 0

    while numero > 0:
        contador += 1
        numero //=10

    print(contador)
# contador_digitos()

# Actividad 3
def suma_enteros():
    numero1 = int(input("1. Ingrese un numero entero: "))
    numero2 = int(input("2. Ingrese un numero entero: "))

    if(numero1 > numero2):
        print("El primer numero ingresado debe ser menor al segundo")
        return
    
    contador = 0
    inicio=numero1+1


    for i in range(inicio, numero2):
        contador+=i

    print(contador)
# suma_enteros()

# Actividad 4
def suma_secuencia():
    contador = 0
    numero = int(input("Ingrese un numero: "))

    while(numero != 0):
        contador+=numero
        numero = int(input("Ingrese un numero: "))
    
    print(contador)
# suma_secuencia()

# Actividad 5
def adivina_numero():
    numero = randint(0,9)
    contador = 1
    numero_ingresado = int(input("Ingrese un numero entre 0 y 9: "))

    while(numero_ingresado != numero):
        contador+=1
        numero_ingresado = int(input("Numero incorrecto, ingrese otro entre 0 y 9: "))

    print(f"Numero correcto! Intentos: {contador}")
# adivina_numero()

# Actividad 6
def numeros_pares():
    contador=0

    for i in range(0,101):
        if(i%2==0):
            contador+=1
    
    print(f"Hay {contador} numeros pares entre 0 y 100")
# numeros_pares()

# Actividad 7
def suma():
    contador = 0
    numero = int(input("Ingrese un numero positivo: "))
    if(numero < 0 ):
        print("El numero debe ser positivo")

    final = numero + 1

    for i in range (0,final):
        contador+=i
    
    print(f"La suma de todos los numeros enteros entre 0 y {numero} es {contador}")
# suma()

# Actividad 8
def tipos_numeros():
    pares=0
    impares=0
    negativos=0
    positivos=0

    for i in range (1,101):
        numero = int(input(f"{i}. Ingrese un numero: "))

        if(numero % 2 != 0):
            impares+=1
        else:
            pares+=1

        if(numero >= 0):
            positivos+=1
        else:
            negativos+=1
    
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")
# tipos_numeros()

# Actividad 9
def promedio():
    suma=0

    for i in range (1,101):
        numero=int(input("Ingrese un numero: "))
        suma+=numero

    print(f"El promedio es: {suma/100}")
# promedio()

# Actividad 10
def invertir():
    numero=int(input("Ingrese un numero: "))
    numero_ingresado = numero
    nuevo_numero = ''

    while(numero > 0):
        numero_string = str(numero)
        nuevo_numero =  nuevo_numero + numero_string[len(numero_string) - 1]
        numero //= 10 

    print(f"El numero {numero_ingresado} invertido es {nuevo_numero}")
invertir()