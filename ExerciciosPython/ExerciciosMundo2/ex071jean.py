print('*'*30)
print('{:^30}'.format('BANCO CEV'))
print('*'*30)
saldo = int(input('Qual Valor Você Deseja Sacar? R$ '))
while True:
    if saldo % 50 == 0:
        print('Total de {:.0f} cedulas de R$50'.format(saldo / 50))
        saldo = 0
        break
    elif saldo % 50 != 0:
        if saldo // 50 > 0:
            print('Total de {:.0f} cédulas de R$50'.format(saldo // 50))
            saldo = saldo - ((saldo // 50) * 50)
    if saldo % 20 == 0:
        print('Total de {:.0f} cédulas de R$20'.format(saldo / 20))
        saldo = 0
        break
    if saldo % 20 != 0:
        if saldo //20 > 0:
            print('Total de {:.0f} cédulas de R$20'.format(saldo // 20))
            saldo -= ((saldo // 20) * 20)
    if saldo % 10 == 0:
        print('Total de {:.0f} cédulas de R$10'.format(saldo / 10))
        break
    if saldo % 10 != 0:
        if saldo // 10 > 0:
            print('Total de {:.0f} cédulas de R$10.'.format(saldo // 10))
            saldo -= ((saldo // 10) * 10)
        if saldo > 0:
            print('Total de {:.0f} cédulas de R$1.'.format(saldo))
            break
    if saldo == 0:
        break
print('*'*45)
print('Volte Sempre ao BANCO CEV. Tenha um Bom dia')
