print('Vamos Jogar JOKENPÔ! ')
import random
computador = random.randint(1, 3)
print('Digite o Numero de Acordo com a Sua Escolha:'
      '\n(1) - Pedra '
      '\n(2) - Papel '
      '\n(3) - Tesoura ')
player = int(input('Escolha uma Opção : '))
if player != 1 != 2 != 3:
      print('Opção INVALIDA , Tente Novamente.')
if computador == player:
      print('DEU EMPATE!! Também escolhi a Opção {}.'.format(computador))
if computador == 1 and player == 2 or computador == 2 and player == 3 or computador == 3 and player == 1:
      print('Parabéns !! Você me Ganhou , escolhi a opção {} e voce {}. '.format(computador, player))
if computador == 1 and player == 3 or computador == 2 and player == 1 or computador == 3 and player == 2:
      print('Eu Te Venci !! Escolhi a Opção {} E você {}.'.format(computador, player))
