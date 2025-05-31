import random

graficos=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
   """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""       ]

#Piedra, Papel o Tigera.
print(f"Bienveniddo a su Primer Videojuego\n PIEDRA, PAPEL O TIGERA")
#entrada
#pedir la opcion al ususario
user=input("Dime que jugara?:\n1. PIEDRA \n2. PAPEL \n3. TIGERA \n")

#convertir entrada a termino computacional

if(user=="PIEDRA"):
    user=0
elif(user=="PAPEL"):
    user=1
elif(user=="TIGERA"):
    user=2

print(f"EL USUARIO JUGÓ {graficos[user]}")

#opcion de la computadora
cpu=random.randint(0,2)

op_cpu=["PIEDRA","PAPEL","TIGERA"]

print(f"LA COMPUTADORA JUGÓ {graficos[cpu]}")

if (user==0 and cpu==2):
    print("El usuario gana")
elif (user==2 and cpu==0):
    print("La computadora gana")
if(user>cpu):
    print("El usuario gana")
elif (cpu>user):
    print("La computadora gana")
else:
    print("EMPATE")
