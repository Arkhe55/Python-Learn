"""Calculadora com While"""

# primeiro_numero = input("Digite um número")
# segundo_numero = input("Digite outro número")

while True:
    ##### Tratamento ######
    primeiro_numero = input("Digite um número: ")
    segundo_numero = input("Digite outro número: ")
    operador = input("Qual operador (+-/*): ")

    numeros_validos = None
    primeiro_convertido = 0
    segundo_convertido = 0

    try:
        primeiro_convertido = float(primeiro_numero)
        segundo_convertido = float(segundo_numero)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os numeros são invalidos")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operadores incorretos, por favor digite operadores validos")
        continue

    #### Calculo ####

    if operador == "+":
        soma = f"{primeiro_convertido + segundo_convertido:.0f}"
        print(soma)
        
    elif operador == "-":
        subtração = f"{primeiro_convertido - segundo_convertido:.0f}"
        print(subtração)

    elif operador == "/":
        divisao = (primeiro_convertido / segundo_convertido)
        print(divisao)

    elif operador == "*":
        multiplicacao = f"{primeiro_convertido * segundo_convertido:.0f}"
        print(multiplicacao)

    else:
        print("Nunca chegaria aqui ^_^")

    #### Pergunta ao usuario ####
    sair = input("Você quer sair? Sim: ").lower().startswith("s")
    print(sair)
    
    if sair is True:
        break