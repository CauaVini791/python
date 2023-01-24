#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
km=float(input("Informe a quantidade de km percorridos:"))
dias_alugado=float(input("Informe a qauntidade de dias pelo qual o carro foi alugado:"))
valor=(dias_alugado*60)+(0.15*km)
print(f"Tendo alugado o carro por {dias_alugado} dias e andado {km}km, você terá que pagar {valor} reais.")