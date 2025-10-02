distância=float(input('Qual a distância da viagem:'))
if distância <= 200:
    km= (distância * 0.50)
else:
    km= (distância * 0.45)
print('Você está prestes a começar uma viagem de:{:.2f}km'.format(distância))
print('E o preço da sua passagem será de:R${:.2f}'.format(km))



