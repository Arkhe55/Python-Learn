frase = "Python é uma linguagem de programação "\
    'Multiparadigma. ' \
    'Python foi criada por guido van rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais = " "

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    
    if qtd_apareceu_mais_vezes < quantas_vezes_apareceu:
        qtd_apareceu_mais_vezes = quantas_vezes_apareceu
        letra_que_apareceu_mais = letra_atual

    i += 1

print (
    'A letra que apareceu mais vezes foi '
    f'{letra_que_apareceu_mais} que apareceu '
    f'{qtd_apareceu_mais_vezes} x '
)