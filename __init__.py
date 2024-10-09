# __init__.py
__version__ = '0.1.0'  # Defina a versão do seu pacote
__author__ = 'César Neves'  # Insira seu nome
__email__ = 'cesarioneves104@gmail.com'  # Insira seu email

# Importando as funções principais do seu módulo
from keycrypt import encript, decript, processkey

# Definindo a lista de itens exportáveis
__all__ = ['encript', 'decript', 'processkey']
