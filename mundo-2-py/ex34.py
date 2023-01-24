#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
pessoas_mais_18=homens=mulheres=0
while True:
    idade=int(input("Informe sua idade: "))
    sexo=input("Qual o seu sexo?(M/F): ").upper()
    if idade>18:
        pessoas_mais_18+=1
    if sexo=="M":
        homens+=1
    if sexo=="F" and idade<20:
        mulheres+=1
    continuar=input("Deseja continuar?(S/N): ").upper()
    print("-"*50)
    if continuar=="S":
        continue
    else:
        break
print(f"De todas as pessoas cadastradas, apenas {pessoas_mais_18} tem menos de 18 anos.")
print(f"Foram cadastrados {homens} homens.")
print(f"De todas as mulheres cadastradas, apenas {mulheres} tem menos de 20 anos.")