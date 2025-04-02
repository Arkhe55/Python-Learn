frase = "Python é uma linguagem de programação "\
    "Multiparadigma. " \
    "Python foi criada por guido van rossum."

i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = " "

while i < len(frase):

    letra = frase[i]

    if letra == ' ':
        i += 1
        continue
    
    qtd_letra_x = frase.count(letra)
    
    i += 1
    
    if qtd_apareceu_mais < qtd_letra_x:
        qtd_apareceu_mais = qtd_letra_x
        letra_apareceu_mais = letra

print("A letra que apareceu mais vezes foi "
f"'{letra_apareceu_mais}'")
