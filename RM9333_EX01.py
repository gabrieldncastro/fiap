"""
Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: 
um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade.

O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento 
que o canal do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba
qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada
nível de assinatura: 

basic - 30%
silver - 20%
gold - 10%
platinum - 5%
"""

annualInvoice = float(input('\nDigite o valor do seu faturamento anual em reais: '))
planType = int(input('\nSelecione abaixo o seu atual plano de assinatura:\n\n [1] Basic | [2] Silver | [3] Gold | [4] Platinum\n\nPlano de assinatura: '))

if planType == 1:
    print(f'O valor a ser pago para o locatário é {(annualInvoice * 0.30):.2f}')
elif planType == 2:
    print(f'O valor a ser pago para o locatário é {(annualInvoice * 0.20):.2f}')
elif planType == 3:
    print(f'O valor a ser pago para o locatário é {(annualInvoice * 0.10):.2f}')
elif planType == 4:
    print(f'O valor a ser pago para o locatário é {(annualInvoice * 0.05):.2f}')
else:
    print('Essa não é uma opção válida')
