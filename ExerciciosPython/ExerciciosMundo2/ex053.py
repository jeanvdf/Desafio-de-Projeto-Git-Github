frase = str(input('Digite uma Frase: ')).strip().upper()
dividido = frase.split()
junto = ''.join(dividido)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[c]
print('O Inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada Não é Palíndromo')
