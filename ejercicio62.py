# Importaciones

MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18
        },
        "costo": 15
    },
    "latte": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
            "leche": 150
        },
        "costo": 25
    },
    "capuchino": {
        "ingredientes": {
            "agua": 250,
            "cafe": 100,
            "leche": 24
        },
        "costo": 30
    }
}

recursos = {
    "agua": 300,
    "cafe": 200,
    "leche": 100
}

ganancias = 0

# Funciones
def hay_recursos_suficientes(ingredientes_orden):
    for elemento in ingredientes_orden:
        if ingredientes_orden[elemento] > recursos[elemento]:
            print(f"Lo siento, no hay suficiente {elemento}.")
            return False
    return True

def procesar_monedas():
    total = 0
    total += int(input("Dime cuántas monedas de $1 vas a utilizar: ")) * 1
    total += int(input("Dime cuántas monedas de $5 vas a utilizar: ")) * 5
    total += int(input("Dime cuántas monedas de $10 vas a utilizar: ")) * 10
    total += int(input("Dime cuántas monedas de $20 vas a utilizar: ")) * 20
    return total

def transaccion_completada(dinero_recibido, costo_de_la_bebida):
    global ganancias
    if dinero_recibido >= costo_de_la_bebida:
        cambio = dinero_recibido - costo_de_la_bebida
        print(f"Tu cambio es: $ {cambio}")
        ganancias += costo_de_la_bebida  # Solo se suman las ganancias del costo de la bebida
        return True
    else:
        print("Lo siento, no es suficiente dinero, te voy a devolver el monto.")
        return False 

def hacer_cafe(nombre_bebida, ingredientes_orden):
    for elemento in ingredientes_orden:
        recursos[elemento] -= ingredientes_orden[elemento]
    print(f"Aquí está tu bebida {nombre_bebida}.")

# Ejecución del código
maquina_encendida = True

while maquina_encendida:
    seleccion = input("Hola, ¿Qué tipo de café te puedo servir? (Espresso, Latte, Capuchino) ").lower()
    
    if seleccion == "apagar":
        maquina_encendida = False
        
    elif seleccion == "reporte":
        print(f"Agua: {recursos['agua']} ml")
        print(f"Café: {recursos['cafe']} g")
        print(f"Leche: {recursos['leche']} ml")
        print(f"Ganancias: ${ganancias}")
        
    else:
        bebida = MENU.get(seleccion)
        if bebida and hay_recursos_suficientes(bebida['ingredientes']):
            print(f"La bebida cuesta ${bebida['costo']}.")
            pago = procesar_monedas()
            if transaccion_completada(pago, bebida['costo']):
                hacer_cafe(seleccion, bebida['ingredientes'])