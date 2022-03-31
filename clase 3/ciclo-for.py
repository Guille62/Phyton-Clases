n = int(input("inserta un numero "))

y=n
factorial_total = 1
x = 1
for x in range (n):
  factorial_total *= n
  print("Valor de factorial_total", factorial_total)
  x += 1
  n -= 1
print ("El factorial de %d es %d" % (y,factorial_total))
