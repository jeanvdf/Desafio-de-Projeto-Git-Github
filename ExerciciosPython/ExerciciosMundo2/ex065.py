print('*'*30)
print('Vamos Coletar Alguns Números..')
print('*'*30)
r = 'S'
c = soma = maior = menor = 0
while r == 'S':
    n = int(input('Digite um Valor: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
media = soma / c
print('Você Digitou {} Numeros.'
      '\nA Média entre eles é {:.2f}'
      '\nO Maior é {} '
      '\nO Menor é {}'.format(c, media, maior, menor))
