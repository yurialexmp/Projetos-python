import math
ângulo=float(input('digite o ângulo que você deseja:'))
seno=math.sin(math.radians(ângulo))
coss=math.cos(math.radians(ângulo))
tang=math.tan(math.radians(ângulo))
print('o ângulo de:{} tem o SENO de:{:.2f}'.format(ângulo,seno))
print('o ângulo de:{} tem o COSS de:{:.2f}'.format(ângulo,coss))
print('o ângulo de:{} tem a TANG de:{:.2f}'.format(ângulo,tang))

