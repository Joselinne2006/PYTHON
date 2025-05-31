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
print("Su IMC equivale a:", imc)
