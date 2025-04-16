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

lista_1 = [1, 2, 3, 4]
lista_2 = ["Gabriel", "Luiz", "Rafael"]
#lista_concatenada = lista_1 + lista_2
lista_1.extend(lista_2)
print(lista_1)