#exercicio 04

#variáveis
actualMin = int(input('\nDigite os minutos atuais: '))
factorialNumber = 1
i = 0

#operador lógico + loop
if actualMin >= 60 or actualMin < 0:
    print('\nVALOR INVÁLIDO!\nPor favor, digite um valor inteiro entre 0 e 60\n') 
elif actualMin == 00:
    print ('\nA senha para desbloquear é: LIBERDADE1\n')
else:
    for i in range(1,actualMin +1):
        factorialNumber = factorialNumber*i
    print(f'\nA senha para desbloquear é: LIBERDADE{factorialNumber}\n')
