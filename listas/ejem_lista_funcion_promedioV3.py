#Robles Pulido Efrain
#Programa donde vamos a guardar cinco calificaciones en una lista,
#enviaremos la lista a una funcion la cual calculara el promedio y lo devolvera

def main():
    lista_califs_llena=llenar_lista_usuario()
    #print(calif_cero) #punto de inspeccion (lista cero, solo tiene ceros)
    print("Las calificacones son:", lista_califs_llena)#lista llena con los valores introducidos
    
    prom=calcular_promedio(lista_califs_llena)
    print("El promedio es", format(prom,'.2f'))#promedio de los valores ya introducidos

def llenar_lista_usuario():
    cant = int(input("Dame cantidad de materias: "))
    list_califs=[0.0]*cant#Creo un espacio en forma de lista de acuerdo a la  
                        #cantidad de materias para agregar los valores deseados 
    index=0
    while index< cant:
        list_califs[index] = float(input("Dame calificacion: "))#para poder hacer eso debemos 
        index+=1                                #de tener creada la lista con todos los elementos dentro 
                                                #para solo tener que áctualizarla con la linea 9
    #print(calif_cero)#punto de inspeccion
    return list_califs#regresamos la lista llena de calificaciones

def calcular_promedio(lista_califs):
    indice=acum=p=0
    while indice<len(lista_califs):#len(lista_califs) nos dara la longitud de la lista llena
        acum=acum+lista_califs[indice]
        indice+=1 #indice= indice+1
    p=acum/indice
    return p

main()
