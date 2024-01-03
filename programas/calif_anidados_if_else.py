#Robles Pulido Efrain
#Programa que imprime un mensaje acorde a la puntuacion obtenida en el curso
#entrada
calif= int(input("Dame calificacion final: "))
#selectiva doble o compuesta anidada
if calif>=90:
    print("Excelente")

else:
    if calif>= 80:
        print("Bien")

    else:
        if calif>= 70:
            print("Regular")

        else:
            if calif >=60:
                print("Estudia mas")

            else:
                print("Suerte para la proxima")
