#estamos en una montaña rusa
#hay un cartel
#si tu estatura es <120 cm puedes pasar
#si tienes menos de 12 pagas $3 pesos
#si tienes menos de 18 pagas $3 pesos
#si tienes mas de 18 pagas $15 pesos


altura=input("Cual es su estatura: ")
altura=int(altura)


if(altura>=120):
    print("diviertete!")
    
    edad=input("Cual es su edad: ")
    edad=int(edad)
    
    if(edad<=12):
            print("Va a pagar $3.00 extras!")
    elif(edad<18):
            print("Va a pagar $7.00 extras!")
    elif(edad>=18):
            print("Va a pagar $15.00 extras!")

else:
    print("No puede subir")