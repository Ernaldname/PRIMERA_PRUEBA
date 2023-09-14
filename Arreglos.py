#creamos los arreglos (vacios para iniciar)

nombres = [] #se almacenan los nombres 
ids = [] #se almacenan las ids 

#definir un tamaño para los arreglos 
capacidad=3

# leer los datos y guardarlos en los arreglos

for i in range(1,capacidad):
  print ("Ingrese los datos de la persona:", i+1)
  nombre = input("Nombre: ")
  id = input("Indentificación: ")

  nombres.append(nombre)
  ids.append(id)

# ahora mostraos los arreglos 
for i in range (1, capacidad):
    print ("Los datos  de la persona: ", i+1)
    print ("El nombre es: ", nombres[i])
    print ("La indentificación es: ", ids[i])