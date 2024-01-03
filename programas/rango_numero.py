#Robles Pulido Efrain
#Programa para determinar si un numero se encuentra en algun rango

#entrada
num= int(input("Dame un numero entre 1 y 1000: "))
#selectiva doble o compuesta anidada
if num >=1 and num <=10:
    print("El numero",num,"se encuentra entre 1 y 10") #Salida

elif num >=11 and num <=100:
    print("El numero",num,"se encuentra entre 11 y 100") #Salida

elif num >=101 and num <=1000:
    print("El numero",num,"se encuentra entre 101 y 1000") #Salida

else:
    print("El numero",num,"está fuera de los rangos") #Salida
