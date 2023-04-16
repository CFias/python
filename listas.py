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


# > MÉTODOS DE LISTAS
lista = [2, 4, 6, 8, 10]


# append
print('Antes do append: ', lista)
lista.append(3)
print('Depois do append: ', lista)


# insert
lista.insert(2, 5)
print('Depois do insert: ', lista)


# extend
lista2 = [1, 3, 7]
lista.extend(lista2)
print('Depois do extend: ', lista)


# pop
lista.pop()
print('Lista após o pop: ', lista)
lista.pop(0)
print('Lista após o pop: ', lista)


# remove
lista.remove(3)
print('Depois do remove: ', lista)


# count
print('Quantidade de 4 na lista: ', lista.count(4))


# index
print('Índice do elemento 12: ', lista.index(4))


# sort
lista.sort()
print(lista)
lista.sort(reverse=True)
print('Lista ordenada de forma revertida: ', lista)


# FUNÇÕES PARA LISTAS

# len
print(len(lista))


# sum / somar os elementos
print(sum(lista))


# max
print('Maior elemento da lista: ', max(lista))


# min 
print('Menor elemento da lista: ', min(lista))