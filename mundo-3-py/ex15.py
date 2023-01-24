#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
lista_números=[]
i=0
matriz=int(input("Qual a matriz? "))
matriz_1=matriz
for c in range(matriz*matriz):
    lista_números.append(float(input("Digite um número para a sua matriz: ")))
for c in range(matriz):
    for i in range(i,matriz_1):
        print([lista_números[i]], end=" ")
    i+=matriz-(matriz-1)
    matriz_1+=matriz
    print()