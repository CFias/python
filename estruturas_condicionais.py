idade = 25

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

"""media= float( input('Qual foi a sua nota ?') )

if media >= 7:
    print(media, 'Aprovado(a)')
elif media >= 5:
    print(media, 'Você está na recuperação!')
else:
    print(media, 'Reprovado(a)')"""


media = float( input('Informe a sua nota aqui: ') )
presenca = float( input('Infome a sua frequência nas aulas: ') )

if media >= 7 and presenca >= 70:
    print('Você foi aprovado!')
elif media >= 5 and presenca >= 60:
    print('Você está na recuperação!')
else:
    print('Você foi reprovado!')