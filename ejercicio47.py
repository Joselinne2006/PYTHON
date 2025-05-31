# Encripte y desencripte según el cifrado César
alfabeto = [
    " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

def cifrado(texto, giro):
    encriptado = ""
    print(f"El texto a encriptar es {texto}")
    for i in range(len(texto)):
        if texto[i] == "": 
            encriptado += " "
        else:
            indice_en_alfabeto = alfabeto.index(texto[i])
            
            
            nuevo_indice = (indice_en_alfabeto + giro) % len(alfabeto)
            encriptado += alfabeto[nuevo_indice]
    
    print(f"El texto encriptado es {encriptado}")

texto = "joselinne angeles"
giro = 3

cifrado(texto, giro)