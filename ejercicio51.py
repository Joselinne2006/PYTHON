
#subastas
from os import system

total_apuestas = {}

def hallar_mas_caro(total_apuestas):
    maximo = 0
    ganador = ""
    for apostante in total_apuestas:
        monto = int(total_apuestas[apostante])  # Convertir a entero
        if monto > maximo:
            maximo = monto
            ganador = apostante
    print(f"El ganador es {ganador} con una apuesta de {maximo}")

def subasta_en_accion():
    subasta_terminada = False

    while not subasta_terminada:
        nombre = input("Cómo te llamas? ")
        apuesta = input("Cuanto vas a aumentar la puja? ")

        total_apuestas[nombre] = apuesta

        #Añadir a alguien mas
        alguien_mas = input("Hay otros apostantes? Si o No: ").lower()
        
        if alguien_mas == "no":
            subasta_terminada = True
        elif alguien_mas == "si":
            system("cls")

subasta_en_accion()
hallar_mas_caro(total_apuestas)  
        
        
