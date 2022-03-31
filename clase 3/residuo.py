n = int(input("ingrese n:"))
x = [ ] 
i = 0
while i < n:

  num = int(input("ingrese numero:"))
  x.append(num)
  i = i + 1

i = 0
for valor in x:

  if valor < 0:

    x[i] = 0

  i = i + 1

print(x)
