l1=float(input('Primeiro segmento:'))
l2=float(input('segundo segmento:'))
l3=float(input('terceiro segmento:'))
if l1 < l2 +l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('os segmentos   PODEM FORMAR um triângulo')
    if l1 == l2 == l3:
      print('seu triângulo é EQUILÁTERO')
    elif l1 != l2 != l3 !=l1:
        print('seu triângulo é um ESCALENO')
    else:
        print('seu triângulo é im ISOSCELES')
else:
    print('seu segmentos NÃO PODE FORMAR um triângulo!!!!')
