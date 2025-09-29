alug=int(input('Quantos dias alugado?:'))
km=float(input('quantos km rodados?:'))
pago=(alug*60) + (km*0.15)
print('o total a pagar em dias é:R${}'.format(pago))
