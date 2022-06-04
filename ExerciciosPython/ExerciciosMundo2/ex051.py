print('Vamos Calcular Os Primeiros 10 Termos de uma P.A')
termo1 = int(input('Digite o Primeiro Termo dessa PA: '))
r = int(input('Digite A Razão : '))
for c in range (1, 11):
    print('{} '.format(termo1), end='► ')
    termo1 += r
print('FIM')