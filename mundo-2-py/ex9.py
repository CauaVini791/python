#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto, à vista no cartão: 5% de desconto, em até 2x no cartão: preço formal , 3x ou mais no cartão: 20% de juros.
preço_produto=float(input("Qual o valor do produto?"))
print('''Agora, escolha a sua forma de pagamento:
[1] à vista dinheiro/cheque: 10% de desconto;
[2] à vista no cartão: 5% de desconto;
[3] em até 2x no cartão: preço formal; 
[4] 3x ou mais no cartão: 20% de juros.''')
forma_pagamento=int(input("Qual a forma de pagamento?"))
if forma_pagamento==1:
    valor=preço_produto-(preço_produto*0.1)
    print(f"Você irá pagar {valor} reais nesse produto.")
elif forma_pagamento==2:
    valor=preço_produto-(preço_produto*0.05)
    print(f"Você irá pagar {valor} reais nesse produto.")
elif forma_pagamento==3:
    print(f"Você irá pagar {preço_produto} reais nesse produto.")
else:
    valor=preço_produto+(preço_produto*0.2)
    print(f"Você irá pagar {valor} reais nesse produto.")