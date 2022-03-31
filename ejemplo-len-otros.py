coleccion = [1,2,3,4,5,6,7,8]

print(coleccion)
longitud = len(coleccion)

print("el valor de len(coleccion)", len(coleccion))
print("-------------------------------------------")

print("La  longitud de la colección es: ", coleccion[longitud-1])#muestra  el  último elemento de la lista
print("La  longitud de la colección es: ", coleccion[-1])#muestra  el  último elemento de la lista escrito de manera mas corta

print("Los números pares son: ", coleccion[1::2])# Parte en 1( posición 0 ) luego se mueve de 2 en 2

print("Lo números impares son: ", coleccion[::2] )#Parte omitiendo el 0 y el 1 

print("los  elementos centro son: ", coleccion[3:5])# los números centro debería ser 4 y 5 (123-4-5-678)

for n in coleccion: #  el FOR es  un ciclo y hacemos que todo quede en una misma linea
    i=coleccion.index(n)
    print("coleccion[%d]" %i, n, sep=" ", end=" : " ) # el SEP agrega un espacio en blanco / el END agrega : entre cifra y cifra
