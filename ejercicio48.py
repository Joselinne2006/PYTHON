# Encripte y desencripte según el cifrado César

alfabeto = [
    " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

def cifrado_encriptado(texto, giro):
    encriptado = ""
    print(f"El texto a encriptar es: {texto}")
    for letra in texto:
        if letra == " ": 
            encriptado += " "
        else:
            indice_en_alfabeto = alfabeto.index(letra)
            nuevo_indice = (indice_en_alfabeto + giro) % len(alfabeto)
            encriptado += alfabeto[nuevo_indice]

    print(f"El texto encriptado es: {encriptado}")
    return encriptado

def cifrado_desencriptado(texto, giro):
    desencriptado = ""
    print(f"El texto a desencriptar es: {texto}")
    for letra in texto:
        if letra == " ":
            desencriptado += " "
        else:
            indice_en_alfabeto = alfabeto.index(letra)
            nuevo_indice = (indice_en_alfabeto - giro) % len(alfabeto)
            desencriptado += alfabeto[nuevo_indice]
    
    print(f"El texto desencriptado es: {desencriptado}")
    return desencriptado

# Ejecución del código principal
texto_original = "civilizacion es bonita"
giro = 4  

texto_encriptado = cifrado_encriptado(texto_original, giro)
cifrado_desencriptado(texto_encriptado, giro)