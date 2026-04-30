import random

def rolar_dados(n):
    dados = []
    for i in range(n):
        dadonovo = random.randint(1,6)
        dados.append(dadonovo)
    return dados

def guardar_dado(dadosrolados, dadosguardados, i):
    lista_final = []
    dadosguardados.append(dadosrolados[i])
    del dadosrolados[i]
    lista_final.append(dadosrolados)
    lista_final.append(dadosguardados)
    return lista_final
    
    

