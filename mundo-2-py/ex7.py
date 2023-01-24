#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, um diferente e ESCALENO: todos os lados diferentes.
r1=float(input("Informe o valor do primeiro segmento:"))
r2=float(input("Informe o valor do segundo segmento:"))
r3=float(input("Informe o valor do terceiro segmento:"))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("Com esses segmentos, você pode formar um triângulo!")
    if r1==r2==r3:
        print("Os segmentos acima podem formar um triângulo EQUILÁTERO.")
    elif r1==r2!=r3 or r1==r3!=r2 or r2==r3!=r1:
        print("Os segmentos acima podem formar um triângulo ISÓSCELES.")
    else:
        print("Os segmentos acima podem formar um triângulo ESCALENO.")
else:
    print("Com esses segmentos, você não poderá formar um triângulo.")