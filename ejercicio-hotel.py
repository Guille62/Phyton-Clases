# En un hotel a los pasajeros que ingresan se les asigna un codigo  que corresponde a un número
# con exactamente 16 cifras. El significado de estas cifras es:

# - Los 8 primeros dígitos corresponden a la fecha de ingreso (aaaammdd)
# - Los siguientes 2 dígitos representan el número de noches de estadía
# - Los siguientes 3 dígitos, corresponde  al número de la habitación que ha ocupado
# - El siguiente dígito corresponde al tipo de servicios que incluye su estadía (1: solo desayuno, 2: todo incluído
#   en alimentación y otros: piscina, spa, tours, espectáculos).
# - Los últimos 2 dígitos corresponden al número de veces que se ha alojado en el hotel.

# Por ejemplo, si un código corresponde a 2006110813201203, significa que:
# El pasajero ingresó el 8 de noviembre del 2006, se quedó 13 noches, ocupó la habitación 201,
# contrató al tipo de servicio todo incluído y es tercera vez que aloja en el hotel.

# Para calcular el monto que debe cancelar el pasajero por la actual estadía se deben aplicar los
# siguientes criterios en conjunto:

# - El precio base por la estadía de 1 noche es de $70.000
# - Las habitaciones con número par tienen vista al lago. Por este motivo su precio base aumenta 10%.
# - Si el tipo de estadía es todo incluido, el precio base incrementa en un 15%
# - Si el periodo en el que ingresa el pasajero está en el rango de fechas desde el 20 de diciembre al
#   5 de marzo (ambas fechas incluidas), o entre el 10 de septiembre al 20 de septiembre (ambas fechas incluidas)
#   se considera temporada alta. Si el perido de ingreso es en cualquier otra fecha, se considera temporada baja.
#   En el caso de temporada alta, el precio base se aumenta  en un 20% la estadía del pasajero.
# - Si el pasajero ha alojado antes en el hotel, entonces se le aplica un descuento de un 3% por cada vez sobre
#   el precio base.

# SE PIDE: Escriba un código fuente en phyton que reciba el código de un pasajero, y que imprima por
#                pantalla la siguiente información.


#  Fecha de ingreso: ( en formato dd-mm-aaaa)
#  Tipo de estadia:
#  Tiempo de estadía:
#  Número de habitación:
#  Número de veces que ha alojado:
#  Valor de estadía completa:

"""
EJEMPLO 1:
ingresa el código de pasajero: 2020091807122202
Fecha de ingreso: 18-9-2020
tipo de estadía: 2
tiempo de estadía: 7
Número de habitación: 122
Número de veces que ha alojado: 2
Valor de estadía completa: $ 681100

EJEMPLO 2:
ingresa el código de pasajero: 2020030810301100
Fecha de ingreso: 8-3-2020
tipo de estadía: 1
tiempo de estadía: 10
Número de habitación: 301
Número de veces que ha alojado: 0
Valor de estadía completa: $ 700000

"""
codigo = int(input('Ingrese el código de pasajero: '))

año = codigo//1000000000000
codigo = codigo%1000000000000

mes = codigo//10000000000
codigo = codigo%10000000000

dia = codigo//100000000
codigo = codigo%100000000

numDiasEstadia = codigo//1000000
codigo = codigo%1000000

numHabitacion = codigo//1000
codigo = codigo%1000

tipoEstadia = codigo//100
codigo = codigo%100

numVecesAlojado = codigo

base = 70000
montoAPagar = base

if numHabitacion%2 == 0:
    montoAPagar = montoAPagar + base*0.1
    
if tipoEstadia == 2:
    montoAPagar = montoAPagar + base*0.15

if mes == 1 or mes == 2 or  (mes == 3 and 1  <= dia <= 5) or \
   (mes == 9 and 10 <= 20) or (mes == 12 and 20 <= dia <= 31):
    montoAPagar = montoAPagar + base*0.2

if numVecesAlojado > 0:
    montoAPagar = montoAPagar - base*(0.03*numVecesAlojado)

montoAPagar = montoAPagar*numDiasEstadia


print('Fecha de ingreso:  ', str(dia)+ '-' + str(mes) + '-' + str(año))
print('Tipo de Estadia: ', tipoEstadia)
print('Tiempo de Estadía: ', numDiasEstadia)
print('Número de Habitación: ', numHabitacion)
print('Número de veces alojado: ', numVecesAlojado)
print('Valor de estadía completa: $', int(montoAPagar))

