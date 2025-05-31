# Ejercicio 1
def factorial_recursivo(numero):
    if numero == 1:
        return 1
    else :
        return numero * factorial_recursivo(numero - 1)
    
def calcular_factorial():
    numero = int(input("Ingrese un numero: "))

    for i in range(1,numero+1):
        print(f"El factorial de {i} es: {factorial_recursivo(i)}")

calcular_factorial()

# Ejercicio 2
def serie_fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    
    return serie_fibonacci(posicion-1) + serie_fibonacci(posicion -2)

def mostrar_serie_fibonacci():
    numero = int(input("Ingrese un numero: "))
    for i in range(1, numero+1):
        print(f"El valor de la secuencia en la posicion {i} es {serie_fibonacci(i)}")

mostrar_serie_fibonacci()

# Ejercicio 3
def potencia(base, exponente) :
  if exponente == 0 :
    return 1
  else :
    return base * potencia(base, exponente - 1);

print(potencia(2,3))

# Ejercicio 4
def convertir_decimal_a_binario(numeroDecimal):
    if(numeroDecimal == 0):
        return '0'
    elif (numeroDecimal == 1):
        return '1'
    else:
        return convertir_decimal_a_binario(numeroDecimal // 2) + str(numeroDecimal % 2)

print(convertir_decimal_a_binario(10))

# Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print(es_palindromo('oso'))

# Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)
print(suma_digitos(1234))

# Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)
print(contar_bloques(4))

# Ejercicio 8
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
print(contar_digito(1234,4))