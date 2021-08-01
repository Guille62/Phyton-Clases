import math

n = int(input("Ingrese el número para el factorial: "))

if n >= 0:
    if (n >0):
        y=math.factorial(n)
        print("El factorial del número",n,"corresponde a", y)
    else:
        print("el factorial de cero es 1")
else:
    print("nose puede calcular el factorial")
