
"""for variavel in range(5):
    print(variavel)"""


"""for variavel in range(1,10):
    print(variavel)"""


"""for variavel in range(1, 12, 3):
    print(variavel)"""


"""nota1 = float( input('Informe sua nota 1') )
nota2 = float( input('Informe sua nota 2') )
nota3 = float( input('Informe sua nota 3') )"""


soma = 0

for c in range(1, 4):
    nota = float( input(f'Informe a sua nota {c}: ') )
    soma = soma + nota

print(soma / 3)