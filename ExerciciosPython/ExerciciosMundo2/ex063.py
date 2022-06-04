print('=-='*15)
print('Vamos Mostrar uma Sequencia Fibonacci!')
print('=-='*15)
n = int(input('Quantos Termos Você Deseja Mostrar? '))
c = 2
n1 = 0
n2 = 1
f = 0
print('{} ► {}'.format(n1, n2), end='')
while c != n:
    f = n1 + n2
    print(' ► {}'.format(f), end='')
    n1 = n2
    n2 = f
    c += 1
print(' ► FIM')
print('*'*45)
print('{} termos de FIBONACCI'.format(n))
print('*'*45)
