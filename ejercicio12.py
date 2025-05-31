#pedir nombre
nombre=input("Dime tu primer nombre: ")
#calcular la longitud
longitud_nombre=len(nombre)
#imprimir todo concatenando
print("Te llamas", nombre," y tu nombre tiene ", longitud_nombre," letras")

#existe type
tipo_nombre=type(nombre)
print(tipo_nombre)

tipo_longitud_nombre=type(longitud_nombre)

print(tipo_longitud_nombre)
