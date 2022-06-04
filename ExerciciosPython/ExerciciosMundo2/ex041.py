from datetime import date
print('Categoria de Nadadores!!')
nasc = int(input('Digite o Ano de Nascimento : '))
anoatual = date.today().year
idade = anoatual - nasc
if 0 < idade  <= 9:
    print('O Atleta com {} anos, está na categoria \033[33;1mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print('O Atleta com {} anos, está na categoria \033[36;1mJUVENIL\033[m'.format(idade))
elif idade <= 19:
    print('O Atleta com {} anos, está na categoria \033[34;1mJUNIOR\033[m'.format(idade))
elif idade <= 20:
    print('O Atleta com {} anos, está na categoria \033[35;1mSÊNIOR\033[m'.format(idade))
elif idade > 20:
    print('O Atleta com {} anos, está na categoria \033[31;1mMASTER\033[m'.format(idade))