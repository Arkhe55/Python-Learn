"""

Listas em python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
    Métodos úteis:
append - adiciona um item ao final
insert - adiciona um item no indice escolhido
pop - remove do final ou do indice escolhido e retorna o valor
del - deleta o indice escolhido
clear - limpa a lista
extend - estende a lista
 + - concatena a lista
    append, insert, pop, del, clear, extend, +
    Created Read Update Delete - (CRUD)

"""

lista = ["Gabriel", "Luiz", "Rodolfo", "Matheus"]
nome = lista.pop(0)
del lista[-3]
# lista.clear()
lista.insert(0, 1)
print(lista)