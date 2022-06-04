print('\033[32m=-=-' * 10)
print('- SIMULADOR DE EMPRÉSTIMO BANCÁRIO -')
print('=-=-' * 10 )
casa = float(input('\033[mQual o valor do imóvel? '))
anos = float(input('Em quantos Anos voce deseja Pagar? '))
parcelas = anos * 12
sal = float(input('Qual é o Seu Salário ? R$ '))
cond = sal * 0.3 > casa / parcelas
if cond == True:
    print('O Valor da parcela não excedeu o limite de 30% do seu Salário.')
    print('O Seu Empréstimo Foi aprovado, nas Seguintes Condições: ')
    print('Valor Do Emprestimo \033[34;1;4mR$ {:.2f}\033[m. \nQuantidade de parcelas: \033[34;1;4m{:.0f}\033[m. \nValor da Parcela \033[34;1;4mR$ {:.2f}\033[m . \nPARABÉNS! '.format(casa, parcelas, casa / parcelas))
else:
    print('\033[31m O Valor da Parcela EXCEDEU o limite de 30% do seu Salário!')
    print('\033[31;1m EMPRESTIMO NEGADO ! ! !')