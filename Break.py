while True:
    x = input("Ingrese un numero ('*' para terminar): ")
    if x == '*': break
    elif x > 0: 
        print ("Numero positivo")
    elif x == 0: 
        print ("Igual a 0")
    else: print ("Numero negativo")