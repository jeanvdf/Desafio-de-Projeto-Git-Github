r = str(input('Qual é o Sexo ? [M/F]')).strip().upper()[0]
while r != 'M' and r != 'F':
    print('Dados Invalidos.. [M / F].\nDigite novamente seu Sexof..')
    r = str(input('Qual é o Sexo ? [M/F]')).strip().upper()[0]
print('Sexo {} Registrado com Sucesso.'.format(r))