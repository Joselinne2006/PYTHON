# Estamos en una montaña rusa
# Hay un cartel
# Si tu estatura es <120 cm puedes pasar
# Si tienes menos de 12 pagas $3 pesos
# Si tienes menos de 18 pagas $7 pesos
# Si tienes más de 18 pagas $15 pesos

# Hay que preguntar si quiere una foto o no.

# Solicita al usuario la estatura
altura = input("¿Cuál es su estatura en cm? ")
altura = int(altura)

# Verifica si la estatura es suficiente para subir
if altura >= 120:
    print("¡Diviértete!")

    # Solicita al usuario la edad
    edad = input("¿Cuál es su edad? ")
    edad = int(edad)

    # Determina el precio según la edad
    if edad <= 12:
        precio = 3.00
        print(f"Va a pagar ${precio} por el ticket.")
    elif edad < 18:
        precio = 7.00
        print(f"Va a pagar ${precio} por el ticket.")
    else:  # edad >= 18
        precio = 15.00
        print(f"Va a pagar ${precio} por el ticket.")

    # Pregunta si quiere una foto
    foto = input("¿Desea una foto? (si/no) ")    
    if foto == "si":
        precio_foto = 3
        print(f"La foto tiene un costo de ${precio_foto}.")
    else:
        precio_foto = 0
    
    # Calcula el precio total
    precio_total = precio + precio_foto
    print(f"El precio total de la cuenta es: ${precio_total}")
else:
    print("No puede subir")
