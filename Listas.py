Lista = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
Lista1 = ["1","2","3","4","Viernes"]

'''# Lista.append("Sabado") Para agregar al final de la lista 

# Lista.insert (3,"Festivo") Para agregar no necesariamente al final de la lista // Primero el lugar que quieres que ocupe y despues el valor o el texto 

# Lista.extend([1,2,3,4,5]) Agrega los elementos que pusimos al final de la lista 

# Lista2 = ["R","S"]
# lsita = Lista + Lista2 Se pueden sumar listas 

# print ("Viernes" in Lista) Podemos determinar si un elemento esta en la lista 

# print (Lista.index("Viernes")) Para determinar que indice tiene 

# print (Lista.count("X")) Determina cuantas veces aparece eso en la lista (Cuenta)

# Lista.pop (2) Sirve para eliminar un elemento de la lista indicandole el indice que quieres eliminar 

 # Lista.remove (3) Indicandole el valor lo eliminas // El pp es para el indice si lo sabes 

# Lista.clear () Elimina todo mi perro jajas

# Lista.sort () Sirve para ordenar elementos acesdentemente '''


'''
NOTAS DE LAS MATERIAS

Materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
Notas = []

for iterador in Materias:
    Nota = input("¿Qué nota has sacado en " + iterador + "?")
    Notas.append(Nota)
for i in range(len(Materias)):
    print("En " + Materias[i] + " has sacado " + Notas[i])

'''

'''

PARA ORDENAR LOS NUMEROS DE UNA LISTA DE MENOR A MAYOR CON .SORT()


awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un número ganador: ")))
awarded.sort()
print("Los números ganadores son " + str(awarded))

'''

'''
PARA INSERTAR 

Lista = [1,2,3,4,5]

Lista.insert(1,"Allone") <- El numero lo toma como el indice que ocupara

for i in Lista:
    print ("Numero", i)


PARA REMOVER UN INDICE QUE COINCIDA CON EL VALOR

a = ["Sol", "Luna"]

a.remove("Sol")

print (a)




SIRVE PARA DETERMINAR CUANTOS ELEMENTOS HAY EN UNA LISTA 

a = ["Sol", "Luna", "Vaca"]

del a[2]

print (len (a))




ELIMINA EL ELEMENTO DEL INDICE QUE LE INDICAMOS 

a = ["Sol", "Luna", "Vaca"]

del a[2]

print (a)


PARA ORDENAR DE MANERA DECENDENTE 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for i in numbers:
    print(i, end=" Sgte ")


PARA EVALUAR LOS NOTAS 

Materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
Notas = []

for i in Materias:
    score = float(input("¿Qué nota has sacado en " + i + ": "))
    if score >= 5:
        Notas.append(i)
for i in Notas:
    Materias.remove(i)
print("Tienes que repetir " + str(Materias))

'''

print (Lista)

