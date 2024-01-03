#Robles Pulido Efrain
#Rodríguez Cano Christian Fabian.
#Rodríguez Rico Mario Eduardo.
#seccion D13
#calendario 2021A

#Programa donde utilizaremos un menú para que el usuario
#elija una opcion que necesite trabajar

import random #Importacion del aleatorio

#Funcion que realizaran las llamadas del menu
def main():
    Opci=0
    while Opci!=6:#Ciclo en donde se selecciona una opcion o el 6 para salir
        print("MENÚ - LISTAS")
        print("1. Llenar lista usuario (calificaciones)")
        print("2. Calcular promedio lista usuario")
        print("3. Llenar lista aleatoriamente (edades)")
        print("4. Determinar la persona de menor edad")
        print("5. Determinar la persona de mayor edad")
        print("6. Salir")
        
        Opci=int(input("Elige tu opcion: "))#Seleccion de la opcion

        if Opci==1:#Llena la lista con calificaciones
            lista_califs_llena=llenar_lista_usuario()
            print("Las calificaciones son = ", \
                  lista_califs_llena)#Lista llena con los valores introducidos
            print(" ")#Salto de linea
            
        elif Opci==2:#Se calcula el promedio de las anteriores calificaciones 
            print("El promedio es = ", format(calcular_promedio(lista_califs_llena),\
                                              '.2f'))#promedio de los valores ya introducidos
            print(" ")#Salto de linea
            
        elif Opci==3:#Se llena la lista de edades aleatoriamente con la funcion
            lista_edad=llenar_lista_aleatoriamente()
            print("Las edades son = ", lista_edad)
            print(" ")#Salto de linea
            
        elif Opci==4:#Se determinara la edad mas joven
            print("La persona mas joven tiene ", determinar_menor(lista_edad), "años")
            print(" ")#Salto de linea
            
        elif Opci==5:#Se determinara la edad mas adulta
            print("La persona mas adulta tiene", determinar_mayor(lista_edad), "años")
            print(" ")#Salto de linea
            
        elif Opci==6:#Salida del programa
            print("Gracias por utilizar este software")

#Funcion que permitira llenar una lista con calificaciones
def llenar_lista_usuario():
    cant_calif = int(input("¿Cuantas calificaciones se van a promediar?: "))
    list_califs=[0.0]*cant_calif#Se crea una lista inicializada con la misma cantidad 
                                #de materias para agregar las calificaciones deseadas 
    index=0
    while index < cant_calif:
        list_califs[index] = float(input("Dame una calificacion: "))#Se introduce las calificaciones
        index+=1
        
    return list_califs#Regresamos la lista llena de calificaciones

#Funcion para calcular el promedio de las calificaciones de la lista
def calcular_promedio(lista_califs):
    indice=acum=p=0
    while indice < len(lista_califs):#len(lista_califs) nos dara la longitud de la lista llena
        acum=acum+lista_califs[indice]
        indice+=1 #indice= indice+1
    p=acum/indice #Division normal para obtener el promedio
    return p #Se regresa el promedio

#Funcion para generar una lista aleatoria de edades
def llenar_lista_aleatoriamente():
    cant_ed= int(input("¿Cuantas edades vamos a trabajar?: "))
    lista_edades=[0]*cant_ed #Se crea una lista inicializada con la misma
    index=0                     #cantidad de edades a utilizar
    while index < cant_ed:
        lista_edades[index] = random.randint(1,100)#Se generara un num. aleatorio del 1 al 100
        index+=1 
    return lista_edades #Se regresa la lista llena de edades

#Funcion para encontrar la edad mas joven de la lista de edades, es decir, el minimo
def determinar_menor(lista_edad):
    Edad_menor=min(lista_edad)
    return Edad_menor #Se regresa la edad mas joven

#Funcion para encontrar la edad mas adulta de la lista de edades, es decir, el maximo
def determinar_mayor(lista_edad):
    Edad_mayor=max(lista_edad)
    return Edad_mayor #Se regresa la edad mas adulta

#LLamada a la función principal
main()
