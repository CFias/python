numero_sorteado = 15

numero_escolhido = int( input('Informe um número entre 1 a 20: ') )

while numero_escolhido != numero_sorteado:
    print('Você errou! Tente novamente...')

    numero_escolhido = int( input('Informe um número entre 1 a 20: ') )

print('Parabéns, você acertou!!!')

# Exemplo 02: Estrutura com contador 

contador = 0

while contador < 5:
    print(contador)

    contador = contador +1