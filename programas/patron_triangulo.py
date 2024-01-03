#Robles Pulido Efrain
#Rodríguez Cano Christian Fabian.
#Rodríguez Rico Mario Eduardo.
#seccion D13
#calendario 2021A
#Programa para tener el patrón de un triángulo.

base = 8 #Tamaño del patrón 

#Estructura de control repetitiva desde - anidado
for r in range(base):#la lista es [0,1,2,3,4,5,6,7]
    for c in range(base,r,-1):#la lista depende del valor de r pero 
                            #comenzara con la "base" y es descendente
        print('*', end='')#Salida
    print()#salto de linea
