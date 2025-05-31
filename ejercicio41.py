#programa que pida al usuario un numero entre el 1 y el 100
#apartir del numero dado que imprima los numeros pares que
#continuan hasta el 1000

numero=int(input("Introduce el numero entre el 1 y el 1000: "))

for i in range(numero,1001):
    par=i%2
    if(par==0):
        print(i)