# Robles Pulido Efrain
#Programa para una tabla de multiplicación seleccionable

t=li=ls=0

#entrada
t=int(input("Teclea el num de la tabla: "))
li=int(input("Dame el limite inferior: "))
ls=int(input("Dame el limite superior: "))
    
#ciclo mientas
while li <=ls: #condicion
    m=t * li
    print(t," * ",li," = ",m)
    li=li + 1 #incremento de la variable de control con el limite inferior
    
