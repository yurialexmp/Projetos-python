n1=int(input('Primeira nota:'))
n2=int(input('Segunda nota:'))
media= (n1+n2)/2
print('Tirando a nota {} e {}, a média do aluno é {}'.format(n1,n2,media))
if 7 > media and media >=5:
    print('o aluno está  em RECUPERAÇÃO!!!!')
elif media < 5:
    print('o aluno está está REPROVADO')
elif media>=7:
    print('o aluno PASSOU!!!!')

