import random
import os

graficos = ["""
 _ __ ___   __ _ _   _  ___  _ __    ___    _ __ ___   ___ _ __   ___  _ __ 
| '_ ` _ \\ / _` | | | |/ _ \\| '__|  / _ \\  | '_ ` _ \\ / _ \\ '_ \\ / _ \\| '__|
| | | | | | (_| | |_| | (_) | |    | (_) | | | | | | |  __/ | | | (_) | |   
|_| |_| |_|\\__,_|\\__, |\\___/|_|     \\___/  |_| |_| |_|\\___|_| |_|\\___/|_|   
                 |___/                                  
""",
           """
           
__   _____ 
\\ \\ / / __|
 \\ V /\\__ \\
  \\_/ |___/
           
"""]

# Datos de comparación
datos = [
    {
        "nombre": "Instagram",
        "contador_seguidores": 346,
        "descripcion": "Plataforma de contenido social",  
        "pais": "Estados Unidos"                        
    },
    {
        "nombre": "Cristiano Ronaldo",
        "contador_seguidores": 183,
        "descripcion": "Jugador profesional de futbol",  
        "pais": "Portugal"                              
    },
    {
        "nombre": "Jeon Jung Kook",
        "contador_seguidores": 1830,
        "descripcion": "Cantante Profesional",          
        "pais": "Corea del Sur"                         
    },
    {
        "nombre": "Kim Soo Hyun",
        "contador_seguidores": 143,
        "descripcion": "Actor y Cantante Profesional",   
        "pais": "Corea del Sur"                         
    }
]

# Funciones

# Generar un objeto aleatorio a partir de los datos.
def obtener_objetos_aleatorios():
    objeto_a = random.choice(datos)
    objeto_b = random.choice(datos)
    while objeto_a == objeto_b:
        objeto_b = random.choice(datos)
    return objeto_a, objeto_b

# Formatear todos los datos de modo que pueda ser utilizado para la función print
def formato_datos(objeto):
    objeto_nombre = objeto["nombre"]
    objeto_descripcion = objeto["descripcion"]  
    objeto_pais = objeto["pais"]                
    return f"{objeto_nombre} es {objeto_descripcion}, que proviene de {objeto_pais}"

def revisar_respuesta(usuario, seguidores_a, seguidores_b):
    if seguidores_a > seguidores_b:
        return usuario == 'a'
    else:
        return usuario == 'b'

# Definición del puntaje
score = 0
continuar_juego = True

print(graficos[0])  # Imprimir el primer gráfico

while continuar_juego:
    os.system("cls" if os.name == 'nt' else 'clear')  # Limpiar la consola
    
    # Obtener objetos aleatorios para comparar
    objeto_a, objeto_b = obtener_objetos_aleatorios()

    # Información a comparar
    print(f"Comparar A: {formato_datos(objeto_a)}")
    print(graficos[1])  # Imprimir el segundo gráfico
    print(f"Comparar B: {formato_datos(objeto_b)}")

    # Preguntar al usuario qué es lo que piensa
    usuario = input("¿Cuál tiene más seguidores? Escriba A o B: ").lower()

    # Verificar si el usuario está correcto.
    objeto_a_contador_seguidores = objeto_a["contador_seguidores"]
    objeto_b_contador_seguidores = objeto_b["contador_seguidores"]

    # Comprobar si el usuario tiene una respuesta correcta.
    respuesta_correcta = revisar_respuesta(usuario, objeto_a_contador_seguidores, objeto_b_contador_seguidores)

    # Decirle si ha acertado o no
    if respuesta_correcta:
        score += 1
        print(f"¡Has acertado! Tu puntaje es {score}.")
    else:
        continuar_juego = False 
        print(f"Lo siento, eso no es correcto. Tu puntaje final es {score}.")

