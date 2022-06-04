from datetime import date
ano = int(input('Digite um Ano para Saber se é Bissexto \nDigite 0 Para Analisar O Ano Atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 % 100 % 400 == 0:
    print('O Ano {} é Bissexto!'.format(ano))
else:
    print('O Ano {} não é Bissexto.'.format(ano))