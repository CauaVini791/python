#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
abertos=0
fechados=0
expressão=input("Digite a expressão:")
for c in expressão:
    if c=="(":
        abertos+=1
    elif c==")":
        fechados+=1
if abertos==fechados:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")