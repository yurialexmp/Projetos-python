salário=float(input('qual o salario do funcionário?R$'))
reajuste= salário + (salário * 15/100)
print('Um funcionário que ganhava R${}, com o aumento de 15% de aumento , passa a receber R${:.2f}'.format(salário,reajuste))