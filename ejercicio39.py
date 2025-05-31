#programa que calcule pormedio de estaturas de un grupo dado

#definir lista
altura_es=[1.50,1.68,1.75,1.90,1.69]

suma=0

for estudiante in altura_es:
    suma+=estudiante
    
promedio=suma/len(altura_es)
print(f"El promedio en estaturas de los alumnos es {promedio}")
    
    
    