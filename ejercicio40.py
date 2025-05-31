#programa que calcule pormedio de estaturas de un grupo dado

#definir lista
#altura_es=[70,65,89,100,60,45,38]

puntuaje_est=input("Dame los puntuajes separados por una coma: ").split(",")

suma=0
maximo=0

for i in range(0,len(puntuaje_est)):
    pun_estu=puntuaje_est[i]
    pun_estu=int(pun_estu)
    suma+=pun_estu
    
    if(pun_estu>maximo):
        maximo=pun_estu

promedio=suma/len(puntuaje_est)
promedio=round(promedio,2)
print(f"El promedio en estaturas de los alumnos es {promedio}")
print(f"El puntuaje maximo es {maximo}")    

