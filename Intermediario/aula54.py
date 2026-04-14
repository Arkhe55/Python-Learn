# Metodos dicionario Python

# len - quantidade de chaves
# keys - retorna chaves do dict
# values - retorna os valores
# items - retorna chave e valor
# Setdefault - adiciona um valor que não existe no dict



pessoa = {
    'nome': "Gabriel",
    'sobrenome': "Santos silva",
}

pessoa.setdefault('idade', 28)
print(pessoa['idade'])
print(pessoa.items())

# print(pessoa.__len__())
# print(list(pessoa.keys()))
# print(tuple(pessoa.values()))
# print(pessoa.items())


# for valores in pessoa.values():
#     print(valores)

# for valor, chave in pessoa.items():
#     print(valor, chave)
