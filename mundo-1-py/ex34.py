#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario=float(input("Informe o seu salário:"))
if salario>1250:
    novo_salario=salario+(salario*0.1)
    print("Com o aumento de 10%, seu salário ficará de {}.".format(novo_salario))
else:
    novo_salario=salario+(salario*0.15)
    print("Com o aumento de 15%, seu salário ficará de {}.".format(novo_salario))