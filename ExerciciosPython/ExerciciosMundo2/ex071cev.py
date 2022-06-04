print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
total = int(input('Quanto Você Deseja Sacar? R$ '))
valor = total
cedula = 50
contcedula = 0
while True:
    if valor >= cedula:
        valor -= cedula
        contcedula += 1
    else:
        if contcedula > 0:
            print(f'Total de {contcedula} notas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contcedula = 0
        if valor == 0:
            break
