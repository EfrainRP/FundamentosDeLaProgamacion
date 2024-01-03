#Robles Pulido Efrain
#Rodríguez Cano Christian Fabian.
#Rodríguez Rico Mario Eduardo.
#seccion D13
#calendario 2021A
#Programa de operadores aritméticos con funciones

def main():
    d1=int(input("Dame un numero entero: "))
    d2=int(input("Dame otro numero entero: "))
    Suma(d1, d2)
    Resta(d1, d2)
    Mult(d1, d2)
    Div(d1, d2)
    Div_Int(d1, d2)
    Residuo(d1, d2)
    Expo(d1, d2)
def Suma (d1, d2):
    sum=d1+d2
    print(d1,'+', d2, '=', sum)
def Resta (d1, d2):
    rest=d1-d2
    print(d1,'-', d2, '=', rest)

def Mult (d1, d2):
    mult=d1*d2
    print(d1,'*', d2, '=', mult)

def Div (d1, d2):
    div=d1/d2
    print(d1,'/', d2, '=', div)

def Div_Int (d1, d2):	
    div_Int =d1//d2
    print(d1,'/ /', d2, '=', div_Int)

def Residuo (d1, d2):
    residuo=d1%d2
    print(d1,'%', d2, '=', residuo)

def Expo (d1, d2):
    exp =d1**d2
    print(d1,'**', d2, '=', exp)

main()
	
