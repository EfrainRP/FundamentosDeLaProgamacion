#Robles Pulido Efrain
# This program displays a triangle pattern.
BASE_SIZE = 8
 
for r in range(BASE_SIZE):#la lista es [0,1,2,3,4,5,6,7]
    #El ciclo anidado dara una vuelta la primera vez,
    #dos vueltas la segunda vez, ....,etc.
    for c in range(r + 1):#la lista depende del valor de r
        print('*', end='')
    print()#salto de linea
