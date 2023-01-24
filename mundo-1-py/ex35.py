#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1=float(input("Informe o valor do primeiro segmento:"))
r2=float(input("Informe o valor do segundo segmento:"))
r3=float(input("Informe o valor do terceiro segmento:"))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("Com esses segmentos, você pode formar um triângulo!")
else:
    print("Com esses segmentos, você não poderá formar um triângulo.")