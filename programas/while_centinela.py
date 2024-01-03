# Robles Pulido Efrain
#Programa para calcular el promedio de 5 calificaciones

calif=acum=0.0
cont=0 #inicializacndo la variable de control

#entrada
calif=float(input("Teclea una calificación o -1.0 para salir: "))

#ciclo mientas
while calif !=-1: #condicion
    acum=acum + calif
    cont=cont + 1 #incremento de la variable de control
    #print("cont=",cont)
    #print("acum=",acum)
    
    #entrada
    calif=float(input("Teclea una calificación o -1.0 para salir: "))
    #print("2cont=",cont)

if cont !=0:
    print("El promedio es: " ,acum/cont)
else:
    print("No se introdujeron calificaciones")
