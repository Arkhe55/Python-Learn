# variavel = print("Gabriel")
# print(variavel)
# soma = [10, 5, 95, 8, 50, 30]
# total_soma = sum(soma)
# media = total_soma / len(soma)
# print(media)

""" Return | Print | NONE """

soma = [10, 50 , 5, 20, 30, 40, 100]
def media_a():
    total = sum(soma)
    media = total / len(soma)
    return media

print(media_a())
