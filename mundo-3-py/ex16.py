#Aprimore o desafio anterior, mostrando no final:                                                    
#A) A soma de todos os valores pares digitados.                                                                                                  
#B) A soma dos valores da terceira coluna.                                                                                                                
#C) O maior valor da segunda linha.
lista_números=[]
i=0
matriz=int(input("Qual a matriz? "))
matriz_1=matriz
soma_pares=0
soma_valores_terceira=0
segunda_coluna=[]
maior=0
for c in range(matriz*matriz):
    lista_números.append(float(input("Digite um número para a sua matriz: ")))
for c in range(matriz):
    for i in range(i,matriz_1):
        print([lista_números[i]], end=" ")
    i+=matriz-(matriz-1)
    matriz_1+=matriz
    print()
for c in range(len(lista_números)):
    if lista_números[c]%2==0:
        soma_pares+=lista_números[c]
print(f"A soma dos números pares digitados é igual a {soma_pares}.")
if matriz>2:
    for c in range(2,len(lista_números)+1,matriz):
        soma_valores_terceira+=lista_números[c]
    print(f"A soma dos valores da terceira coluna é igual a {soma_valores_terceira}.")
else:
    print("Não existe terceira coluna nesta matriz.")
if matriz>1:
    for c in range(matriz,matriz*2):
        segunda_coluna.append(lista_números[c])
    for c in range(len(segunda_coluna)):
        if c==0:
            maior=segunda_coluna[0]
        else:
            if segunda_coluna[c]>maior:
                maior=segunda_coluna[c]
    print(f"O maior valor da segunda linha é o {maior}.")
else:
    print("Não existe segunda linha nesta matriz.")