import random
import funcoes

def dados(numero_dados):
    dados = []
    for i in range(numero_dados):
        dados.append(random.randint(1,6))
    return dados

cartela_pontos = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

categorias = ['1', '2', '3', '4', '5', '6', 'sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']
funcoes.imprime_cartela(cartela_pontos)

for rodada in range(12):

    if all(v != -1 for v in cartela_de_pontos['regra_simples'].values()) and \
        all(v != -1 for v in cartela_de_pontos['regra_avancada'].values()):
        break

    dados_rolados = dados(5)
    dados_guardados = []
    repetidas = 0
    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_guardados}')

    jogada = False
    while not jogada:
        opcao = str(input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:'))

    if opcao == '1':
        indice = str(input("Digite o índice do dado a ser guardado (0 a 4):"))
        dados_guardados.append(dados_rolados[indice])
        dados_rolados.pop(indice)

    elif opcao == '2':
        indice = str(input("Digite o índice do dado a ser remove (0 a 4):"))
        dados_rolados.append(dados_guardados[indice])
        dados_guardados.pop(indice)

    elif opcao == '3':
        if repetidas >=2:
            print('Você já usou todas as repetidas.')
        else:
            dados_rolados = dados(len(dados_rolados))
            repetidas +=1
    
    elif opcao == '4':
        funcoes.imprime_cartela(cartela_pontos)

    elif opcao == '0':
        combinacao = str('Digite a combinação desejada:')
        if combinacao not in categorias:
            print ('Combinação inválida. Tente novamente.')
            continue

        if combinacao in ['1','2','3','4','5','6']:
            if cartela_pontos['regra_simples'][int(combinacao)] != -1:
                print ('Essa combinação já foi utilizada.')
                continue
        else:
            if cartela_pontos['regra_avancada'][combinacao] != -1:
                print ('Essa combinação já foi utilizada.')
                continue
        
        todos_dados = dados_rolados + dados_guardados
        cartela_pontos = funcoes.faz_jogada(todos_dados, combinacao, cartela_pontos)
        jogada = True
    else:
        print('Opção inválida. Tente novamente.')
    
    if not jogada:
        print (f'Dados rolados: {dados_rolados}')
        print (f'Dados guardados: {dados_guardados}')

pontuacao = 0
pontos = 0

for valor in cartela_pontos['regra_simples'].values():
    if valor != -1:
        pontos += valor
        pontuacao += valor

for valor in cartela_pontos['regra_avancada'].values():
    if valor != -1:
        pontuacao += valor

if pontos >= 63:
    pontuacao += 35

funcoes.imprime_cartela(cartela_pontos)
print (f'Pontuação total: {pontuacao}')