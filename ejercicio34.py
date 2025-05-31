#Somos PIRATAS
#Enterrar un tesoro
#pedir un numero de dos digitos al usuario.
#y esos dijitos son las cordenadas donde se enterrara el tesoro.
#el programa pedira las cordenadas donde se enterrara el tesoro.
#el programa tiene que enterrar el tesoro.

#primero representar el mapa
renglon1=["❏","❏","❏"]
renglon2=["❏","❏","❏"]
renglon3=["❏","❏","❏"]

mapa=[renglon1,
      renglon2,
      renglon3]
print("El mapa para esconder el tesoro luce asi:")
print(f"{renglon1}\n{renglon2}\n{renglon3}\n")

tesoro=input("Donde desea esconder el tesoro? (Dos cifras): ")
#primer digito renglones y el segundo columnas

d1=tesoro[0]
d1=int(d1)
d1-=1

d2=tesoro[1]
d2=int(d2)
d2-=1

#enterrar el tesoro
mapa[d1][d2]="X"

print(f"{renglon1}\n{renglon2}\n{renglon3}\n")



