print("===CALCULADORA===")
print("Elige una opción")
print("1-Suma")
print("2-Resta")
print("3-Multiplicación")
print("4-División")

y=int(input("Escribe tu elección: "))


if(y==1):

  a=input("Introduce el primer numero\n")
  b=input("Introduce el segundo numero\n")

  a2=float(a)
  b2=float(b)

  resultado= a2+b2
  resultado_round = round(resultado,1)

  print("El resultado de la suma es:",resultado_round)

elif(y==2):

  a=input("Introduce el primer numero\n")
  b=input("Introduce el segundo numero\n")

  a2=float(a)
  b2=float(b)

  resultado= a2-b2
  resultado_round = round(resultado,1)
  
  print("El resultado de la resta es:",resultado_round)

elif(y==3):

  a=input("Introduce el primer numero\n")
  b=input("Introduce el segundo numero\n")

  a2=float(a)
  b2=float(b)

  resultado= a2*b2
  resultado_round = round(resultado,1)
   
  print("El resultado de la multiplicación es:",resultado_round)

elif(y==4):

  a=input("Introduce el primer numero\n")
  b=input("Introduce el segundo numero\n")

  a2=float(a)
  b2=float(b)

  resultado= a2/b2
  resultado_round = round(resultado,1)
   
  print("El resultado de la división es:",resultado_round)

else:

  print("NUMERO INVALIDO")
