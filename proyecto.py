capantalones = 150 
cacamisas = 100 
casacos = 5 
casombreros = 10  
cazapatosi = 11 
cazapatosf = 11 

valorpant = 25000
valorcami = 10000
valorsac = 45000
valorsombre = 5000
valorzapai = 90000
valorzapaf = 90000

new = {}
per = {}

usuario = 0

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
    print ("1) Vender / 2) Modificar / 3) Agregar ")
    ven = int (input ("Ingrese 1 opcion: "))
    while (ven < 0 or ven > 3):
        print ("No esta permitido en el sistema, seleccione una de las 3 opciones mencionadas: ")
        ven = int (input ("Ingrese 1 opcion: "))
    if ven == 1: 
            print ("EN EL INVENTARIO HAY DISPONIBLE: \n ")

            print ("Que desea vendeer: ")
            print ("EN EL INVENTARIO HAY DISPONIBLE: \n ")
            print (f"1) {capantalones} Pantalones disponibles a {valorpant} C/U")
            print (f"2) {cacamisas} Camisas disponibles a {valorcami} C/U")
            print (f"3) {casacos} Sacos disponibles a {valorsac} C/U")
            print (f"4) {casombreros} Sombreros disponibles a {valorsombre} C/U")
            print (f"5) {cazapatosi} Zapatos Deportivos disponibles a {valorzapai} C/U")
            print (f"6) {cazapatosf} Zapatos Formales disponibles a {valorzapaf} C/U \n")
            
            articulo = int (input("Ingrese el articulo "))
            if articulo == 1: 
                cantidad1 = int (input ("Que cantidad: "))
                print ("EN EL INVENTARIO: \n ")
                print (f"1) Quedan {capantalones - cantidad1} Pantalones disponibles a {valorpant} C/U")

                print ("Elija 1 opcion \n")
                print ("1. Volver al inicio")
                print ("2. Vender otro producto")
                print ("3. Salir corriendo por ver eso precios")
                print ("4. Ver total de ventas del dia")
                opp = int (input("Ingrese la opcion: "))
                if opp == 3:
                    print ("Corra perra corra")

            elif articulo == 2: 
                cantidad1 = int (input ("Que cantidad: "))
                print ("EN EL INVENTARIO: \n ")
                print (f"2) {cacamisas - cantidad1} Camisas disponibles a {valorcami} C/U")

                print ("Elija 1 opcion \n")
                print ("1. Volver al inicio")
                print ("2. Vender otro producto")
                print ("3. Salir corriendo por ver eso precios")
                print ("4. Ver total de ventas del dia")
                opp = int (input("Ingrese la opcion: "))
                if opp == 3:
                    print ("Corra perra corra")
                

           



