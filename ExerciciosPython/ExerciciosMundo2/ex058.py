print('COMPUTADOR: Vou pensar em um número de 1 a 10!!\nTENTE ADIVINHAR..!!')
from random import randint
comp = randint(1, 10)
c = 1
r = int(input('Qual o número que eu pensei ??? '))
while r != comp:
    if r > comp:
        print('Menos .. Tente novamente..')
        r = int(input('Digite o proximo número: '))
        c += 1
    else:
        print('Mais .. Tente novamente..')
        r = int(input('Digite o Proximo número: '))
        c += 1
print('PARABÉNS!! Você Acertou.. Eu pensei no número {}. '
      '\nVocê precisou de {} Tentativas Para acertar.'.format(comp, c))
