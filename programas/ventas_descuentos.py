#Robles Pulido Efrain
#Rodríguez Cano Christian Fabian.
#Rodríguez Rico Mario Eduardo.
#seccion D13
#calendario 2021A

#Programa para determinar el descuento utilizado y el precio a pagar
#Entrada
p= int(input("Teclea la cantidad de productos comprados: "))
#Proceso
d=p*99 #Operacion para calcular el precio total a pagar

#Estructura de control selectiva doble anidada y el operador lógico “y”
if p>=10 and p<=19:
    pd=d*(1-0.2)#Operacion para calcular el precio total a pagar con su descuento
    print ("Tu descuento es de 20% y pagaras $", pd) #Salida

elif p>=20 and p<=49:
    pd=d*(1-0.3)#Operacion para calcular el precio total a pagar con su descuento

    print ("Tu descuento es de 30% y pagaras $", pd) #Salida

elif p>=50 and p<=99:
    pd=d*(1-0.4)#Operacion para calcular el precio total a pagar con su descuento
    print ("Tu descuento es de 40% y pagaras $", pd) #Salida
    
else:
    print ("Cantidad fuera de la promoción") #Salida
