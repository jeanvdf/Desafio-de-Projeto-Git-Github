print('-=-' * 20)
print('Vamos Saber Se 3 Retas Podem Formar um Triângulo... ')
print('-=-' * 20)
r1 = float(input('Qual a medida da Primeira Reta? '))
r2 = float(input('Qual a medida da Segunda Reta? '))
r3 = float(input('Qual a medida da Terceira Reta? '))
if r1 < (r2 + r3) and r3 < (r1 + r2) and r2 < (r1 + r3):
    print('Estas Retas Podem Formar um Triângulo.')
else:
    print('Estas Retas NÃO Podem Formar um Triângulo.')
