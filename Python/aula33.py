"""
Tipo Mutáveis
Copiando o valor (Imutáveis)
Aponta para o mesmo valor da memoria (Mutáveis)
"""

lista_1 = ["Gabriel", "João", "Rodolfo"]
lista_2 = lista_1.copy()
lista_1[0] = "Batata"
# lista_2 = lista_1

print(lista_1)

print(lista_2)