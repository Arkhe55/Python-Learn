nome = input("Qual é seu nome?: ")
idade = input("Qual sua idade?: ")

if nome and idade:
    print(f"seu nome é: {nome}")
    print(f"seu nome invertido é: {nome[::-1]}")
    print(f"Seu nome contem: {len(nome)} Caracteres")
    print(f"A primeira letra do seu nome é: {nome[-1]}")
    print(f"A Ultima letra do seu nome é: {nome[0]}")

    if " " in nome:
        print(f"Seu nome contem espaços")

else:
    print("Desculpe, Você deixou campos vazios")
