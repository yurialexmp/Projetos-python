'''co=float(input('Comprimento do cateto oposto:'))
ca=float(input('comprimento do cateto adjacente:'))
hi=(co**2 +ca**2) ** (1/2)
print('a hipotenusa vai medir:{:.2f}'.format(hi))'''

#import math
#co=float(input('cumprimento do cateto oposto:'))
#ca=float(input('cumprimento do cateto adjacente:'))
#h1=math.hypot(co,ca)
#print('a hipotenusa vai medir:{:.2f}'.format(h1))

from math import hypot
co=float(input('Comprimento do cateto oposto:'))
ca=float(input('comprimento do cateto adjacente:'))
hi=hypot(co,ca)
print('a hipotenusa vai medir:{:.2f}'.format(hi))

#3 formas de fazer calculo da hipotenusa 

