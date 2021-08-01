#SEXTO PROGRAMA
#SEGUIMOS TRABAJANDO CON EL NÚMERO AL CUADRADO

n = float(input("Ingrese su número por favor "))# al ser el valor ingresado un flotante
nombre = str(input("Ingrese su nombre por favor "))
#Procesamiento

cuadrado = n * n #la variable que usa el elemento flotante anterior adquiere la propiedad flotante también
cuadrado_decimal = round(cuadrado,1)
#Salida
print("Estimado(a) {0} el cuadrado del número {1} corresponde a {2}".format(nombre,n,cuadrado_decimal))
