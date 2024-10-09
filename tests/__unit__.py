from keycrypt import encript # função para criptografia
from keycrypt import decript # função para decriptografia
from keycrypt import processkey # função para criptografia e decriptografia de Arquivos

# key= - Cria uma chave para criptografar
# cmd= - Adicione um número de camandas

# Criptografando Dados
__dadoCripto__ = encript('Keycrypt - framework para criptografia', key='criarChave', cmd=1)
print ('\n DADOS CRIPTOGAFADO:',__dadoCripto__)

# keyDecript= - Cria uma chave para criptografar
# cmd= - Adicione um número de camandas

# decriptografando Dados
__dadosdecriptografados__ = decript('0001MXgwaOeatwatrgv4@w-j@khatycholgzyhq1tLmW@ArUcCtscc@Ze4tHkBrFvKqvirtZcShYkFc==!', keyDecript='criarChave', cmd=1)
print ('\n DADOS DECRIPTOGRAFADOS:',__dadosdecriptografados__)

# action='crypt' - Para criptografar os dados do arquivo

# CRIPTOGRAFANDO ARQUIVO
try:
    processkey('file.txt', key='chave', cmd=2, action='crypt')
except TypeError:
    print ('')
    print ('\n <ERROR> PARAMENTOS INCOMPLETOS.')

# action='decrypt' - Para decriptografar os dados do arquivo

# CRIPTOGRAFANDO ARQUIVO
try:
    processkey('file.txt', key='chave', cmd=2, action='decrypt')
except TypeError:
    print ('')
    print ('\n <ERROR> PARAMENTOS INCOMPLETOS.')