"""
#ambitos locales
def incrementar_enemigos():
    enemigos=2
    print(f"La funcion incrementar_enemigos tiene {enemigos} enemigos")

#ejecucion principal del codigo
#definimos el ambito local
enemigos=1

incrementar_enemigos()
print(f"enemigos globales tiene {enemigos} enemigos")


def beber_porcion():
    salud_jugador=100
    fuerza_de_la_pocion=2
    return salud_jugador
     
beber_porcion()
print(beber_porcion())


nivel_juego=3
enemigos=["Esqueleto","Zombie","Alien"]


if(nivel_juego<5):
    nuevo_enemigo=enemigos[0]
    
print(nuevo_enemigo)

enemigos=1
def incrementar_enemigos():
    global enemigos
    enemigos+=1
    print(f"La funcion incrementar_enemigos tiene {enemigos} enemigos")

incrementar_enemigos()
print(f"enemigos globales tiene {enemigos} enemigos")

PI=3.1416
"""
