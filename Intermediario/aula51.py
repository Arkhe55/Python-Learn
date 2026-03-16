"""Closure função que retorna outras funçoes"""

def saudação(msg):
    def saudar(nome):
        return f'{msg}, {nome}' 
    return saudar

falar_bom_dia = saudação("Olá bom dia")
falar_boa_noite = saudação("Olá boa noite")

# print(falar_bom_dia("Gabriel"))
# print(falar_boa_noite("Luiz"))

for nome in ["Gabriel", "Matheus", "fernando"]:
    print(falar_boa_noite(nome))
    print(falar_bom_dia(nome))
