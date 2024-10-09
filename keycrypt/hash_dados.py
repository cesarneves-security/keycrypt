import random
import string
from caracters import caract_incript
def calcular_deslocamento(chave):
    deslocamento = sum(ord(char) for char in chave) % 26
    return deslocamento

def gerar_caractere_aleatorio():
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    return random.choice(caracteres)

def criptografar_substituicao(texto, chave):
    deslocamento = calcular_deslocamento(chave)
    resultado = ""
    
    for char in texto:
        if char.isupper():
            resultado += chr((ord(char) + deslocamento - 65) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) + deslocamento - 97) % 26 + 97)
        else:
            resultado += char
        
        resultado += gerar_caractere_aleatorio()
    
    resultado = resultado[:-1] 
    resultado += random.choice(['==!', '==@', '==?'])  
    return resultado

def decriptografar_substituicao(texto, chave):
    deslocamento = calcular_deslocamento(chave)
    texto = texto[:-3] 
    resultado = ""
    
    for i in range(0, len(texto), 2):
        char = texto[i]
        if char.isupper():
            resultado += chr((ord(char) - deslocamento - 65) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) - deslocamento - 97) % 26 + 97)
        else:
            resultado += char
    
    return resultado

def criptografar(texto, chave, numero_de_camadas):
    resultado = texto
    for _ in range(numero_de_camadas):
        resultado = criptografar_substituicao(resultado, chave)

    # A string criptografada agora não contém o número de camadas.
    return resultado

def decriptografar(texto_criptografado, chave, numero_de_camadas):
    resultado = texto_criptografado
    
    for _ in range(numero_de_camadas):
        resultado = decriptografar_substituicao(resultado, chave)
    
    return resultado