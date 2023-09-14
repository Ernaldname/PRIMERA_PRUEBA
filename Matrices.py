Cantidad = int (input ("Numero De empleados: "))
Semanas = int (input ("Numero de Semanas : "))
Nombre = (input ("Nombre: "))

for i in range (0,Semanas): 
  Horas = int (input ("Cantidad de horas: "))

for i in range (1,Cantidad):
  Nombre = (input ("Nombre: "))
  Semanas = int (input ("Numero de Semanas : "))
  Horas = int (input ("Cantidad de horas: "))
  for i in range (0,Semanas): 
    Horas = int (input ("Cantidad de horas: "))
  
print ("Menu")

print ("1. Calcular salario total")
print ("2. Calcular pago nómina semanal")

digite = ("Digite su opcion: ")

if digite == 1: print ("El salario del empleado 1",)
