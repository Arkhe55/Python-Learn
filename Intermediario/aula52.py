"""Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
"""

pessoa = {
    "nome": "Gabriel",
    "sobrenome": "Santos Silva",
    "idade": 28,
    "endereço": "Rua Tantos Tantos"

}

pessoa_2 = dict(nome="Sara", sobrenome="Santos silva", idade=18)

#[] para acessar o "indice" do dicionario
print(pessoa["idade"])
print(pessoa_2["sobrenome"])
print("-------------")

for chave in pessoa:
    print(chave, pessoa[chave])