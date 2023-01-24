#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
cateto_oposto=float(input("Informe o valor do cateto oposto:"))
cateto_adjacente=float(input("Informe o valor do cateto adjacente:"))
hipotenusa=((cateto_oposto**2)+(cateto_adjacente**2))**(1/2)
print(hipotenusa)

import math
cateto_oposto=float(input("Informe o valor do cateto oposto:"))
cateto_adjacente=float(input("Informe o valor do cateto adjacente:"))
hipotenusa=math.hypot(cateto_oposto,cateto_adjacente)
print(hipotenusa)