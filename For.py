'''y = 0
for i in range (1,21):
  y = y + 2/i ** 2
print(format (y,".5f"))'''


'''coleccion = 1,2,3,4,5,6

for i in (coleccion):
  print (f"Hola Rey: {i}")'''
  

Nom1 = str (input ("Escriba su Nombre: "))
edad1 = int (input ("Escriba su Edad: "))

Nom2 = str (input ("Escriba su nombre: "))
edad2 = int (input ("Escriba su Edad: "))

Nom3 = str (input ("Escriba su nombre: "))
edad3 = int (input ("Escriba su Edad: "))

coleccion = {Nom1: edad1, Nom2: edad2, Nom3: edad3}

for i in coleccion:
  print (f" {i}, {coleccion [i]}")