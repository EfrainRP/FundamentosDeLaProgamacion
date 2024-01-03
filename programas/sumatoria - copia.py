# Robles Pulido Efrain
#Rodríguez Cano Christian Fabian.
#Rodríguez Rico Mario Eduardo.
#seccion D13
#calendario 2021A
#Programa para una sumatoria del 1 hasta el numero limite

n=st=0
#Entrada
n= int(input("Dame un numero entero (limite):  "))

#ciclo for
for num in range(1, n+1):
    st=num+st #sumatoria de todos los terminos del 1 hasta nuestro limite 

for num in range(1, n):
    print(num, end=' + ')#imprimira cada termino del 1 hasta nuestro limite

print(num+1, end=' ')
print(' = ',st)


