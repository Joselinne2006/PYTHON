import random
#Piedra, Papel o Tigera.
print(f"Bienveniddo a su Primer Videojuego\n PIEDRA, PAPEL O TIGERA")
#entrada
#pedir la opcion al ususario
user=input("Dime que jugara?:\n-PIEDRA \n-PAPEL \n-TIGERA \n")


#opcion de la computadora
aleatorio=random.randint(0,2)
op_cpu=["PIEDRA","PAPEL","TIGERA"]
cpu=op_cpu[aleatorio]
print(cpu)

#procesamiento
#comparar casos e imprimir

if(user=="PIEDRA"):
    if(cpu=="PIEDRA"):
        print(f"LA COMPUTADORA JUGÓ {cpu}")
        print("EMPATE")
    elif(cpu=="PAPEL"):
        print(f"LA COMPUTADORA JUGÓ {cpu}")
        print("ANONIMO GANA")
    else:
        print(f"LA COMPUTADORA JUGÓ {cpu}")
        print("USUARIO GANA")
            
        
elif (user=="PAPEL"):
    if(cpu=="PIEDRA"):
        print(f"LA COMPUTADORA JUGÓ {cpu}")
        print("USUARIO GANA")
    elif(cpu=="PAPEL"):
        print(f"LA COMPUTADORA JUGÓ {cpu}")
        print("EMPATE")
    else:
        print(f"LA COMPUTADORA JUGÓ {cpu}")
        print("ANONIMO GANA")
        
else:
    if(cpu=="PIEDRA"):
        print(f"LA COMPUTADORA JUGÓ {cpu}")
        print("ANONIMO GANA")
    elif(cpu=="PAPEL"):
        print(f"LA COMPUTADORA JUGÓ {cpu}")
        print("USUARIO GANA")
    else:
        print(f"LA COMPUTADORA JUGÓ {cpu}")
        print("EMPATE")