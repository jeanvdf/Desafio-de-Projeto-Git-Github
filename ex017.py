'''#Calculo hipotenusa
from math import sqrt, pow
catadj = float(input('Digite o Cateto Adjacente: '))
catop = float(input('Digite o Cateto Oposto: '))
hip = sqrt(catadj**2 + catop**2)
print('O valor da hipotenusa é {} .'.format(hip))'''
#Calculo hipotenusa
from math import hypot
catadj = float(input('Digite o Cateto Adjacente: '))
catop = float(input('Digite o Cateto Oposto: '))
hip = hypot(catadj, catop)
print('O valor de Hipotenusa é {:.2f} .'.format(hip))