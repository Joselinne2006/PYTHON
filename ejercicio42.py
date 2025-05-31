#generador de contraseñas
#Pedir al usuario la cantidad de letras, numeros, simbolos

import random


letras=["a","b","c","d","e","f","g","h","i","j"]
numeros=["1","2","3","4","5","6"]
simbolos=["!",'"',"#","$","%"]

contraseña=""

cantL=int(input("Cuantas letras: "))
cantN=int(input("Cuantos numeros: "))
cantS=int(input("Cuantos simbolos: "))

for i in range(0,cantL):
    letra_aleatoria=random.choice(letras)
    contraseña+=letra_aleatoria
for i in range(0,cantN):
    num_aleatoria=random.choice(numeros)
    contraseña+=num_aleatoria
for i in range(0,cantS):
    sim_aleatoria=random.choice(simbolos)
    contraseña+=sim_aleatoria

print(contraseña)