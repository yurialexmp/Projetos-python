velocidade=int(input('Qual a a velocidade atual do carro:'))
if velocidade > 80:
    multa=(velocidade-80)*7
    print('MULTADO!!! Você ultrapassou o limite que é de 80km/h')
    print('VocÊ deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia!!!!')

