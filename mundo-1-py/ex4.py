#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.
algo=input("Digite algo:")
print("O tipo primitivo dessa coisa digitada é {}.".format(type(algo)))
print("Só tem espaços? {}".format(algo.isspace()))
print("É um número? {}".format(algo.isnumeric()))
print("É alfabético? {}".format(algo.isalpha()))
print("É alnumérico? {}".format(algo.isalnum()))
print("Está maiúscula? {}".format(algo.isupper()))
print("Está minúscula? {}".format(algo.islower()))