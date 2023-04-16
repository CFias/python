# FUNÇÕES 

# 1. O que são e quando utilizá-las ?

# Funções que já utilizamos anteriormente...

"""print() # - Imiprimi uma mensagem (int, float, str) no console (terminal, cmd)
input() # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len()   # - Recebe uma lista e retorna o tamanho dessa lista
max()   # - Retorna o maior valor de uma lista """

# 2. Criação de Funções 

# Função inicial
def saudacao():
    print('Aprendendo cada vez mais.')
    print('Estou feliz com tudo isso!')

saudacao()


# Função com parâmetros
def saudacao(name, curso):
    print(f'Olá, {name} seja bem-vindo(a)!')
    print(f'É um prazer ter você fazendo o nosso curso de {curso}')

saudacao('Cleidson', 'Python')
saudacao('Milena', 'JavaScript')


# Função com parâmetros default
def saudacao(name, curso='Python'):
    print(f'Olá, {name} seja bem-vindo(a)!')
    print(f'É um prazer ter você fazendo o nosso curso de {curso}')

saudacao('Cleidson')


# Função com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O resultado da soma é: ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado  = calculadora(10, 20)
print(resultado)