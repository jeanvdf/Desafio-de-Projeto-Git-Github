nome = str(input('Digite o nome de sua Cidade: ')).strip().upper()
dividido = nome.split()
print('A cidade começa com o nome "Santo" ? {}'.format('SANTO' in dividido[0]))
#print(nome[:5].upper() == 'SANTO')