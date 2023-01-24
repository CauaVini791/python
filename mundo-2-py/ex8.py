#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: IMC abaixo de 18,5: Abaixo do Peso, entre 18,5 e 25: Peso Ideal, 25 até 30: Sobrepeso, 30 até 40: Obesidade, acima de 40: Obesidade Mórbida.
peso=float(input("Informe seu peso:"))
altura=float(input("Informe sua altura:"))
imc=peso/(altura**2)
if imc<18.5:
    print("Seu IMC é {}. Você está abaixo do peso.".format(imc))
elif imc>=18.5 and imc<25:
    print("Seu IMC é {}. Você está com o peso ideal.".format(imc))
elif imc>=25 and imc<30:
    print("Seu IMC é {}. Você está sobrepeso.".format(imc))
elif imc>=30 and imc<40:
    print("Seu IMC é {}. Você está obeso.".format(imc))
else:
    print("Seu IMC é {}. Você está com obesidade mórbida.".format(imc))