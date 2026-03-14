"""
args argumentos não nomeados

* - * args (empacotamento e desempacotamento)
"""

x, y, *resto = 1, 2, 3, 4, 5
print(x, y, resto)

# def soma (x, y):
#     print(x, y, *resto)

# soma(x, y)

def argumento(*args):
    total = 0
    for numero in args:
        total += numero
    return(total)

soma = argumento(1, 2, 3, 4, 5 ,6 ,7)
print(soma)

soma_2 = argumento(4, 5, 6, 20, 40, 80)
print(soma_2)

