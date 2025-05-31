#Programa que pida edad
#mostrar nuestros dias, semanas meses y años
#vivir 100 años
edad=input("Dime cuantos años tienes: ")
edad=int(edad)
#cuantos años restantes nos quedan

años_res=100-edad

#calcular dias
#años de 365 dias
dias=años_res*365

#calcular semanas
#52 semanas
semanas=años_res*52
#calcular 12 meses
meses=años_res*12

print(f"Hola, te quedan {años_res} años,{meses} meses,{semanas} semanas y {dias} dias")