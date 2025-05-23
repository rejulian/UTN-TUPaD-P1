from math import pi

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

def solicitar_nombre():
    nombre = input("Ingrese su nombre:")
    return nombre

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

saludar_usuario(solicitar_nombre())

def solicitar_apellido():
    apellido = input("Ingrese su apellido:")
    return apellido

def solicitar_edad():
    edad = int(input("Ingrese su edad:"))
    return edad

def solicitar_residencia():
    residencia = input("Ingrese su residencia:")
    return residencia

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

informacion_personal(solicitar_nombre(), solicitar_apellido(), solicitar_edad(), solicitar_residencia())

def solicitar_radio():
    radio = int(input("Ingrese el radio:"))
    return radio

def calcular_area_circulo(radio):
    area = pi * radio**2
    print(f"El area es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    print(f"El perimetro es: {perimetro}")

def mostrar_informacion_circulo(radio):
    calcular_area_circulo(radio)
    calcular_perimetro_circulo(radio)

mostrar_informacion_circulo(solicitar_radio())

def solicitar_segundos():
    segundos = int(input("Ingrese cantidad de segundos:"))
    return segundos

def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"Los segundos ({segundos}) en horas son: {horas}")

solicitar_segundos(solicitar_segundos())

def solicitar_numero():
    numero = int(input("Ingrese un numero:"))
    return numero

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero*i)

tabla_multiplicar(solicitar_numero())

def solicitar_peso_en_kg():
    peso = float(input("Ingrese su peso en kg: "))
    return peso

def solicitar_altura_en_metros():
    altura = float(input("Ingrese su altura en metros: "))
    return altura

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(imc)

calcular_imc(solicitar_peso_en_kg(), solicitar_altura_en_metros())

def solicitar_grados_en_celsius():
    grados = float(input("Ingrese grados en celsius: "))
    return grados

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"Los grados celsius ({celsius}) en fahrenheit son: {fahrenheit}")

celsius_a_fahrenheit(solicitar_grados_en_celsius())

def solicitar_notas():
    nota = int(input("Ingrese la su nota:"))
    return nota

def calcular_promedio(a,b,c):
    promedio = (a+b+c) / 3
    print(f"El promedio es {promedio}")

calcular_promedio(solicitar_notas(),solicitar_notas(),solicitar_notas())