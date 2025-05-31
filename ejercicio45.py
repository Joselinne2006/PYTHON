import math

def calcular_pintura(alto, ancho, cobertura):
    # Área a pintar
    area_pintar = alto * ancho
    # Cantidad de latas
    latas_necesarias = area_pintar / cobertura
    # math.ceil sirve para redondear 
    latas_necesarias = math.ceil(latas_necesarias)
    # Imprimir datos
    print(f"Se requieren {latas_necesarias} latas.")

alto = input("¿Cuánto mide de alto la pared en metros? ")
alto = float(alto)
ancho = input("¿Cuánto mide de ancho la pared en metros? ")
ancho = float(ancho)
cobertura = input("¿Cuántos metros cuadrados cubre la pintura? ")
cobertura = float(cobertura)

calcular_pintura(alto, ancho, cobertura)