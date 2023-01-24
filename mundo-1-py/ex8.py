#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 
metros=float(input("Informe uma medida em metros:"))
quilometro=metros/1000
hectometro=metros/100
decametro=metros/10
decimetro=metros*10
centimetro=metros*100
milimetro=metros*1000
print(f"Recebendo {metros} metros, temos que ele é equivalente a {quilometro}km, {hectometro}hm, {decametro}dam, {decimetro}dm, {centimetro}cm e {milimetro}ml.")