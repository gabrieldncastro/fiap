#exercicio 01

annualInvoice = float(input('\nDigite o valor do seu faturamento anual em reais: '))
paymantPercentage = 0

validPlan = False
while validPlan == False:
    planType = int(input('\nPor favor, selecione abaixo o seu atual plano de assinatura:\n\n [1] Basic | [2] Silver | [3] Gold | [4] Platinum\n\nPlano de assinatura: '))
    if planType == 1:
        paymantPercentage = annualInvoice * 0.30
        validPlan = True
    elif planType == 2:
        paymantPercentage = annualInvoice * 0.20
        validPlan = True
    elif planType == 3:
        paymantPercentage = annualInvoice * 0.10
        validPlan = True
    elif planType == 4:
        paymantPercentage = annualInvoice * 0.05
        validPlan = True
    else:
        print('\n\nEssa não é uma opção válida!') #caso o usuario selecione uma opção inválida, apresente as opções atê que seja feito uma escolha válida

if paymantPercentage != 0:
    print(f'\nO valor a ser pago para o locatário é: {paymantPercentage:.2f} Reais\n')



  
