# Construye un programa en Python que calcule y muestre por pantalla la raíz cúbica de un número entero
# ingresado por el usuario. El resultado deberá estar redondeado a 2 decimales.
import math

num = int(input("Ingrese su número: "))

cubo = num**(1/3)

redondeado = round(num**(1/3), 2)

print(redondeado)
