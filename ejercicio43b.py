import random

# Gráficos
vidas_graficos = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

list_palabras = ["amarillo", "rojo", "violeta"]

palabra_elegida = random.choice(list_palabras)

display = ["_" for _ in palabra_elegida]
print("La palabra ganadora ya ha sido seleccionada")
print(" ".join(display))

vidas = 6
print(f"Tienes {vidas} vidas")

print(vidas_graficos[vidas])
fin_juego = False 
letras_adivinadas = set()

while not fin_juego:
    letra_user = input("Adivinar una de las letras: ").lower()
    
    if letra_user in letras_adivinadas:
        print("Ya has intentado esa letra. Prueba con otra.")
        continue
    
    letras_adivinadas.add(letra_user)
    
    if letra_user in palabra_elegida:
        for posicion in range(len(palabra_elegida)):
            if letra_user == palabra_elegida[posicion]:
                display[posicion] = letra_user
        print("¡Bien hecho! Has adivinado una letra.")
    else:
        vidas -= 1
        print(f"La letra '{letra_user}' no está en la palabra. Te quedan {vidas} vidas.")
    
    print(vidas_graficos[vidas])
    print(" ".join(display))
    
    if vidas == 0:
        fin_juego = True
        print(f"El juego ha terminado. Has perdido. La palabra era '{palabra_elegida}'.")
    elif "_" not in display:
        fin_juego = True
        print(f"¡Felicidades! Has adivinado la palabra '{palabra_elegida}'.")