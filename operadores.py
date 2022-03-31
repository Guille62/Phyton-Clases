num1 = int(input("Digite un número: "))
num2 = int(input("Digite otro número: "))

if num1%2==0 and num2%2==0:
    print(f"tu número {num1} y tu número {num2} son pares")

elif num1%2!=0 and num2%2==0:
    print(f"tu número {num1} es impar pero tu número {num2} es par")

elif num1%2==0 and num2%2!=0:
    print(f"tu número {num1} es par pero tu número {num2} es impar")    

else:
    print("Tus números son impares")
