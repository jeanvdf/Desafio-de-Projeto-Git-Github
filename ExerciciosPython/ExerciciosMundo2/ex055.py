print('Vamos Anotar o Peso de 5 Pessoas...')
maior = 0
menor = 0
for peso in range(1, 6):
    p = float(input('Digite o Pesso da {}ª pessoa: '.format(peso)))
    if peso == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O Maior Peso foi {:.2f} Kg.'
      '\nO Menor Peso foi {:.2f} Kg.'.format(maior, menor))
