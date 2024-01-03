#Robles Pulido Efrain

# Programa para simular el comportamiento de un reloj digital

# Tema: Ciclos anidados, pag. 190 libro Tony Gaddis
#Total de vueltas entre los dos ciclos?R=24 * 60 * 60 =86400

# Ciclo que controla las horas
for hours in range(24):#[0,1,2,3,..,23]
    # Ciclo que controla los minutos
    for minutes in range(60):#[0,1,2,3,..,59]
        #Ciclo que controla los segundos
        for seconds in range(60):#[0,1,2,3,..,59]
            #for mili in range (60) es para que su comportamiento sea mas realista a un reloj
                print(hours,':', minutes,':', seconds)
