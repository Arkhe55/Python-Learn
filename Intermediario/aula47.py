"""
"""

x = 4

def escopo():
    global x
    x = 10
    print(x)

escopo()
print(x)  