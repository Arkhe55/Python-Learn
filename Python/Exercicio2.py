"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero_inteiro = int(input("Digite um número inteiro: "))
    if numero_inteiro % 2 == 0:
        print(f"O {numero_inteiro} é par")
        
    else:
        print(f"O {numero_inteiro} é impar")
except:
    print("Número Digitado incorreto, por favor digite um número inteiro")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = int(input("Que horas são?"))

if 0 <= horario <= 11:
    print("Bom dia")
elif 12 <= horario <= 17:
    print("Boa tarde")
elif 18 <= horario <= 23:
    print("Boa noite")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input("Qual seu primeiro nome?: ")
tamanho_nome = len(primeiro_nome)


if tamanho_nome >=1:
    print(None)
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif tamanho_nome <= 5 and tamanho_nome >= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Por favor digite um nome maior")
