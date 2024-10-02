#interpolação
#x e X Hexadecimal (0123456789ABCDEF)

nome = "Gabriel"
preco = 1.500

saldo= '%s seu saldo devedor é R$%.3f' % (nome, preco)

print(saldo)
print("O hexadecimal de %i é %.04X" % (13, 13))

#F String

variavel='ABC'
print(f'{variavel:a>10}')
print(f'{variavel:a^11}')
print(f"{1503.2556:0<+5.1f}")
numero=12500
print(f'{numero:,}')

