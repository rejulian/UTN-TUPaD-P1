# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}

precios_frutas["Naranja"] = 1200;
precios_frutas["Manzana"] = 1500;
precios_frutas["Pera"] = 2300;

print(precios_frutas)

# Ejercicio 2
precios_frutas["Banana"] = 1330;
precios_frutas["Manzana"] = 1700;
precios_frutas["Melón"] = 2800;

print(precios_frutas)

# Ejercicio 3
frutas = list(precios_frutas.keys())
print(frutas)

# Ejercicio 4
def almacenar_contactos():
    contactos = {}

    print("Ingresa 5 contactos")
    for i in range(5):
        nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
        numero = input(f"Ingresá el número de {nombre}: ")
        contactos[nombre] = numero
    
    consulta = input("Ingresá el nombre del contacto que querés buscar: ")
    if(consulta in contactos):
        print(f"El número de {consulta} es {contactos[consulta]}")
    else:
        print(f"{consulta} no se encuentra en la agenda.")

# almacenar_contactos()

# Ejercicio 5
def contar_palabras():
    frase = input("Ingrese una frase: ")
    palabras_unicas = set()
    recuento = {}
    frase_lista = frase.split(" ")
    
    for i in range(len(frase_lista)):
        palabras_unicas.add(frase_lista[i])
        if(frase_lista[i] in recuento):
            recuento[frase_lista[i]] += 1
        else:
            recuento[frase_lista[i]] = 1

    print(f"Palabras unicas: {palabras_unicas}")
    print(f"Recuento: {recuento}")
# contar_palabras()

# Ejercicio 6
def mostrar_promedio():
    alumnos = {}

    for i in range(3):
        nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
        nota1 = int(input(f"Ingresá la primera nota de {nombre}: "))
        nota2 = int(input(f"Ingresá la segunda nota de {nombre}: "))
        nota3 = int(input(f"Ingresá la tercera nota de {nombre}: "))

        notas = (nota1, nota2, nota3)

        alumnos[nombre] = notas
    
    print("Promedios de los alumnos:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio}")

# mostrar_promedio()

# Ejercicio 8
stock_productos = {
    "manzana": 50,
    "banana": 30,
    "naranja": 20
}


print("Productos disponibles:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock} unidades")

producto = input("\nIngresá el nombre de un producto: ").lower()

if producto in stock_productos:
    print(f"El stock actual de {producto} es: {stock_productos[producto]} unidades")

    agregar = input(f"¿Querés agregar unidades a {producto}? (si/no): ").lower()
    if agregar == "si":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
else:
    print(f"{producto} no existe en el inventario.")
    agregar_nuevo = input("¿Querés agregar este nuevo producto? (sí/no): ").lower()
    if agregar_nuevo == "sí":
        unidades = int(input(f"¿Cuántas unidades tiene {producto}?: "))
        stock_productos[producto] = unidades
        print(f"{producto} fue agregado con {unidades} unidades.")

print("\nEstado final del stock:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock} unidades")

# Ejercicio 9
agenda = {}

agenda[("Lunes", "09:00")] = "Reunión"
agenda[("Martes", "14:00")] = "Llamada con cliente"
agenda[("Miércoles", "11:30")] = "Cumple"
agenda[("Jueves", "16:00")] = "Clases"
agenda[("Viernes", "10:00")] = "Gimnasio"

print("Agenda semanal:")
for clave, evento in sorted(agenda.items()):
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

dia = input("\nIngresá el día para consultar (ej: Lunes): ")
hora = input("Ingresá la hora para consultar (ej: 09:00): ")

clave = (dia, hora)
if clave in agenda:
    print(f"Evento programado: {agenda[clave]}")
else:
    print("No hay eventos programados para ese día y hora.")

# Ejercicio 10
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

capitales_a_paises = {}

for pais, capital in paises.items():
    capitales_a_paises[capital] = pais

print("Diccionario capital -> país:")
print(capitales_a_paises)
