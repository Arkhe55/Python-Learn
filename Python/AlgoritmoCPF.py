"""
Calculo do primeiro dígito do CPF

CPF: 115.822.070-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  115.822.070-70 (11582207070)
   10  9  8  7  6  5  4  3  2
*  1   1  5  8  2  2  0  7  0
   10  9  40 56 12 10 0  21 0

Somar todos os resultados: 
Multiplicar o resultado anterior por 10
158 * 10 = 1580
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""
import re

while True:
    dado_usuario = input("Digite seu CPF: ")
    dado_usuario = re.sub(r"[^0-9]", "",
    dado_usuario)
    
    print(dado_usuario)

    try:
        if len(dado_usuario) != 9:
            raise Exception("")
        dez_digitos = dado_usuario
        contador_regresivo_1 = 10
        resultado_1 = 0
        for indice_1 in dez_digitos:
            resultado_1 += int(indice_1) * contador_regresivo_1
            contador_regresivo_1 -= 1
        resultado_nove_digitos = (resultado_1 * 10) % 11
        resultado_nove_digitos = resultado_nove_digitos if resultado_nove_digitos <= 9 else 0
        print(f"-- Primeiro digito dos 2 Ultimos: {resultado_nove_digitos} --")
        
        # Segundo digito dos 2 Ultimos
        dez_digitos = dado_usuario + str(resultado_nove_digitos)
        contador_regresivo_2 = 11
        resultado_2 = 0
        for indice_2 in dez_digitos:
            resultado_2 += int(indice_2) * contador_regresivo_2
            contador_regresivo_2 -= 1
        resultado_dez_digitos = (resultado_2 * 10) % 11
        resultado_dez_digitos = resultado_dez_digitos if resultado_dez_digitos <= 9 else 0
        print(f"-- Segundo Digito dos 2 Ultimos: {resultado_dez_digitos} --" )
            
    except Exception as erro:
        print(erro)
        print("Tivemos um problema. Verifique se seu cpf é valido Exemplo: 062.464.560-65")


    
        

    
    
    
    

    