"""
Docstring for Intermediario.aula46
"""
x = 4 #Valor fora do escopo da função

def funcao(x):
    x = 10
    def funcao_2(y):
        y = 20
        print(x, y)
    funcao_2(x)

print(x) #Valor executado fora do escopo da função
funcao(x)
