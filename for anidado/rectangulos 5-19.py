#Robles Pulido Efrain
# This program displays a rectangular pattern
# of asterisks.
rows = int(input('How many rows? '))
cols = int(input('How many columns? '))

for r in range(rows): #CICLO EXTERIOR
    for c in range(cols): #CICLO ANIDADO
        print('*', end='')
    print(' ')#SALTO DE LINEA
