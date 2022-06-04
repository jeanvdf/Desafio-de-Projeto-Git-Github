print('Vamos Comparar Dois Números Inteiros')
n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))
if n1 > n2:
    print('O Primeiro Numero ({}) é Maior que o Segundo ({}). '.format(n1, n2))
elif n2 > n1:
    print('O Segundo Numero ({}) é Maior que o Primeiro ({}).'.format(n2, n1))
else:
    print('Não Existe Numero Maior, os Dois São Iguais ({} = {}).'.format(n1, n2))
