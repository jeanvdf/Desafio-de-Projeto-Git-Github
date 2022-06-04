dias = int(input('Quantos dias alugado ? '))
km = float(input('Quantos KM foram rodados ? '))
print('O Valor do Aluguel ficou em R${:.2f} '.format((dias*60)+(km*0.15)))