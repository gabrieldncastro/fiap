#exercicio 03

#variáveis
estudante = 1

notaImpar = 0
estudanteImpar = 0
mediaImpar = 0

notaPar = 0
estudantePar = 0
mediaPar = 0

#alunos quem tem o numero impar na chamada
print('\nAtenção, você está digitando a nota dos alunos ímpares\n')

while (estudante <= 10):
    if estudante % 2 == 1:
        notaImpar = float(input(f'Digite a nota do estudante nº{estudante}: '))
        mediaImpar = mediaImpar + notaImpar
        estudanteImpar = estudanteImpar + 1
    estudante = estudante + 1
estudante = 0

#alunos que tem o numero par na chamada
print('\nAtenção, você está digitando a nota dos estudantes pares\n')
while (estudante <= 10):
    if estudante % 2 == 0 and estudante > 0:
        notaPar = float(input(f'Digite a nota do estudante nº{estudante}: '))
        mediaPar = mediaPar + notaPar
        estudantePar = estudantePar + 1
    estudante = estudante + 1
estudante = 0

#print(f'\n A média dos estudantes foi:\n Estudantes Impares: {:.1f} | Estudantes Par:{:.1f}')