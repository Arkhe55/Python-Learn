perguntas = [
        {   
        'pergunta': 'Quanto é 2 + 2?',
        'opçoes': ['1', '2', '3', '4'],
        'resposta': '4',
        },
        {
        'pergunta': 'quanto é 20*20?',
        'opçoes': ['200', '350', '400', '150'],
        'resposta': '400',
        }]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['pergunta'])
    print()

    opçoes = pergunta['opçoes']

    for i, opcao in enumerate(opçoes):
        print(f"{i})",opcao)

    print()
    escolha = input("Escolha uma opção: ")

    escolha_int = None
    acertou = False
    qtd_opçoes = len(opçoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opçoes:
            if opçoes[escolha_int] == pergunta['resposta']:
                acertou = True
    print()

    if acertou:
        qtd_acertos += 1
        print("Acertou!!")
    else:
        print("Não acertou")

    print()

    print("Quantidade de acertos: ", qtd_acertos)
    print("de", len(perguntas), "perguntas")


