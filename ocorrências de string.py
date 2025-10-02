'''f=str(input('digite uma frase:')).upper()
print('A letra A aparece {} vezes na frase.'.format(f.count('A')))
print('A primeira letra A aparaceu na posição:{}'.format(f.find('A')))
print('A ultima letra A apareceu na posição:{}'.format(f.rfind('A')))'''

nome=str(input('digite seu nome completo:')).strip()
nome=nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é:{}'.format(nome[0]))
print('Seu último nome é:{}'.format(nome[3]))
