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

def remover_dado(dadosrolados, dadosguardados, i):
     lista_final = []
     dadosrolados.append(dadosguardados[i])
     del dadosguardados[i]
     lista_final.append(dadosrolados)
     lista_final.append(dadosguardados)
     return lista_final

def calcula_pontos_regra_simples(dadosrolados):
    pontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in dadosrolados:
        if dado in pontos:
            pontos[dado]+=dado
    return pontos

def calcula_pontos_soma(dadosrolados):
    soma = 0 
    for dado in dados:
        soma+=dado
    return soma

    

