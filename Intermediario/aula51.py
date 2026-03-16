"""Closure função que retorna outras funçoes"""

def comprimento(msg):
    def saudar(nome):
        return f'{msg}, {nome}'
    return saudar

falar_bom_dia = comprimento("Olá bom dia")
falar_boa_noite = comprimento("Olá boa noite")

# print(falar_bom_dia("Gabriel"))
# print(falar_boa_noite("Luiz"))

for nome in ["Gabriel", "Matheus", "fernando"]:
    print(falar_boa_noite(nome))
    print(falar_bom_dia(nome))
