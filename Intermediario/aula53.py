pessoa = {}

chave = "nome"
sobrenome = "sobrenome"

pessoa[chave] = "Gabriel"
pessoa[sobrenome] = "Santos silva"

print(pessoa[chave])

pessoa[chave] = "Luiz"

# del pessoa[sobrenome]

if pessoa.get(sobrenome) is None:
    print("Não Existe")

else:
    print(pessoa[sobrenome])


