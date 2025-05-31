#tipos de datos
    #datos enteros ---- no tienen propiedad leng
    #(-inf, +inf) ----- fracciones, racionales, decimales
x=49593953

    #Datos flotantes ---- tampoco tienen propiedades leng
    #son aquellos que involucran a los racionales,decimales
    #y=0.3
    #z=1/4
    
    #datos de tipo booleanos
    #si ---- o no , True false -----1,0
    
    #datos de tipo string
nombre = "Joselinne"  # Los strings deben estar entre comillas
print(nombre[2])  # [] ---- operador de indexamiento

# length es para identificar la cantidad de letras que tiene
# un string determinado
# solo se les puede aplicar len a los strings
longitud_nombre = len(nombre)
print(longitud_nombre)

numero_x = 1342645295674390
# Los números no tienen una función len, por lo que se debe convertir a string primero
longitud_numero = len(str(numero_x))
print(longitud_numero)


