print('Vamos Coletar Dados de 4 Pessoas.')
somaidade = 0
hvelho = 0
nomevelho = []
somaidmulher = 0
for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite o Nome: ')).strip()
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Digite o Sexo (M / F) : ')).strip().upper()
    if sexo == 'M':
        if idade > hvelho:
            hvelho = idade
            nomevelho = nome
    if sexo == 'F' and idade < 20:
        somaidmulher += 1
    somaidade += idade
medidade = somaidade / 4
print('A Média das Idades é de {:.1f} anos.'.format(medidade))
print('O Homem Mais Velho é {} com {} anos. '.format(nomevelho, hvelho))
print('No Total temos {} Mulheres Abaixo de 20 anos.'.format(somaidmulher))
