print('\033[32m=-=' * 5)
print('CALCULO DE IMC')
print('=-=' * 5)
peso = float(input('\033[34mDigite o Seu Peso (Kg): '))
altura = float(input('Digite a Sua Altura (cm): '))
altura = altura / 100
IMC = peso / (altura ** 2)
print('O IMC dessa pessoa é : {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Voce Está ABAIXO DO PESO IDEAL.')
elif 25 > IMC >= 18.5:
    print('Voce Está no PESO IDEAL.')
elif 30 > IMC >= 25:
    print('Você Esta no SOBREPESO.')
elif 40 > IMC >= 30:
    print('Você Está na OBESIDADE.')
else:
    print('Você Esta na OBESIDADE MÓRBIDA.')
