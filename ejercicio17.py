# Calcular propinas
# Según la cantidad de personas que comieron
# El programa indicará a cada persona cuánto tiene que dejar de propina
# Se puede dejar un 10%, 12% o 15% de propina

# Primero las entradas
comensales = int(input("Dime cuántas personas comieron: "))

cuenta = float(input("¿De cuánto fue su cuenta?: "))

propina = int(input("¿Cuánto desea dejar de propina, 10%, 12% o 15%?: "))

# Verificación de la entrada de propina
if propina not in [10, 12, 15]:
    print("Error: Por favor, ingrese un porcentaje de propina válido (10%, 12% o 15%).")
else:
    # Cuenta total incluyendo propina
    if propina == 10:
        cuenta_total = cuenta * 1.10
    elif propina == 12:
        cuenta_total = cuenta * 1.12
    elif propina == 15:
        cuenta_total = cuenta * 1.15

    # Cuánto debe aportar cada comensal
    cantidad_por_persona = cuenta_total / comensales
    cantidad_por_persona = round(cantidad_por_persona, 2)

    # Mostrar la cuenta total y el monto por persona
    print(f"La cuenta total es de ${cuenta_total:.2f}, incluyendo una propina del {propina}%.")
    print(f"Dado que comieron {comensales} personas, cada uno debe aportar: ${cantidad_por_persona:.2f}")

