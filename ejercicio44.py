def saludo():
    print("Hola")
    print("¿Cómo estas?")
    print("El clima está bien")

saludo()
#incluye argumentos
#def mi_funcion(argumento):
    #haz esto (con el argumento)
    #luego haz esto
    #finalmente haz esto
    
def saludo_con_nombre(nombre):
    print(f"Hola {nombre}")
    print(f"¿Cómo estas {nombre}?")
    print("El clima está bien")
    
saludo_con_nombre("Yoss")
    
#funcion con 3 argumentos
def saludo_con(nombre,ubicacion):
    print(f"Hola {nombre}")
    print(f"¿Cómo está el clima en {ubicacion}?")
    
saludo_con("Jeon","Seul")

#def mi_funcion(a,b,c):
    #haz  esto con a
    #luego esto con b
    #finalmente esto con c

def ejemplo(a,b,c):
    print(a)
    print(b)
    print(c)
ejemplo(c=1,b=2,a=3)

    