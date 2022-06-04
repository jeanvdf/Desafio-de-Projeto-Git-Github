cont = 0
s = 0
for c in range (1, 7):
    n = int(input('Digite o {}º Valor :'.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
if s == 0:
    print('Você Não Digitou Nenhum Valor Par...')
else:
    print('Você Digitou {} numeros PARES e a Soma deles é {}. '.format(cont, s))