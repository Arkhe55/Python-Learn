import random

nove_digitos = ""
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_regresivo_1 = 10
resultado_1 = 0
for indice_1 in nove_digitos:
    resultado_1 += int(indice_1) * contador_regresivo_1
    contador_regresivo_1 -= 1
resultado_nove_digitos = (resultado_1 * 10) % 11
resultado_nove_digitos = resultado_nove_digitos if resultado_nove_digitos <= 9 else 0
print(f"-- Primeiro digito dos 2 Ultimos: {resultado_nove_digitos} --")

# Segundo digito dos 2 Ultimos
dez_digitos = nove_digitos + str(resultado_nove_digitos)
contador_regresivo_2 = 11
resultado_2 = 0
for indice_2 in dez_digitos:
    resultado_2 += int(indice_2) * contador_regresivo_2
    contador_regresivo_2 -= 1
resultado_dez_digitos = (resultado_2 * 10) % 11
resultado_dez_digitos = resultado_dez_digitos if resultado_dez_digitos <= 9 else 0
print(f"-- Segundo Digito dos 2 Ultimos: {resultado_dez_digitos} --" )
cpf_gerado = f'{nove_digitos}{resultado_nove_digitos}{resultado_dez_digitos}'
print(f"CPF: {cpf_gerado}")