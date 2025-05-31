#El concepto de las listas: es una agrupacion de elementos ordenados
#si listamos frutas: manzanas, pera,sandia

numeros=[10,9,8,7,6,5,4,3,2,1]
#      =[0,1,2,3,4,5,6,7,8,n]

print(numeros[6])

asistentes=["Ana","Jose","Hilda","Marcos"]
print(asistentes[2])
texto="Hola"


frutas=[]
print(frutas)

frutas.append("Sandia")
print(frutas)

frutas.append("Platano")
print(frutas)


fruta=input("Que fruta quiere añadir a la canasta: ")
frutas.append(fruta)
print(frutas)
