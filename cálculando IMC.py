Peso=float(input('Qual é o seu peso?(kg)'))
altura=float(input('Qual a sua altura?(m)'))
print('o IMC dessa pessoa é de {:.1f}'.format(Peso/(altura**2)))
IMC=Peso / (altura**2)
if IMC<18.5:
    print('Você está abaixo do peso')
elif 18.5<=IMC<25:
    print('Você está em um peso ideal')
elif 25<=IMC<30:
    print('Você está SOBREPESO')
elif 30<=IMC<40:
    print('Você está OBESIDADE')
elif IMC>=40:
    print('Você está OBESIDADE MÓRBIDA')
