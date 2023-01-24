#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
valor=(float(input("Digite um número:")),float(input("Digite um número:")),float(input("Digite um número:")),float(input("Digite um número:")))
print(f"O número 9 apareceu {valor.count(9)} vezes.")
if 3 in valor:
    (f"O número 3 está na {valor.index(3)+1} posição.")
else:
    ("O número 3 não foi digitado.")
for n in valor:
    if n%2==0:
        print(f"O número par digitado foi {n}.")