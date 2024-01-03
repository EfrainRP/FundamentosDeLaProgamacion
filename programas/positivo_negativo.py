#Robles Pulido Efrain
#Rodríguez Cano Christian Fabian.
#Rodríguez Rico Mario Eduardo.
#seccion D13
#calendario 2021A

#Programa para determinar el total de números positivos y negativos ingresados

n=neg=pos=0

#entrada
n=int(input("Dame un numero o CERO para salir: "))

#ciclo mientas
while n != 0: 
    if n<0:
        neg=neg+1

    else:
        pos=pos+1

    n=int(input("Dame un numero o CERO para salir: "))

print("Total de numeros positivos" ,pos)
print("Total de numeros negativos" ,neg)
