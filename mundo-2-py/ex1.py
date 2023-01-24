#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa=float(input("Informe o valor da casa:"))
salario=float(input("Informe seu salário:"))
anos=float(input("Em quantos anos você deseja pagar?"))
anos_meses=anos*12
mensal=valor_casa/anos_meses
if mensal<=0.3*salario: print("Empréstimo concedido.")
else: print("Empréstimo negado.")