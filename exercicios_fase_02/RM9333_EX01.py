
annualInvoice = float(input('\nDigite o valor do seu faturamento anual em reais: '))
planType = int(input('\nSelecione abaixo o seu atual plano de assinatura:\n\n [1] Basic | [2] Silver | [3] Gold | [4] Platinum\n\nPlano de assinatura: '))
paymantPorcentage = 0

if planType == 1:
    paymantPorcentage = annualInvoice * 0.30
elif planType == 2:
    paymantPorcentage = annualInvoice * 0.20
elif planType == 3:
    paymantPorcentage = annualInvoice * 0.10
elif planType == 4:
    paymantPorcentage = annualInvoice * 0.05
else:
    print('Essa não é uma opção válida')

if paymantPorcentage != 0:
    print(f'O valor a ser pago para o locatário é {paymantPorcentage:.2f}')
