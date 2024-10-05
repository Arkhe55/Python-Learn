#Operadores lógicos
#and (e) or (ou) not (não)
#and: Todas as condiçoes precisam ser
#verdadeiras.
#se qualquer valor for considerado falso ou verdadeiro
#a expressão inteira será avaliada naquele valor
#São considerados falsy: 0 0.0 "" False
#Também tem o tipo none que é
#considerado não valor

entrada = input("[E]ntrada ou [S]aida: ")

senha_permitida = "123456"
senha_digitada = input("Digite a senha: ")

if (entrada == "E" or entrada == "e") and senha_permitida == senha_digitada:
    print("Entrou")
else:
    print("Saida")