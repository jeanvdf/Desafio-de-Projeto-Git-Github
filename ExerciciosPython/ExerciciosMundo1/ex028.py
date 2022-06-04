from random import randint
n2 = randint(0, 5)
print('Estou pensando em um número entre 0 e 5 .. \n --- TENTE ADIVINHAR!! ---')
n1 = int(input('Digite o numero : '))
if n1 == n2:
    print('PARABENS !!! VOCE CONSEGUIU ADIVINHAR!')
else:
    print('Você Errou, Eu pensei no número {}, Mais Sorte na Proxima ... '.format(n2))