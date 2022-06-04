print('*'*15)
print('PAR OU IMPAR!')
print('*'*15)
c = s = 0
while True:
    from random import randint
    comp = randint(0, 11)
    print('*-'*20)
    jogador = int(input('Diga um Valor: '))
    pijog = ' '
    while pijog not in 'PI':
        pijog = str(input('Você escolher Par ou Impar? [P/I]')).upper().strip()[0]
    s = comp + jogador
    print('*-'*20)
    if s % 2 == 0:
        print(f'Você Jogou {jogador} e o computador jogou {comp}. Deu um Total de {s} E DEU PAR.')
        if pijog == 'P':
            print('Você VENCEU! \nVamos Jogar Novamente...')
            c += 1
        else:
            print('Você PERDEU!')
            break
    elif s % 2 == 1:
        print(f'Você jogou {jogador} e o computador jogou {comp}. Deu um Total de {s} E DEU ÍMPAR.')
        if pijog == 'I':
            print('Você VENCEU! \nVamos Jogar Novamente...')
            c += 1
        else:
            print('Você PERDEU!')
            break
print('*'*33)
print(f'GAME OVER!! Você venceu {c} vezes.')
print('*'*33)
