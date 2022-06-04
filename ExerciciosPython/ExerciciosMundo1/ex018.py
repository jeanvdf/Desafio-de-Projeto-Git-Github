from math import cos, sin, tan, radians
ang = float(input('Digite um Angulo Qualquer: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print('O Valor do Seno é {:.2f}, Cosseno {:.2f} e a Tangente {:.2f}. '.format(seno, cos, tg))