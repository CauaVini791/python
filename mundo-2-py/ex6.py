#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos: MIRIM, até 14 anos: INFANTIL, até 19 anos: JÚNIOR, até 25 anos: SÊNIOR e acima de 25 anos: MASTER.
ano_nascimento=int(input("Em que ano você nasceu?"))
idade=2022-ano_nascimento
if idade<=9:
    print("Categoria MIRIM")
elif idade>9 and idade<=14:
    print("Categoria INFANTIL")
elif idade>14 and idade<=19:
    print("Categoria JÚNIOR")
elif idade>19 and idade<=25:
    print("Categoria SÊNIOR")
else:
    print("Categoria MASTER")