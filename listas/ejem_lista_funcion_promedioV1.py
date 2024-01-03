#Robles Pulido Efrain
#Programa donde vamos a guardar cinco calificaciones en una lista,
#enviaremos la lista a una funcion la cual calculara el promedio y lo devolvera

def main():
    calif=[76.5,86.5,99.5,63.5,98.5]
    prom=calcular_promedio(calif)
    print("El promedio es", prom)

def calcular_promedio(calif):
    indice=acum=p=0
    while indice<len(calif):#len(calif) nos dara la longitud de la lista
        acum=acum+calif[indice]
        indice+=1 #indice= indice+1
    p=acum/indice
    return p

main()
