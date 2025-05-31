#Lista de palabras.
#todas las palabas son posibles de nuestro juegi.

import random

list_palabras=["amarillo","rojo","violeta"]

#hacer que aleatoriamente seleccione una palabra
palabra_elegida=random.choice(list_palabras)

#testo palabra_elegida="amarillo"

#generar el display
display=[]
for _ in palabra_elegida:
    display+="_"
print(f"La palabra ganadora ya ha sido seleccionada")
print(display)

#el usuario iintrodduce una letra para adivinar la palabra final.
letra_user=input("Adivinar una de las letras: ").lower()

#verificar si la letra del usuario pertenece a una letra de la palabra que se ingrese.

for posicion in range(len(palabra_elegida)):
    if letra_user==palabra_elegida[posicion]:
        display[posicion]=letra_user

print(display)