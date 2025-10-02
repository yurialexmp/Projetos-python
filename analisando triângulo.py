print('-=-'* 20)
print('Analisador de triângulos')
print('-=-'* 20)
a=float(input('primeiro valor:'))
b=float(input('segundo valor:'))
c=float(input('terceiro valor:'))

if a<b+c and b<a+c and c<a+b:
    print('Com suas medidas, formará um triângulo!!!')
else:
    print('com suas medidas, NÃO formará um triângulo!!!')
