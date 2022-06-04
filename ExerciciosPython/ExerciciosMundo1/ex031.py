viagem = float(input('Qual a distância da viagem (Km) ?  '))
if viagem <= 200:
    preco = viagem * 0.5
    print('O Valor da Sua Viagem será de R${:.2f} .'.format(preco))
else:
    preco = viagem * 0.45
    print('O Valor da Sua viagem será de R${:.2f} .'.format(preco))