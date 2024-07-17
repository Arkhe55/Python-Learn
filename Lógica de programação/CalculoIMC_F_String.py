"""
Mudança no Calculo de IMC
com F String

"""
nome = "Gabriel santos silva"
altura = 1.77
peso = 88
imc = peso / altura ** 2
texto = f"{nome} tem {altura} de altura e pesa {peso} quilos e seu imc é {imc:.2f}"
print(texto)
