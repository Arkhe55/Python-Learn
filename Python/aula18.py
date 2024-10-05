#operadores in e not in
#Strings são iteráveis
#Iteráveis são objetos capazes de retornar seus membros um de cada vez

nome = ...
#print(nome[...])

# print("ab" in nome)
# print(10 * "-")
# print("ab" not in nome)

# nome = input("Digite um nome: ")
# encontrar = input ("Digite o que deseja encontrar: ")

# if encontrar in nome:
#     print(f'{encontrar} Está em {nome}')
# else:
#     print(f'{encontrar} Não esta em {nome}')

senha = input("Digite uma senha: ")
confirmacao = input("Repita novamente: ")

if senha in confirmacao:
    print("Continuando seu cadastro...")
else:
    print("Confirmação incorreta")