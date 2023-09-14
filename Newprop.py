print ("Siendo 1 = Administrador y 2 = Vendedor")

usuario = int (input ("Por favor ingrese su usuario: "))
nombre = input ("Escriba su nombre: ")
telf = input ("Escriba su Telefono: ")


while (usuario < 0 or usuario > 2):
    print ("No esta permitido en el sistema, seleccione una de las 2 opciones mencionadas: ")
    usuario = int (input ("Por favor ingrese su usuario: "))
if usuario == 1: print ("\nBienvenido ",nombre, "ya puede administrar el inventario \n")
elif usuario == 2: print ("\nBienvenido",nombre, "ya puede efectuar ventas \n")
else: print ("Opcion no valida")

if usuario == 1: 
    print ("Que opcion realizara ") 
    print ("1) Opciones de Ventas / 2) Modificar Almacen / 3) Agregar Surtido")
    ven = int (input ("Ingrese 1 opcion: "))
    
    while (ven < 0 or ven > 3):
        print ("No esta permitido en el sistema, seleccione una de las 3 opciones mencionadas: ")
        ven = int (input ("\n Ingrese 1 opcion: "))

    producto = {}
    continuar = True

    while continuar:
     
        print ("\n Elija 1 opcion \n")
        print ("1. Agregar producto")
        print ("2. Vender Producto")
        print ("3. Ver total de ventas del dia")
        opci = int (input ("Seleccione una opcion: "))

        while (opci < 0 or opci > 3 ):

            print ("\n No esta permitido en el sistema, seleccione una de las 3 opciones mencionadas: ")
            print ("1. Agregar producto")
            print ("2. Vender Producto")
            print ("3. Ver total de ventas del dia")

            opci = int (input ("\n Ingrese 1 opcion: "))
            
        break

    if opci == 1: keyss = input('¿Que Producto desea agregar? ')

    print ("Escriba el valor")
    valor = input (keyss + ": ")
    producto[keyss] = valor
    print(producto)
    continuar = int (input('¿Quieres añadir más información (1= Si / 2 = No)? '))
    
    if continuar == "1":

        keyss = input('¿Que Producto desea agregar? ')
        print ("Escriba el valor")
        valor = input(keyss + ": ")
        producto[keyss] = valor
        print(producto)
        continuar = (input('¿Quieres añadir más información (1= Si / 2 = No)? '))
    
    elif continuar == "2": print ("Elija 1 opcion \n")
    print ("\n Elija 1 opcion \n")
    
    print ("1. Vender producto")
    print ("2. Salir corriendo por ver esos precios")            
    print ("3. Ver total de ventas del dia")
    continuar = int (input ("Seleccione una opcion: "))
    while (continuar < 0 or continuar > 2 ): print ("No esta entre las opciones ")
    print ("\n Elija 1 opcion \n")
    print ("1. Vender producto")
    print ("2. Salir corriendo por ver esos precios")            
    print ("3. Ver total de ventas del dia")
    continuar = int (input ("Seleccione una opcion: "))       

