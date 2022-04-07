#exercicio 01

annualInvoice = float(input('\nDigite o valor do seu faturamento anual em reais: '))

planoValido = False
while planoValido == False:
    planType = int(input('\nSelecione abaixo o seu atual plano de assinatura:\n\n [1] Basic | [2] Silver | [3] Gold | [4] Platinum\n\nPlano de assinatura: '))
    if planType == 1:
        paymantPercentage = annualInvoice * 0.30
        planoValido = True
    elif planType == 2:
        paymantPercentage = annualInvoice * 0.20
        planoValido = True
    elif planType == 3:
        paymantPercentage = annualInvoice * 0.10
        planoValido = True
    elif planType == 4:
        paymantPercentage = annualInvoice * 0.05
        planoValido = True
    else:
        print('Essa não é uma opção válida')
  
if paymantPercentage != 0:
    print(f'O valor a ser pago para o locatário é: {paymantPercentage:.2f} reais')

#adicionar uma estrutura de repetição para que, caso o usuário queira, retornar para opção de digitar salário
#adicionar estrutura de repetição para, quando não for uma opção válida, retornar as opções de plano de assinatura

  
