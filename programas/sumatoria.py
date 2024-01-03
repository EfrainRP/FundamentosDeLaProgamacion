#Robles Pulido Efrain
#Rodríguez Cano Christian Fabian.
#Rodríguez Rico Mario Eduardo.
#seccion D13
#calendario 2021A
#Programa para una sumatoria del 1 hasta el numero limite

n=0 #Inicializacion

#Entrada
n= int(input("Dame un numero entero (limite):  "))

#Estructura de control repetitiva desde
for num in range(1, n):
    print (num, end=' + ')#Salida, no se mostrara el valor limite en la lista
                          # para que cuando llegue a n-1 imprima el '+' al final 
  
print(num+1, end='') #Salida, imprimiremos el ultimo valor faltante
                     #del num para que sea igual al limite y no muestre '+' al final
#Proceso   
x=(n*(n+1))/2 #Formula (de Gauss) de la sumatoria de numeros consecutivos 
print(' =', x)#Salida

