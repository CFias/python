cheguei_atrasado = int(input('Quantas vezes você chegou atrasado? '))
nome = input('Qual é o seu nome ?')

if cheguei_atrasado >= 3:
    print(f'Você não pode entrar, {nome}. Você está suspenso, pois você já chegou atrasado {cheguei_atrasado} vezes!')
elif cheguei_atrasado == 1:
    print(f'Pode entrar, {nome}. Mas caso chegue atrasado mais duas vezes, você será suspenso!')
elif cheguei_atrasado == 2:
    print(f'Pode entrar, {nome}. Mas caso chegue atrasado mais uma vezes, você será suspenso!')
else:
    print('Pode entrar!')



