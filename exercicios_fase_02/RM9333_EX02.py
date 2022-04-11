#exercicio 02

print('\nPor favor, digite a quantidade total de votos que cada dia da semana recebeu\n')

#input para cada dia da semana
votesMonday = int(input('Segunda-feira: '))
votesTuesday = int(input('Terça-feira: '))
votesWednesday = int(input('Quarta-feira: '))
votesThursday = int(input('Quinta-feira: '))
votesFriday = int(input('Sexta-feira: '))
totalVotes = (votesMonday + votesTuesday + votesWednesday + votesThursday + votesFriday) #armazenamento do total de votos

print(f'\nA quantidade total de votos é {totalVotes}') #output do total de votos

dictionare = dict({'Segunda-feira': votesMonday, 'Terça-feira' : votesTuesday, 'Quarta-feira' : votesWednesday, 'Quinta-feira' : votesThursday, 'Sexta-feira' : votesFriday})

print(f'\nO resultado da apuração de votos foi: {dictionare}\n')

#em caso de empate:
winner = (max(dictionare, key=dictionare.get))
empate=False
for chave in dictionare.keys():
    if (chave is not winner and dictionare[chave] == dictionare[winner]):
        print('Houve empate entre {} e {}'.format(chave,winner))
        empate=True
if empate:
    exit()

#caso não haja empate
print(f'O dia com a maior quantidade de votos foi: {winner} com {dictionare[winner]} votos!\n') 
