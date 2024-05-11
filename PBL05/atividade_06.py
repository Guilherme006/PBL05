# Utilizando a estrutura de repetição for, faça um programa que receba 10 
# números e conte quantos deles estão no intervalo [10,20] e quantos deles 
# estão fora do intervalo.


dentro_intervalo = 0
fora_intervalo = 0


for i in range(10):
    numero = float(input("Digite um número: "))
    
   
    if numero >= 10 and numero <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1


print("Quantidade de números dentro do intervalo [10,20]:", dentro_intervalo)
print("Quantidade de números fora do intervalo [10,20]:", fora_intervalo)
