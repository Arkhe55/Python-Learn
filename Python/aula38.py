"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

#   "Para programas que nescecitam de precisão
#           em com números decimais "
# import decimal
# numero_1 = decimal.Decimal('0.1')
# numero_2 = decimal.Decimal('0.7')

numero_1 = 0.1
numero_2 = 0.7
soma = numero_1 + numero_2


print(type (soma))
print(type (f"{soma:.1f}"))
print(type (round(soma, 2)))