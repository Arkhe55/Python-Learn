# condicao = True

# while condicao:
#     nome = input ("Qual é seu nome?")
#     print(f'Seu nome é {nome}')

contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 5:
        print("Não vou mostrar o 5")
        continue
    
    if contador >= 10 and contador <= 40:
        print("Não vou mostrar o", contador)
        continue
    
    print(contador)
    
    if contador == 50:
        break

print("Acabou")
    
"""
Operadores de atribuição
= += -= *= /= //= %= **= %=
"""
print("--Operadores--")
operador = 2
operador += 2
print(operador)