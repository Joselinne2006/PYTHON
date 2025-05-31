#Programa que dado un numero A y un numero B
#se convierta las variables de modo que
#A=6 y B=8 y cuando termine las variables esten
#invertidas A=8 y B=6# Definir variable A
A = 6
# Definir variable B
B = 8

print("Valores originales")
print(" a = ", A)
print(" b = ", B)

# INVERTIR
# Variable auxiliar
c = A  # c = 6

# INVERTIR A
A = B  # A = 8

# INVERTIR B
B = c  # B = 6

# Imprimir valores invertidos
print("Valores invertidos")
print(" a = ", A)
print(" b = ", B)
