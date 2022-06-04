n = int(input('Digite um Número: '))
s = 0
for c in range (1, n + 1):
    if n % c == 0 or n % c == n:
        s += 1
if s == 2:
    print('O Número é Primo!!')
else:
    print('O Número Não é Primo.')
