from datetime import date
ano=int(input('Qual ano quer analisar? Coloque o 0 para analisar o ano atual:'))
if ano==0:
    ano=date.today().year
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('Seu ano {} é bissexto.'.format(ano))
else:
    print('seu ano {} não é bissexto.'.format(ano))
