import random
import string
from caracters import caract_incript
from __error__ import __erroFile__
from __error__ import __cabecalhoErro__
caracts = caract_incript

def calcular_deslocamento(chave):
    deslocamento = sum(ord(char) for char in chave) % 26
    return deslocamento

def gerar_caractere_aleatorio():
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    return random.choice(caracteres)

def criptografar(texto, chave, numero_de_camadas):
    resultado = texto
    numero_de_camadas_codificado = f"{numero_de_camadas:04b}"  
    for _ in range(numero_de_camadas):
        deslocamento = calcular_deslocamento(chave)
        temp_resultado = ""
        for char in resultado:
            if char.isupper():
                temp_resultado += chr((ord(char) + deslocamento - 65) % 26 + 65)
            elif char.islower():
                temp_resultado += chr((ord(char) + deslocamento - 97) % 26 + 97)
            else:
                temp_resultado += char
            temp_resultado += gerar_caractere_aleatorio()
        resultado = temp_resultado[:-1]
        resultado += random.choice(['==!', '==@', '==?'])
    return numero_de_camadas_codificado + resultado

def decriptografar(texto, chave, numero_de_camadas):
    if len(texto) < 4:
        return " Erro: Texto criptografado inválido."
    
    numero_de_camadas_codificado = texto[:4]
    resultado = texto[4:]
    
    # Verificação para garantir que o cabeçalho é válido
    if not all(bit in '01' for bit in numero_de_camadas_codificado):
        __cabecalhoErro__()
    try:
        numero_de_camadas_armazenadas = int(numero_de_camadas_codificado, 2)
    except ValueError:
        return " Erro: Número de camadas inválido."
    
    deslocamento = calcular_deslocamento(chave)

    # Remover sufixos conhecidos antes de começar a decriptação
    if resultado.endswith(('==!', '==@', '==?')):
        resultado = resultado[:-3]  # Remover os últimos 3 caracteres

    # Verificar se o número de camadas é válido
    if numero_de_camadas_armazenadas != numero_de_camadas:
        return " Erro: Número de camadas inválido."
    
    for _ in range(numero_de_camadas_armazenadas):
        temp_resultado = ""
        for i in range(len(resultado)):
            char = resultado[i]
            if char.isupper():
                temp_resultado += chr((ord(char) - deslocamento - 65) % 26 + 65)
            elif char.islower():
                temp_resultado += chr((ord(char) - deslocamento - 97) % 26 + 97)
            else:
                temp_resultado += char

        # Remover caracteres aleatórios
        resultado = ''.join(temp_resultado[j] for j in range(len(temp_resultado)) if j % 2 == 0)

    return resultado

def processar_arquivo(arquivo, chave, numero_de_camadas, acao):
    conteudo = arquivo
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except FileNotFoundError:
        __erroFile__(conteudo)
    
    if (acao.lower() == 'crypt') or (acao.lower() == 'c'):
        conteudo_processado = criptografar(conteudo, chave, numero_de_camadas)
    elif (acao.lower() == 'decrypt') or (acao.lower() == 'd'):
        conteudo_processado = decriptografar(conteudo, chave, numero_de_camadas)
        
        # Aqui verificamos se houve erro na decriptação
        if "Erro:" in conteudo_processado:
            pass  # Imprimir erro no terminal
            #return  # Retornar sem sobrescrever o arquivo

    else:
        print("Ação inválida.")
        #return
    # Esta parte só será executada se não houver erro
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo_processado)
    except FileNotFoundError:
        __erroFile__(conteudo)
    #print ("  '{}' Criptografados.".format(arquivo))
    print(f"\n <ALERT> dados no arquivo '{arquivo}' {'CRYPTOGRAFADOS' if acao.lower() in ['crypt', 'c'] else 'DECRYPTOGRAFADOS'}.")
