print('\033[32;1m Programa de Alistamento Militar \033[m')
nome = str(input('Qual é o Seu Nome ? '))
a = int(input('Qual seu Ano de Nascimento ? '))
from datetime import date
anoatual = date.today().year
if anoatual - a < 18:
    print('Você tem {} anos e Ainda irá se alistar ao serviço militar.'.format(anoatual - a))
    print('Você deverá se alistar daqui {} anos em {}.'.format(18 - (anoatual - a), a + 18))
elif anoatual - a == 18:
    print('Você tem {} anos E Deve se Alistar este ano ao serviço militar.'.format(anoatual - a))
else:
    print('Voce Já Passou do Período de Alistamento Militar.')
    print('Voce deveria ter Se Alistado {} anos Atrás em {}.'.format((anoatual - a) - 18, a + 18))
