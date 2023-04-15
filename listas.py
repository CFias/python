# Antes 
nota1 = 7.9
nota2 = 8.7
nota3 = 9.8

# Com Lista
notas = [7.9, 8.7, 9.8]

# Criando Listas
lista = []
lista = list()
lista = [25, 'Fias', 1998, True]
lista_de_listas = [10, [1, 2, 3]]


# Indexação de Slices (Fatiamento)
lista = [25, 'Fias', 1998, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
#print(lista[4])

print(lista[-1])

# Slices
lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:3])

# Interação com o FOR

# 1. Utilizando os próprios elementos da lista
for elemento in lista:
    print(elemento)

# 2. Utilizando os Índices
print('Comprimento da Lista: ', len(lista))
for i in range(len(lista)):
    print(i)