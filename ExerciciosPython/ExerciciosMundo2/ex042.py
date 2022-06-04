print('\033[32m-=-' * 20)
print('Vamos Saber Se 3 Retas Formam um Triângulo e Qual.')
print('-=-' * 20)
l1 = float(input('\033[mDigite a Primeira Reta: '))
l2 = float(input('Digite a Segunda Reta: '))
l3 = float(input('Digite a Terceira Reta: '))
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    if l1 == l2 == l3:
        print('As Retas \033[32mPODEM\033[m Formar um Triângulo !! \nE Formam um \033[34;4mTriângulo Equilátero\033[m, com todos os lados iguais.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('As Retas \033[32mPODEM\033[m Formar um Triangulo !! \nE formam um \033[34;4mTriângulo Isósceles\033[m, com 2 lados iguais.')
    else:
        print('As Retas \033[32mPODEM\033[m Formar um Triângulo !! \nE formam um \033[34;4mTriângulo Escaleno\033[m, com todos os lados diferentes.')
else:
    print('As Retas \033[31;1mNÃO\033[m Podem Formar um Triângulo.')