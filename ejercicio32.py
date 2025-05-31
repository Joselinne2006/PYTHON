#Quiero que la computadora seleccione a la persona siguiente para irse
#VIc Broda
#
#

import random
participantes=["Juan","Julian","Sofia","Amadis"]
num_aleatorio=random.randint(1,4)
print(num_aleatorio)

victima=participantes[num_aleatorio]
print(f"Lo sentimos, {victima} se tiene que ir")

