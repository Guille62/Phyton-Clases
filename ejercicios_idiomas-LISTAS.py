preguntas =[
    "Cual es  su nombre: ",
    "What's your name: ",
    "Qual é o seu nome: ",
    "Quel est votre nom: "
    ]

saludos=[
    "Hola %s !",
    "Hello %s !",
    "Olá %s !",
    "Bonjour %s !"
    ]

print("0: Esp")
print("1: Eng")
print("2: Pt")
print("3: Fr")

lenguajes =int(input("(0,1,2,3): "))

nombre=input(preguntas[lenguajes])
print(saludos[lenguajes] % nombre)
