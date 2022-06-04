import random
aluno1 = input('Qual o nome do Primeiro Aluno? ')
aluno2 = input('Qual o nome do Segundo Aluno? ')
aluno3 = input('Qual o nome do Terceiro Aluno? ')
aluno4 = input('Qual o nome do Quarto Aluno? ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))