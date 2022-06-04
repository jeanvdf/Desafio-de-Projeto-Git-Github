c = 1
print('Digite Numero negativo para Parar')
while True:
    tabu = int(input('Deseja Ver a Tabuada de Qual Número? '))
    if tabu < 0:
        break
    while c <= 10:
        print(f'{c:>2} x {tabu} = {c * tabu}')
        c += 1
    c = 1
print('Programa Tabuada Encerrado..')