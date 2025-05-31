#implementacion de modulo random

import random
#generar numeros enteros
#crear, generar un numero aleatorio entre el 1 y el 10

num_aleatorio=random.randint(1,10)
print(num_aleatorio)


#generar decimales
#random.random() ------- 0.00000000 - 0.99999999
aleatorio_flotante=random.random()*10
print(aleatorio_flotante)

#crear, generar un numero aleatorio entre el 0.0 y el 4.99999999
#rango_flot=aleatorio_flotante*5
#print(rango_flot)