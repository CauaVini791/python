#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla='APRENDER',"PROGRAMAR","LINGUAGEM","PYTHON","CURSO","GRÁTIS","ESTUDAR","PRATICAR","TRABALHAR","MERCADO","PROGRAMADOR","FUTURO"
vogais="A","E","I","O","U"
for c in tupla:
    print(f"\nNa palavra {c} temos as vogais: ",end="")
    for letra in c:
        if letra in "AEIOU":
            print(letra.lower(),end=" ")