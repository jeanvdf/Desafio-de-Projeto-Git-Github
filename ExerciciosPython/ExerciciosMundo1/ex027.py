nome = str(input('Digite Seu nome Completo: ')).strip()
dividido = nome.split()
print('O Seu primeiro nome é {}.'.format(dividido[0]))
print('O Seu ultimo nome é {}.'.format(dividido[-1]))
