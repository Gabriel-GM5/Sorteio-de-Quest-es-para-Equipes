import random

# Coleta os dados de entrada
nQuestões = int(input('\nNúmero de questões: '))
vetQuestões = []
for i in range(nQuestões):
    vetQuestões.append(i + 1)
nPessoas = int(input('\nNúmero de pessoas: '))
vetPessoas = []
for i in range(nPessoas):
    print('\nColega ', i + 1)
    vetPessoas.append(input('Nome: '))

print('\nAs', nQuestões, 'questões serão divididas entre os', nPessoas, ':)')

# Divide as questões igualmente e aleatoriamente
nDivisão = nQuestões//nPessoas
vetResultado = []
for i in vetPessoas:
    tmp = []
    random.shuffle(vetQuestões)
    for j in range(nDivisão):
        tmp.append(vetQuestões[0])
        del vetQuestões[0]
    vetResultado.append({'nome': i, 'questões': tmp})

# Sorteia uma pessoa para cada questão restante
existeSortudo = False
for i in range(len(vetQuestões)):
    existeSortudo = True
    random.shuffle(vetQuestões)
    for i in range(random.randint(0, 9)):
        random.shuffle(vetPessoas)
    for j in range(len(vetResultado)):
        if vetResultado[j]['nome'] == vetPessoas[0]:
            vetResultado[j]['questões'].append(vetQuestões[0])
            del vetQuestões[0]
            del vetPessoas[0]
            break

# Exibe o resultado final
print("\nRESULTADO")
for i in vetResultado:
    print(i['nome'], '->', len(i['questões']), 'questões', '->', sorted(i['questões']))
if existeSortudo:
    print('\nQuem está com sorte e teve menos questões: ')
    for i in vetPessoas:
        print('-', i)
