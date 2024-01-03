#Robles Pulido Efrain
#Programa de convertidor de Celsius a Fahrenheit

def main():
    temp=float(input("Tecle una cantidad de °C: "))
    convertidor_C_a_F(temp)#temp es el argumento
    temp2=float(input("Tecle una cantidad de °F: "))
    convertidor_F_a_C(temp2)

def convertidor_C_a_F(tempC):#tempC es el parametro
    tempF=(tempC*9/5)+32
    print(tempC,"grados °C =", tempF, "grados °F")

def convertidor_F_a_C(tempF):#tempF es el parametro
    tempC=(tempF-32)*5/9
    print(tempF,"grados °F =", tempC, "grados °C")

main()

