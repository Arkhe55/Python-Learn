"""
Listas em python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Métodos úteis:
    append, insert, pop, del, clear, extend, +
    Created Read Update Delete - (CRUD)
"""

lista = [1, 2, 3, 4]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

print("Lista inteira: ",lista)

lista.append(5)
lista.append(6)
lista.append(7)
#A Ordem do indice muda com a alteração
lista.pop(0)
lista.pop(0)
lista.pop(0)
lista.pop(0)

print("Lista com indices removidos: ",lista)
