'''
• Crear un diccionario donde se almacene el usuario y la clave.
• Pedir el ingreso por teclado de usuario y clave.
• Validar que lo ingresado sea igual a los datos del diccionario, de lo contrario mostrará un error de inicio de sesión.
El usuario solo tiene un máximo de 3 intentos fallidos, al superarlos termina el programa.
• Cuando el inicio de sesión es correcto, pasa un menú de dos opciones:
1. Convertir fecha en texto.
2. Calcular tiempo de nacido.
• En la primera opción, solicitar por teclado una fecha en formato "11/02/2022", crear una función que devuelva lo siguiente "Viernes, 11 de febrero de 2022".
• La segunda opción, solicitar la fecha de nacimiento, crear una función que devuelva los años, meses y días de
nacido (edad).
'''



usu = str (input ("Ingrese su nombre: "))
code = str (input ("Ingrese codido de usuario: "))

dic = {usu:code}

print ("La llave es: ",dic.keys())



'''name = input ("Ingrese nombre: ")
cod = input ("Ingrese condigo: ")


if name in usu and cod in code:
    print ("Eres el elejido Neo \n Elije una opcion \n 1) Jalarte la marmota o 2) Salvar al mundo")
    opci = int (input ("Ingrese una de las 2 opciones: "))
    while opci < 1 or opci > 2:
        print ("Error mija")
        opci = int (input ("Ingrese una de las 2 opciones: "))
            
else: print ("Paila rey")

'''