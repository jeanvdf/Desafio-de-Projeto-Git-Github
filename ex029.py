vel = int(input('Qual a velocidade do Veículo (Km/h) ?  '))
if vel > 80:
    multa = vel - 80
    print('Você ultrapassou o Limite de Velocidade e Será multado em R$ {} .'.format(multa*7))
    print('A multa é de R$7.00 por Km/h excedido.')
else:
    print('Parabéns! Você esta dentro do limite de velocidade da via (80Km/h).')