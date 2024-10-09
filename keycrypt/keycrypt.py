import string
import sys
import os
from hash_dados import *
from hash_file import *
import random
# encriptando e decriptando dados
caracteres2 = random.choice(caract_incript)

def encript(EncriptDados, key, cmd):
    dados = EncriptDados
    chave = key
    numero_de_camadas = cmd
    dados2 = dados.replace(' ', caracteres2)
    dados_criptografados = criptografar(dados2, chave, numero_de_camadas)
    return dados_criptografados

def decript(DecriptDados, keyDecript, cmd):
    key = keyDecript
    #numero_de_camadas_usuario = cmd
    dados_decriptografados = decriptografar(DecriptDados, key, cmd)
    dados_decriptografados1 = dados_decriptografados.replace(caracteres2, " ")
    dados_decriptografados2 = dados_decriptografados1.replace('@', ' ')
    dados_decriptografados3 = dados_decriptografados2.replace('!', ' ')
    dados_decriptografados4 = dados_decriptografados3.replace('#', ' ')
    dados_decriptografados5 = dados_decriptografados4.replace('$', ' ')
    dados_decriptografados6 = dados_decriptografados5.replace('&', ' ')
    dados_decriptografados7 = dados_decriptografados6.replace('*', ' ')
    dados_decriptografados8 = dados_decriptografados7.replace('=', ' ')
    dados_decriptografados9 = dados_decriptografados8.replace('_', ' ')
    if (dados_decriptografados9 == None) or (dados_decriptografados9 == ''):
        return "  <ERRO> ERRO DE CAMADA."
    else:
        return dados_decriptografados9

# encriptando e decriptando file
def processkey(fileEncript, key, cmd, action):
    chave = key
    numero_de_camadas = cmd
    processar_arquivo(fileEncript, chave, numero_de_camadas, action)

    
    