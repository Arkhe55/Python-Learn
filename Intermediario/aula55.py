# copy - retorna um copia rasa (shallow copy)

# import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'list': [0, 1, 2]
}

d2 = d1.copy() # import copy copy.deepcopy()

d2['c1'] = 1000
d2['list'][0] = 5000

print(d1)
print(d2)
