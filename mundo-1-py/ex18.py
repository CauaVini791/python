#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo=float(input("Informe um ângulo:"))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print("O ângulo {} tem {:.2f} como seu seno, {:.2f} como seu cosseno e {:.2f} sendo sua tangente.".format(angulo,seno,cosseno,tangente))