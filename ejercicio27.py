#programa que sea una calculadora de amor
#funcionamiento
#ingresar 2 nombres
#cuantas letras coinciden en los nombres
#con respecto a la frase "true love"


#si el puntuaje es menor a 10 o mayor a 10
#son tan compatibles como la coca cola y los mentos.

#si el puntiaje esta entre 40 y 50, entonces lucen
#compatibles

#en cualquier otro caso los astros no son claros.

# Solicita nombres de novio y novia
# Solicita los nombres del novio y la novia
el = input("Nombre del novio: ")
el = el.lower()
ella = input("Nombre de la novia: ")
ella = ella.lower()

nombres = el

t1 = nombres.count("l")
r1 = nombres.count("o")
u1 = nombres.count("v")
e1 = nombres.count("e")

l1 = nombres.count("l")
o1 = nombres.count("o")
v1 = nombres.count("v")
e1 = nombres.count("e")

primer_digito = t1 + r1 + u1 + e1 + l1 + o1 + v1 + e1

nom = ella

t2 = nom.count("l")
r2 = nom.count("o")
u2 = nom.count("v")
e2 = nom.count("e")

l2 = nom.count("l")
o2 = nom.count("o")
v2 = nom.count("v")
e2 = nom.count("e")

segundo_digito = t2 + r2 + u2 + e2 + l2 + o2 + v2 + e2

puntuaje = primer_digito + segundo_digito

if puntuaje < 10 or puntuaje > 90:
    print("Tan compatibles como la coca cola y los mentos")
elif puntuaje >= 40 and puntuaje <= 50:
    print("Lucen compatibles")
else:
    print("Los astros no son claros")

