#calculadora que reste, sume, multiplique y divida.

#sumaa
def suma(n1,n2):
    return n1+n2
#restaa
def resta(n1,n2):
    return n1-n2
#multiplicación
def multiplicacion(n1,n2):
    return n1*n2
#división
def division(n1,n2):
    return n1/n2

operaciones={
    "+":suma,
    "-":resta,
    "*":multiplicacion,
    "/":division
    }
num1=input("Introduce el primer numero: ")
num1=int(num1)
num2=input("Introduce el segundo numero: ")
num2=int(num2)

for simbolo in operaciones:
    print(simbolo)
    
simbolo_seleccionado=input("Indique la operacion a realizar: ")
calculadora=operaciones[simbolo_seleccionado]
resultado=calculadora(num1,num2)

print(f"{num1} {simbolo_seleccionado} {num2} = {resultado}")