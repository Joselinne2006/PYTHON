import random
print("""
     _       _ _       _                    _   _   _                                
    / \   __| (_)_   _(_)_ __   __ _    ___| | | \ | |_   _ _ __ ___   ___ _ __ ___  
   / _ \ / _` | \ \ / / | '_ \ / _` |  / _ \ | |  \| | | | | '_ ` _ \ / _ \ '__/ _ \ 
  / ___ \ (_| | |\ V /| | | | | (_| | |  __/ | | |\  | |_| | | | | | |  __/ | | (_) |
 /_/   \_\__,_|_| \_/ |_|_| |_|\__,_|  \___|_| |_| \_|\__,_|_| |_| |_|\___|_|  \___/ 
                                                                                     
 """)
def establecer_dificultad():
    dificultad = input("Selecciona una dificultad, Facil o Dificil: ").lower()
    return 10 if dificultad == "facil" else 5

def verificar_respuesta(usuario, solucion, intentos):
    if usuario > solucion:
        print("Tu numero es mayor que la solucion")
    elif usuario < solucion:
        print("Tu numero es menor que la solucion")
    else:
        print(f"Felicidades, adivinaste el numero {solucion} en el que pense")
    return intentos - 1

def videojuego():
    print("Bienvenido al videojuego de leer mentes")
    print("Voy a pensar en un numero entre el 1 al 100")

    solucion = random.randint(1, 100)
    print(f"secreto, la solucion es: {solucion}")

    intentos = establecer_dificultad()
    print(f"Tienes {intentos} intentos disponibles para adivinar el numero")

    while intentos > 0:
        usuario = int(input("En que numero crees que estoy pensando? "))
        intentos = verificar_respuesta(usuario, solucion, intentos)
        
        if usuario == solucion:
            return
        elif intentos > 0:
            print("Intente de nuevo")
        else:
            print("Lo siento, ya no te quedan intentos")

videojuego()





