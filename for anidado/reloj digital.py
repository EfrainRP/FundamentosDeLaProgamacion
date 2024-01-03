#Robles Pulido Efrain

# Programa para simular el comportamiento de un reloj digital

# Tema: Ciclos anidados, pag. 190 libro Tony Gaddis
#Cuantos valores genera la llamada a la funcion range (60)? R=60
#Cuales son los valores de la lista? R=[0,1,2,3,4,5,...57,58,59]
#Cuantas vueltas o iteracions dara cada ciclo? R=60
#Total de vueltas entre los dos ciclos?R=60 * 60 =3600

# Ciclo que controla los minutos
for minutes in range(60):#[0,1,2,3,..,59]
    #ciclo que controla los segundos
    for seconds in range(60):#[0,1,2,3,..,59]
        print(minutes,':', seconds)
