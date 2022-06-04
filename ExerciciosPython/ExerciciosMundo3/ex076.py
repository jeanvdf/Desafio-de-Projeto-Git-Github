lista = ('Lápis', 1000, 'Borracha', 0.75, 'Camiseta', 35, 'Boné', 20, 'Calça', 100, 'Leite', 5.6, 'Margarina', 6.9, 'Feijão', 9.8, 'Tempero', 3.8, 'Frango', 9.98)
print('-'*43)
print('{:^42}'.format('LISTAGEM DE PREÇOS'))
print('-'*43)
for c in range(1, len(lista), 2):
    print('{:.<34}R$'.format(lista[c-1]), end='')
    print('{: >7.2f}'.format(lista[c]))
print('-'*42)
