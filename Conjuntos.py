'''# Son datos desornedados y Unicos

# conjunto = set () El "set" Es para diferenciar los conjuntos de los diccionarios ya que como los diccionarios los dos utilizan {}

# conjunto = {1,2,3,5,6} No pueden haber valores duplicados porque se va a guardar como valor unico // Ejemplo conjunto = {1,2,3,5,6,1} 
# print (conjunto)
# conjunto = {1,2,3,5,6} Solo se van a imprimir los valores que no estan duplicados '''

conjunto = set ()

conjunto = {1,2,3,5,6}

'''# conjunto.add (2) Este es el metodo para agregar 
# conjunto.add (Aqui va el valor que quieres eliminar ) Este es el metodo para eliminar 
# conjunto.clear () Para eliminar todo Rey 

# Tambien se puede buscar en el conjunto '''

print (conjunto)


a = {1,2,3}
b = {3,4,5}

'''# c = a | b De esta manera se hace la Union de los conjuntos
# c = a & b  Para hacer la interseccion 
# c = a - b La diferencia para mostrar los que estan en a y no en y viceversa asi: c = b - a // Esto es para los valores que estan en un lado y no esten al mismo tiempo en el otro

# c = a ^ b Esto es para la difencia simetrica (Valores que estan en ambos conjutos pero no no al mismo tiempo)

# Se pueden volver conjuntos inmutables de la sgte forma a = frozenset({1,2,3})
'''
c = a ^ b 

print (c)