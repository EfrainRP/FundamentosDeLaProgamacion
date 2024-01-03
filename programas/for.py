# Robles Pulido Efrain
#Programa para determinar una lista de num. pares y nones 

p=n=0

p=int(input("Dame un limite para numero pares: "))
n=int(input("Dame un limite para numero nones: "))


#ciclo for pares
for p in range(2, p+1,2):
    print(p, end='  ')#Salida
print("  ")

#ciclo for nones
for n in range(1, n+1,2):
    print(n, end='  ')#Salida
print("  ")
    

    
