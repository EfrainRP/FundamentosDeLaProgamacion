# Robles Pulido Efrain
#Programa para calcular el promedio de 5 calificaciones

calif=prom=acum=0.0
cont=1 #inicializacndo la variable de control

#ciclo mientas
while cont <=5: #condicion
    #entrada
    calif=float(input("Dame una calificacion: "))
    acum=acum + calif
    cont=cont + 1 #incremento de la variable de control
    
#calculando el promedio
prom=acum/(cont-1)#la resta es para compensar que el contador aumento +1
#cuando llego a 6 y estamos utilzando solo 5 ciclos

#salida
print("El promedio es: " ,prom)
