#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade=float(input("Informe a velocidade do carro:"))
if velocidade>80:
    multa=7*(velocidade-80)
    print("Você excedeu o limite de 80km/h e, consequentemente, foi multado em {} reais.".format(multa))
else:
    print("Parbéns por fazer o mínimo andando na velocidade certa.")