#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idades=0
media_idade=0
mulheres_menos_20=0
nome_mais_velho=0
mais_velho=0
for c in range(0,4):
    nome=input("Qual o seu nome?")
    idade=int(input("Qual a sua idade?"))
    sexo=input("Qual o seu sexo (MASCULINO ou FEMININO)?").upper()
    soma_idades=soma_idades+idade
    if sexo==str("FEMININO") and idade<20:
        mulheres_menos_20=mulheres_menos_20+1
    elif sexo==str("MASCULINO"):
        if c==0:
            nome_mais_velho=nome
            mais_velho=idade
        else:
            if idade>mais_velho:
                nome_mais_velho=nome
                mais_velho=idade
media_idade=soma_idades/4
print(f"A média de idade desse grupo é {media_idade}.")
print(f"O homem mais velho é {str(nome_mais_velho)} com {mais_velho} anos.")
print(f"O número de mulheres com menos de 20 anos é {mulheres_menos_20}.")