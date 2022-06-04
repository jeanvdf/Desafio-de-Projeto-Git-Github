contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
r = 'S'
while r == 'S':
    while True:
            num = int(input('Digite um Número entre 0 e 20: '))
            if 0 <= num <= 20:
                break
            print('Tente Novamente..', end=' ')
    print(f'Você digitou o numero {contagem[num]}. ')
    r = str(input('Deseja Continuar? [S / N]')).strip().upper()
