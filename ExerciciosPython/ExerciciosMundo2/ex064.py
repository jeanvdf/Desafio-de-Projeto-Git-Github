print('*'*30)
print('SOMADOR DE NUMEROS INTEIROS')
print('*'*30)
n = soma = c = 0
while n != 999:
    n = int(input('Digite um numero ["999" para Parar] : '))
    if n != 999:
        soma += n
        c += 1
print('Foram Digitados {} Números e a Soma Dos Valores é {}.'.format(c, soma))
