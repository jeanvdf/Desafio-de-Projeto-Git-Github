s = c = contmais = 0
r = 'S'
while r == 'S':
    nome = str(input('Digite o nome do produto : '))
    preco = float(input('Digite o Preço do Produto. R$  '))
    s += preco
    if preco > 1000:
        contmais += 1
    if c == 0 or preco < menor:
        menor = preco
        menornome = nome
    r = str(input('Deseja Continuar ? [S / N]: ')).strip().upper()[0]
    while r not in 'SsNn':
        r = str(input('Deseja Continuar ? [S / N]: ')).strip().upper()[0]
    c += 1
print(f'O Valor total Gasto na Compra é R${s:.2f}.')
print(f'Ao Total Você tem {contmais} produtos acima de R$1000.00 ')
print(f'O Produto mais barato é {menornome} custando R${menor}')
