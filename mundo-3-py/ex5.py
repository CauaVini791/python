#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tupla=("Lápis", 1.75, 
"Borracha", 2,
"Caderno", 15.90,
"Estojo", 25,
"Transferidor", 4.50,
"Compasso", 9.99,
"Mochila", 120.32,
"Caneta", 3.30,
"Livro", 34.90)
print("LISTAGEM DE PREÇOS")
for c in range(0, len(tupla)):
    if c%2==0:
        print(f"{tupla[c]} custa",end=" ")
    else:
        print(f"{tupla[c]:.2f}")