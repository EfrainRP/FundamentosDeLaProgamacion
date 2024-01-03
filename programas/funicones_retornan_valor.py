#Robles Pulido Efrain
#Rodríguez Cano Christian Fabian.
#Rodríguez Rico Mario Eduardo.
#seccion D13
#calendario 2021A
#Programa para determinar la estacion del mes de nacimiento

#Funcion principal
def main():
    mes=int(input("Dame el numero del mes de nacimiento: "))
    estacion= evaluacion (mes)
    print("Naciste en la temporada de", estacion)

#Funcion de evaluacion del mes
def evaluacion(mes):
    if mes==12 or mes==1 or mes==2:
        return ('Invierno')#Regresara el valor resultante a la funcion principal
    
    elif mes==3 or mes==4 or mes==5:
        return ('Primavera')#Regresara el valor resultante a la funcion principal
    
    elif mes==6 or mes==7 or mes==8:
        return ('Verano')#Regresara el valor resultante a la funcion principal

    elif mes==9 or mes==10 or mes==11:
        return ('Otoño')#Regresara el valor resultante a la funcion principal

#Llamada a la funcion principal     
main()
