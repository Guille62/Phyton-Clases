nombre= ["Maria", "Juan"]
deporte= ["golf", "tenis"]
frecuencia= ["mucho", "poco"]

i=0
while i<len(nombre):
    print("{0} juega {1}. {0} practica {2}.".format(nombre[i],deporte[i], frecuencia[i]))
    i=i+1
