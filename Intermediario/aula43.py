"""Introdução a função
funçoes são trechos de codigos usados para
replicar determinada ação ao longo do seu codigo.
elas podem receber valores para parâmetro (argumentos)
e retornar um valor especifico."""

#Exemplo 1
def sum(a , b , c): # <- Parâmetros
    print(a, b , c)

sum(1,2,3) # <- Argumentos

#Exemplo 2
def saudacao(nome):
    print(f"Olá {nome}!")
nome_usuario = input("Olá qual é seu nome?: ")
saudacao(nome_usuario)

#Exemplo 3
def saudacao(nome="Sem nome"):
    print(f"Olá {nome}!")
saudacao("Matheus")
saudacao("Rodolfo")
saudacao()
