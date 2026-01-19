"""
Docstring for Intermediario.aula45

Valores padrão para parâmetros
Ao definir uma função, parametros podem
ter valores padrão. Caso o valor não seja
Enviado para o parâmetro o padrão valor sera usado

"""

def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", "|", x + y + z)
    else:
        print(f"{x=} {y=}", "|", x + y)


soma(10, 5, 10)
