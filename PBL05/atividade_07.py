# Faça um programa que calcule e mostre a soma dos 50 primeiros números 
# pares.

soma = 0

for numero in range(0, 101, 2):  
    soma += numero

print("A soma dos 50 primeiros números pares é:", soma)


