#numero par o impar
#pedir el numero
num=input("Ingrese un numero: ")
num=int(num)

#hacer la operacion si el residuo es = 0 entonces es par
if(num%2==0):
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")    