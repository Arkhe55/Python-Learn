"""
Mudança no Calculo de IMC
com F String e Input


"""
nome = input("Qual seu nome?")
altura = float(input("Qual sua altura? "))
peso = int(input("Quanto você pesa? "))

imc = peso // altura ** 2


texto = f"{nome} tem {altura} de altura e pesa {peso} quilos e seu imc é {imc:.2f}"
print(texto)