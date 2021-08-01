#Biblioteca MATH ( es un biblioteca propia de phyton raiz cuadrada, pi, etc)

import math

#ENTRADA
print("ingrese los valores para la ecuación")

B = float(input("Ingrese el valor de B: "))
A = float(input("Ingrese el valor de A: "))
C = float(input("Ingrese el valor de C: "))

#PROCESAR
DISCRIMINANTE = ((B**2) - (4*A*C))
print("el discriminante es: ", DISCRIMINANTE)

#FLUJO CONDICIONANTE Y SALIDA

if DISCRIMINANTE >= 0:
    RAIZ1 = ((-B + (math.sqrt(DISCRIMINANTE)))/(2*A))
    RAIZ2 = ((-B - (math.sqrt(DISCRIMINANTE)))/(2*A))
    print("la primera raíz es ", RAIZ1)
    print("la segunda raíz es ", RAIZ2)
else:
    print("Raices complejas")


