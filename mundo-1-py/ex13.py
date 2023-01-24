#Faça um algorítimo que leia o salário de um funcionário e mostre seu novo saláreio, com 15% de aumento.
salario=float(input("Informe o salário do funcionário:"))
aumento=salario*0.15
novo_salario=salario+aumento
print(f"Com 15% de aumento, o novo salário desse funcionário ficará de {novo_salario}.")