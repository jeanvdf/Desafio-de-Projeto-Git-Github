print('=-='*10)
print('CADASTRAMENTO DE DADOS')
print('=-='*10)
mais18 = hcont = menos20 = 0
r = 'S'
while True:
    while r == 'S':
        i = int(input('Digite a Idade: '))
        sexo = str(input('Digite o Sexo [M/F]: ')).upper().strip()[0]
        while sexo not in 'fMmF':
            sexo = str(input('Digite o Sexo [M/F]: ')).upper().strip()[0]
        print('-.-'*10)
        if i > 18:
            mais18 += 1
        if sexo == 'M':
            hcont += 1
        if sexo == 'F' and i < 20:
            menos20 += 1
        r = str(input('Deseja Continuar ? [S / N] : ')).strip().upper()[0]
        while r not in 'SsNn':
            r = str(input('Deseja Continuar ? [S / N] : ')).strip().upper()[0]
    break
print(f'Foram Cadastradas {mais18} pessoas com Mais de 18 Anos.')
print(f'Foram Cadastradas {hcont} homens.')
print(f'Foram Cadastradas {menos20} mulheres com menos de 20 Anos.')
