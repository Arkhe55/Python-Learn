# get - obtém uma chave
# pop - apaga um item com a chave e retorna o mesmo
# popitem - apaga o ultimo item adicionado
# update - atualiza dicionario com outro

p1 = {
    'nome':'gabriel',
    'sobrenome': 'santos silva'
}

# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')

# print(nome)
# print(p1.items())

# print(p1.popitem())
# print(p1)

p1.update({
    'idade':18,
    'nome':'Antonio'
})

print(p1)