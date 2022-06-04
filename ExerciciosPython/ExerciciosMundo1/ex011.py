l = float(input('Qual é a largura da parede (m)? '))
h = float(input('Qual é a altura da parede (m)? '))
a = l*h
print('A área de parede é {} m² e são necessários {:.2} L de tinta para pinta-la'.format(a, a/2))