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
    for dado in dadosrolados:
        soma+=dado
    return soma

def calcula_pontos_sequencia_baixa(dadosrolados):
    sequencias_baixas = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
    for sequencia in sequencias_baixas:
        verifica = 0
        for  dado in sequencia:
            if dado not in dadosrolados:
                verifica +=1
        if verifica == 0:
            return 15
    return 0 


def  calcula_pontos_sequencia_alta(dadosrolados):
    sequencias_altas = [[1,2,3,4,5],[2,3,4,5,6]]
    for sequencia in sequencias_altas:
        verifica = 0
        for dado in sequencia:
            if dado  not in dadosrolados:
                verifica +=1
        if verifica == 0:
            return 30
    return 0

def calcula_pontos_full_house(dadosrolados):
    verificador = {}
    for dado in dadosrolados:
        if dado in verificador:
            verificador[dado] +=1
        else:
            verificador[dado] =1
    numeros = list(verificador.values())
    if len(numeros) ==2 and (2 in numeros and 3 in numeros):
        soma = 0
        for dado in dadosrolados:
            soma += dado
        return soma
    
    return 0

def calcula_pontos_quadra(dadosrolados):
    verificador = {}
    for dado in dadosrolados:
        if dado in verificador:
            verificador[dado] +=1
        else:
            verificador[dado] = 1
    numeros = list(verificador.values())
    if len(numeros) == 4:
        soma = 0
        for dado in dadosrolados:
            soma += dado
        return soma
    
    return 0

