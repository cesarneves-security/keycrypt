from setuptools import setup, find_packages

setup(
    name='keycrypt',  # Nome do seu pacote
    version='0.1.0',  # Versão do seu pacote
    author='César Neves',  # Seu nome
    author_email='cesarioneves104@gmail.com',  # Seu e-mail
    #url='https://github.com/usuario/keycrypt',
    description='keycrypt é um Framework para criptografia.',  # Descrição do pacote
    long_description=open('README.md').read(),  # Descrição longa (opcional)
    long_description_content_type='text/markdown',  # Tipo da descrição longa
    packages=find_packages(),  # Encontra automaticamente os pacotes
    install_requires=[  # As dependências do seu projeto
        'random',
        'string',
    ],
    classifiers=[  # Classificadores para o PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)
