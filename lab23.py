import os
dicc_admin={}
dicc_inventario={}
dicc_users={}
ID_Ptemp=[]



def config_admin():
  ID_A=input ("Ingrese cédula del admin: ")
  while (True):
    passtemp1=str(input("Ingrese una contraseña: "))
    passtemp2=str(input("Confirme su contraseña: "))
    if (passtemp1==passtemp2):
      password=passtemp1
      break
    else:
      print("Las contraseñas no coinciden")
  nombre=input("Ingrese el nombre del responsable: ")
  dicc_admin[ID_A] = [password,nombre]


def inventario():
  while True:
    while True:
      IDtemp = int(input("Ingrese el ID para el producto: "))
      if (len(ID_Ptemp)==0):
        ID_P=IDtemp
        ID_Ptemp.append(IDtemp)
        break
        
      elif(len(ID_Ptemp)>0): 
        while True:
          for i in range (0,len(ID_Ptemp)):
            if (IDtemp==ID_Ptemp[i]):
              print ("El ID ingresado ya existe, por favor ingrese otro")
              IDtemp = int(input("Ingrese el ID para el producto: "))
            else:
              break
          break
        ID_P=IDtemp
        ID_Ptemp.append(IDtemp)      
          
        break
       
      
    nombreP = str(input("Ingresar el nombre del producto: "))
    cantidadP = int(input("Ingresar la cantidad de artículos del producto: "))
    precioP = int(input("Ingresar el precio del producto: "))
    
    
    dicc_inventario[ID_P] = [nombreP,cantidadP,precioP]
    

    op=str(input("¿Desea seguir agregando productos? Digite S para si o N para no: "))

    if (op=="S" or op=="s"):
      os.system('clear')
    elif (op=="N" or op=="n"):
      os.system('clear')
      break
    else:
      print("Opción inválida")

def config_users():
  while True:
    ID_U=input ("Ingrese cédula del vendedor: ")
    while (True):
      passtemp1=str(input("Ingrese una contraseña: "))
      passtemp2=str(input("Confirme su contraseña: "))
      if (passtemp1==passtemp2):
        password=passtemp1
        break
      else:
        print("Las contraseñas no coinciden")
    nombre=input("Ingrese el nombre del responsable: ")
    dicc_users[ID_U] = [password,nombre]
    op=str(input("¿Desea seguir agregando usuarios? Digite S para si o N para no: "))

    if (op=="S" or op=="s"):
      os.system('clear')
    elif (op=="N" or op=="n"):
      os.system('clear')
      break
    else:
      print("Opción inválida")

def config_inicial():
  config_admin()
  inventario()
  config_users()


config_inicial()

while True:
  print("Bienvenido al AJASITOSNO")







  

    
#print (notas)