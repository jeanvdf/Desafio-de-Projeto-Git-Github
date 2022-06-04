frase = str(input('Digite uma frase: ')).strip().upper()

print('Esta Frase Aparece a letra "A" {} vezes'.format(frase.count('A')))
print('Esta Frase Aparece a letra "A", pela primeira vez, na posição {}.'.format(frase.find('A')+1))
print('Esta Frase Aparece a letra "A", pela ultima vez, na posição {}.'.format(frase.rfind('A')+1))

