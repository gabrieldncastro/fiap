#exercicio 03

#variáveis
studant = 1
oddNotes = 0
totalOddNote = 0
evenNotes = 0
totalEvenNote = 0

#alunos quem tem o numero ímpar na chamada
print('\nAtenção, você está digitando a nota dos alunos ímpar\n')

while (studant <= 50):
    if studant % 2 == 1:
        oddNotes = float(input(f'Digite a nota do studant nº{studant}: '))
        totalOddNote = totalOddNote + oddNotes
    studant = studant + 1
studant = 0

#alunos que tem o numero par na chamada
print('\nAtenção, você está digitando a nota dos estudantes par\n')
while (studant <= 50):
    if studant % 2 == 0 and studant > 0:
        evenNotes = float(input(f'Digite a nota do studant nº{studant}: '))
        totalEvenNote = totalEvenNote + evenNotes
    studant = studant + 1
studant = 0

#medias
averageEvenStudants = totalEvenNote / 25
averageOddStudants = totalOddNote / 25

print(f'\n A média dos estudantes foi:\n\n Estudantes ímpar: {averageOddStudants:.1f} | Estudantes Par:{averageEvenStudants:.1f}')

if averageOddStudants == averageEvenStudants:
    print('\nHouve empate entre a média dos alunos ímpar e par')
elif averageOddStudants > averageEvenStudants:
    print(f'\nOs alunos com a média ímpar obtiveram uma média superior aos alunos com numero par na chamada.')
else:
    print(f'\nOs alunos com a média Par obtiveram uma média superior aos alunos com ímpar na chamada.')
