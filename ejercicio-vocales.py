# Hacer programa que pida un caracter e indique si es una vocal o no

caracter = input("Ingrese un caracter: ")


if caracter  in "aeiou":
    print(f"tu caracter es la vocal {caracter}")
else:
    print("tu caracter es una letra")
