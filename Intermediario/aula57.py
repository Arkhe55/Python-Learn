# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um Set
# set(iteravel) ou {1, 2, 3}

# set_1 = set('Gabriel')
# set_2 = {'Gabriel'}

# print(type(set_2))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

set_1 = {1, 2 ,3, 3, 3, 3, 3, 5, 4, 4, 1 ,4}

print(set_1)

# print(6 not in set_1)

# set_1 = set(lista)
# lista_2 = list(set_1)

# for i, indice in enumerate(set_1):
#     print(i, indice)

# Métodos úteis:
# add, update, clear, discard


