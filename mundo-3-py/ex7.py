#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros=[]
for c in range(0,5):
    numeros.append(float(input("Digite um número:")))
numeros.sort()
print(f"O menor número digitado foi {numeros[0]}.")
print(f"O maior número digitado foi {numeros[4]}.")