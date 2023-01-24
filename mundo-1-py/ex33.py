#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a=int(input("Informe o primeiro número:"))
b=int(input("Informe o segundo número:"))
c=int(input("Informe o terceiro número:"))
if a>b>c:
    print("a é o maior e c é o menor")
elif a>c>b:
    print("a é o maior e b é o menor")
elif b>a>c:
    print("b é o maior e c é o menor")
elif b>c>a:
    print("b é o maior e a é o menor")
elif c>a>b:
    print("c é o maior e b é o menor")
elif c>b>a:
    print("c é o maior e a é o menor")