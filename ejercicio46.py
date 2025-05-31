#determinar si un numero es parimo o no

def primo_no(numero):
    for i in range(2,numero):
        if(numero%i)==0:
            print("El numero no es primo")
            break
        else:
            print("El numero es primo")
            break

primo_no(67)