#programa que diga si el año es biciesto o no.

#como decirle a la computadora que haga algo.

#que la computadora calule si es biciesto o no.
# Solicita al usuario que ingrese un año
año = input("Dime el año que quieres calcular: ")
año = int(año)  # Convierte la entrada a un entero

# Calcula el residuo al dividir el año entre 4
residuo = año % 4

# Verifica si el año es divisible entre 4
if residuo == 0:
    # Es divisible entre 4, ahora verifica si es divisible entre 100
    residuo = año % 100
    
    # Verifica si el año es divisible entre 100
    if residuo == 0:
        # Es divisible entre 100, ahora verifica si es divisible entre 400
        residuo = año % 400
        
        # Verifica si el año es divisible entre 400
        if residuo == 0:
            # El año es divisible entre 400, por lo tanto es bisiesto
            print("El año es bisiesto")
        else:
            # El año es divisible entre 100 pero no entre 400, por lo tanto no es bisiesto
            print("El año no es bisiesto")
    else:
        # El año es divisible entre 4 pero no entre 100, por lo tanto es bisiesto
        print("El año es bisiesto")
else:
    # El año no es divisible entre 4, por lo tanto no es bisiesto
    print("El año no es bisiesto")
