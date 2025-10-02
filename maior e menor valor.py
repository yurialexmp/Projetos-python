v1=int(input('Primeiro valor:'))
v2=int(input('Segundo valor:'))
v3=int(input('Terceiro valor:'))
if v1<v2 and v1<v3:
    menor=v1
if v2<v3 and v2<v1:
    menor=v2
if v3<v1 and v3<v2:
    menor=v3
#verificando número maior
if v1>v2 and v1>v3:
    maior=v1
if v2>v3 and v2>v1:
    maior=v2
if v3>v1 and v3>v2:
    maior=v3
print('o menor valor digitado foi:{}'.format(menor))
print(f'o maior valor digitado foi:{maior}')


