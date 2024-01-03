#Robles Pulido Efrain
#Programa donde vamos a guardar cinco calificaciones en una lista,
#enviaremos la lista a una funcion la cual calculara el promedio y lo devolvera

def main():
    cant = int(input("Dame cant. de materias: "))
    calif=[0.0]*cant#Creo un espacio en forma de lista para agregar los valores deseados
    index=0
    while index< 5:
        calif[index] = float(input("Dame calificacion: "))#para poder hacer eso debemos 
        index+=1                                #de tener creada la lista con todos los elementos dentro 
                                                #para solo tener que áctualizarla con la linea 9
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
