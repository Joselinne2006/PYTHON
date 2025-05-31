#pizza pequeña 15
#mediana 20
#grande 25
#preguntar si va con pepperoni si es si es $2.00 extras
#preguntar si va con extra queso si es si es $1.00
#mostrar el total a pagar.

print("CH ----- $15.00")
print("M ----- $20.00")
print("G ----- $25.00")
pizza=input("Hola, que tipo de Pizza desea? ")

if(pizza=="CH"):
    pr=15.00
elif (pizza=="M"):
    pr=20.00
elif(pizza=="G"):
    pr=25.00

pepperoni=input("Desea agregar Pepperoni? (SI/NO)")
if(pepperoni=="SI"):
    pr_extra=2.00
else:
    pr_extra=0

queso=input("Desea agregar Queso? (SI/NO)")
if(queso=="SI"):
    que_extra=1.00
else:
    que_extra=0

total=pr+pr_extra+que_extra
print(f"El costo total de su pizza es de: {total}")
