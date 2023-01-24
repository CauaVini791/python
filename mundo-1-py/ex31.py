#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia=float(input("Informe a distância em km:"))
if distancia<=200:
    preço=distancia*0.50
    print("O preço da passagem fica de {} reais.".format(preço))
else:
    preço=distancia*0.45
    print("O preço da passagem fica de {} reais.".format(preço))