# Diccionario 
# Tienen que haber una clave y un valor 


diccionario = {"Azul":"Blue","Rojo":"Red","Verde":"Green"}

# print (diccionario["Azul"]) De esta manera se puede buscar en los diccionarios /// Escribes las clave (llave) y te devuelve un valor 

# De esta manera se agrega diccionario["Naranja"] = "Orange" 

# Al igual que para modificar el valor diccionario["Naranja"] = "ORANGE"

# del (diccionario ["Verde"]) de esta manera se puede eliminar 

del (diccionario ["Rojo"])

print (diccionario)

# Se puede editar, modificar, eliminar y agregar un diccionario dentro de otro diccionario 

# equipo = {10:"Paulo Dyvala",7:"Cristiano",}

# print (equipo.keys()) De esta forma imprime las claves del diccionario 

# print (equipo.values()) De esta forma imprime los valores del diccionario 

# print (equipo.items()) te muestra la clave y el valor dentro del diccionario cada uno de ellos en listas 

# print (equipo.items())

# Ejercicios de prueba 

'''
DIVISA 

divisa = {"Euro":"€", "Dollar": "$", "Yen":"¥" }

print ("1) Euros €")
print ("2) Dollares $")
print ("3) Yenes ¥")

conver = int (input ("Escriba moneda a convertir: "))
while conver < 0 or conver > 3:
    print ("No perrin, elija otra vez")
    conver = int (input ("Escriba moneda a convertir: "))
if conver == 1:
    print ("Okay usted eligio ", divisa["Euro"])
elif conver == 2:
    print ("Okay usted eligio ", divisa["Dollar"])
elif conver == 3:
    print ("Okay usted eligio ", divisa["Yen"])

'''


'''
DATOS PERSONALES

Nombre = str (input ("Escriba su Nombre: "))
Edad = int (input ("Escriba su Edad: "))
Direccion = (input ("Escriba su Direccion: "))
Telefono = int (input ("Escriba su Telefono: "))

dic = {"Nombre":Nombre, "Edad": Edad, "Direccion": Direccion, "Telefono": Telefono}

print (dic["Nombre"], "Tiene",dic["Edad"], "años, vive en", dic["Direccion"], "y su numero de telefono es", dic["Telefono"] )

'''

'''
FRUTAS

frutas = {"Platano":1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))

if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")

'''

'''
MESES

mes = {"Enero":"Enero", "Febrero":"Febrero", "Marzo": "Marzo","Abril": "Abril","Mayo": "Mayo","Junio": "Junio","Julio": "Julio","Agosto": "Agosto","Septiembre": "Septiembre","Octubre": "Octubre","Noviembre": "Noviembre","Diciembre": "Diciembre :3"}

dia = int (input ("Escriba el dia: "))
meses = str (input ("Escriba el mes: ")).title()
año = int (input ("Escriba el año: "))

if meses in mes:
    print ("Dia",dia,"de ",mes[meses],"del año ",año)



'''
 
'''
Con .itmes 

 curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for a, b in curso.items():
    print(a, 'tiene', b, 'créditos')
    total_creditos += b
print('Número total de créditos del curso: ', total_creditos)
'''

'''
CON EL METODO ITEMS():

Informacion de usuarios


producto = {}

cantidad = int (input ("Ingrese el numero de personas: "))

for i in range (0, cantidad):
    keyss = input("Nombre de invitado: ")
    print ("Edad del invitado: ")
    valor = input(keyss + ": ")
    producto[keyss] = valor
    for x, y in producto.items(): 
        print ("Nombre: ", x, "Edad: ",y)

'''

'''
METODO ZIP()

Recibe un parametro de dos elementos iterables 
ambos parametros deben tener el mismo numero de elementos 

dic = dict (zip("abcd",[1,2,3,4]))

print (dic)

{'a': 1, 'b': 2, 'c': 3, 'd': 4} Se imprimira esto 
'''

'''
KEYS()

Para retornar las llaves

VALUES()

Para retornar los valores

'''

'''
CLEAR

Elimina todos los items del diccionario dejandolo vacio

dic1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic1.clear()

print (dic1)
'''

'''
FROMKEYS

Recibe como parametros un iterable y un valor, devolviendo
un diccionario que contiene como claves los elementos del iterable con el mismo valor

dic = dict.fromkeys(["Vaca","por","P"],3)

print (dic)
'''


'''
PARA ASIGNAR UN VALOR A LA CLAVE DE UN ELEMENTO DEL DICCIONARIO (MODIFICARLO MEJOR DICHO)

versions = {"zope": None, "Well": 5}
versions["zope"] = 2.3

print (versions)

'''


'''
Eleccion 

dic = {1: "Vida", 2: "Muerte"}

for x, y in dic.items():
    print (x, y)

ing = int (input ("Ingrese un numero "))

if ing in dic:
    print ("Epa perrin")

else: print ("Pailas")


'''