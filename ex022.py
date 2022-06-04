nome = str(input('Qual é o seu nome completo ? '))
print('O seu nome em Maiusculas é :')
print(nome.upper())
print('O seu nome em minusculas é :')
print(nome.lower())
print('O Seu nome tem {} caracteres'.format(len(''.join(nome.split()))))
dividido = nome.split()
print('O Seu primeiro nome tem {} caracteres'.format(len(dividido[0])))

