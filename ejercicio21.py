#Programa que calcule el IMC
print("Bienvenido, es un programa que calcula el IMC")

peso = input("Ingrese su peso en kilos: ")
peso = float(peso)  # Convierte el peso a float para manejar decimales

altura = input("Ingrese su altura en cm: ")
altura = float(altura)  # Convierte la altura a float para manejar decimales

# Convertir altura de cm a metros
altura_metros = altura / 100

# Calcular el IMC
imc = peso / (altura_metros ** 2)

#redondear el numero
imc=round(imc,1)

if imc < 18.5:
    print(f"Tu IMC es de: {imc}, estás en bajo peso")
elif imc < 25:
    print(f"Tu IMC es de: {imc}, estás en peso normal")
elif imc < 30:
    print(f"Tu IMC es de: {imc}, estás en sobrepeso")
else:
    print(f"Tu IMC es de: {imc}, estás en obesidad")
