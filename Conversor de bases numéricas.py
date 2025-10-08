num=int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL  
[ 3 ] converter para HEXADECIMAL''')
opção=int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para BINARIO é igual {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual {}'.format(num,oct(num)))
else:
    print('{} convertido para HEXADECIMAL é igual {}'.format(num,hex(num)))

