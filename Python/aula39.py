""" Split divide uma string 
    Join Une uma string """

frase = "É mais importante dominar" \
" as cartas que você tem nas mãos do que reclamar " \
" das cartas que seu oponente recebeu"

lista_de_frases = frase.split()

# for indice, frase in enumerate(lista_de_frases):
#     print (lista_de_frases[indice])

for indice in enumerate(lista_de_frases):
    print(f"{indice}\n")

print(" --- Join --- \n ")
frases_unidas = "-".join("abc")
print(frases_unidas)
