def mi_funcion():
    return 3*2


#variable receptora =mi_funcion
variable_receptira=mi_funcion()

def formatear_nombre(primer_nombre,primer_apellido):
    primer_nombre=primer_nombre.title()
    primer_apellido=primer_apellido.title()
    #print(f"Tu nombre es {primer_nombre} {primer_apellido}")
    return primer_nombre,primer_apellido


nombre=input("Dame tu primer nombre: ")
apellido=input("Dame tu primer apellido: ")
formatear_nombre(nombre,apellido)
    
primer_nombre_formateado,primer_apellido_formateado=formatear_nombre(nombre,apellido)
    