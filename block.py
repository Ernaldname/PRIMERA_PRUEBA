'''
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras
que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

'''

Materias = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in Materias:
    if i % 3:
        Materias.remove(i)
print("Las Letra son: " + str(Materias))


