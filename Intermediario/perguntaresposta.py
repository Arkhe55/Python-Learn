while True:
    perguntas = [
        {   
        'pergunta': 'Quanto é 2 + 2?',
        'opção': ['1', '2', '3', '4'],
        'resposta': '4',
        },
        {
        'pergunta': 'quanto é 20*20?',
        'opção': ['200', '350', '400', '150'],
        'resposta': '400',
        }]

# Primeira questão
    perguntas_opçoes = perguntas[0]['opção']

    print("Pergunta:", perguntas[0]['pergunta'])
    print("Opçoes: ")
    contador = 0

    for indice in perguntas_opçoes:
        print(f'{contador})', (indice))
        contador += 1

    input_usuario = input("Qual a reposta correta? ")
    resposta_correta = '3'

    if input_usuario == resposta_correta:
        print("Você acertou ^-^")
    else:
        print("Errrouuuu!!!")

# Segunda Questão

    perguntas_opçoes_2 = perguntas[1]['opção']
    print()
    print("Pergunta:", perguntas[1]['pergunta'])
    print()
    print("Opçoes: ")
    
    contador = 0

    for indice in perguntas_opçoes_2:
        print(f'{contador})', (indice))
        contador += 1
    
    input_usuario_2 = input("Qual a reposta correta? ")
    resposta_correta_2 = '2'

    if input_usuario_2 == resposta_correta_2:
        print("Você acertou ^-^")
    else:
        print("Errrouuuu!!!")




    

    


        




        
        
        


