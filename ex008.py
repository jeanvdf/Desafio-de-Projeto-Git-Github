m = float(input('Digite um valor em metros: '))
print('A medida {:.0f}m corresponde a {:.0f}cm, {:.0f} mm, {:.0f}dm, {}dam, {}hm e {}km '.format(m, m*100, m*1000, m*10, m/10, m/100, m/1000))