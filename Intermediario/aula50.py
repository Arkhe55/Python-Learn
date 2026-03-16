"""High Order functions
função de primeira classe"""

def msg(mensagem, nome, idade):
    return f'{mensagem}, {nome}, {idade}'

def exe(saudacao, *args):
    return saudacao(*args)

v = exe(msg, "Olá", "Gabriel", "Idade")
print(v)


# variavel_1 = msg("Olá")
# print(variavel_1)

# print(msg("Olá bom dia"))