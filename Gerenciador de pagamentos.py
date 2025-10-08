p=float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais''')
opção=int(input('Qual a opção?'))
if opção == 1:
    total= p - (p*10/100)
elif opção == 2:
    total = p -  (p * 5/100)
elif opção == 3:
    total = p
    parcela= total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = p + (p * 20/100)
    totparc = int(input('Quantas Parcelas?'))
    parcela = total / totparc
    print('Sua compra será em {}x de R${:.2f}'.format (totparc,parcela))
else:
    total = p
    print('OPERAÇÃO INVÁLIDA DE PAGAMENTO')
print('Sua compra de R${:.2f} vai custar R${:.2f} no total.'.format(p,total))



