palavra_secreta = "amor"
letra_acertada = ""
numero_tentativas = 0

import os

while True:

    numero_tentativas += 1

    letra_digitada = input("Digite uma letra: ")

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
        
        print("Palavra formada: ", palavra_formada)
        
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print("PARABENS!! VOCÊ ACERTOU!")
        print("A palavra era: ", palavra_secreta)
        print("Número de tentativas: ", numero_tentativas)
        letra_acertada = ""
        numero_tentativas = 0