sal = float(input('Qual o Valor do Salário? R$ '))
if sal >= 1250:
    print('O Aumento do Salário Será de 10% \nO Seu novo Salário é R$ {:.2f} .'.format(sal + sal*0.10))
else:
    print('O Aumento do Salário Será de 15% \nO Seu novo Salário é R$ {:.2f} .'.format(sal + sal*0.15))
