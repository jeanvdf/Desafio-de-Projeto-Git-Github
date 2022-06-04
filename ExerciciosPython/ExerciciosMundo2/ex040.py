print('Programa De Avaliação de Médias')
n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Parabéns!! Você Foi \033[32;1;4mAPROVADO\033[m, com a média {:.1f} .'.format(m))
elif 5 <= m < 7:
    print('Você Deve Ficar em \033[33;4;1mRECUPERAÇÃO\033[m, com a média {:.1f} .'.format(m))
else:
    print('Aluno \033[31;1;4mREPROVADO\033[m !! Sua média foi {:.1f} .'.format(m))
