#91-100 sobresaliente
#81-90 supero las expectativas
#71-80 aceptable
#61-70 de panzazo

puntuajes_alumnos={"Harry":81,
                   "Ron": 78,
                   "Hermione": 99,
                   "Draco": 74,
                   "Dumbledore":62}

rendimientos_alumnos={}

for alumno in puntuajes_alumnos:
    puntuaje=puntuajes_alumnos[alumno]
    if puntuaje>90:
        rendimientos_alumnos[alumno]="Sobresaliente"
    elif puntuaje>80:
        rendimientos_alumnos[alumno]="Supero las expectativas"
    elif puntuaje>70:
        rendimientos_alumnos[alumno]="Aceptable"
    else:
        rendimientos_alumnos[alumno]="Paso de panzazo"

print(rendimientos_alumnos)