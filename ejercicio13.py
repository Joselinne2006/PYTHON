numero = input("Dame un número de 2 dígitos: ")
# sacar el primer dígito
num_d1 = numero[0]
num_d1 = int(num_d1)
print(type(num_d1))  # Debería mostrar <class 'int'> para verificar que la conversión fue exitosa

# sacar el segundo dígito
num_d2 = numero[1]
num_d2 = int(num_d2)
print(type(num_d2))  # Debería mostrar <class 'int'> para verificar que la conversión fue exitosa

# sumar ambos dígitos
suma = num_d1 + num_d2
print(suma)
