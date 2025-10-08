from datetime import date
atual= date.today().year
ano=int(input('Data de nascimento:'))
idade= atual- ano
print('o atleta tem {} anos'.format(idade))
if idade<=9:
    print('a classificação do atleta é MIRIM')
elif idade<=14:
    print('a classificação do atleta é INFANTIL')
elif idade<=19:
    print('a classificação do atleta é JUNIOR')
elif idade<=25:
    print('a classificação do atleta é SÊNIOR')
elif idade>25:
    print('a classificação do atleta é MASTER')




