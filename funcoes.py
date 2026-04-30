import random

def rolar_dados(n):
    dados = []
    for i in range(n):
        dadonovo = random.randint(1,6)
        dados.append(dadonovo)
    return dados