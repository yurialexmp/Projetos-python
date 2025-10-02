salário =float(input('Qual o salário do funcionário:R$'))
if salário >=1250:
    aumento=(salário*0.10)+ salário
else:
    aumento=(salário*0.15)+ salário
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário,aumento))