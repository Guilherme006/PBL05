# Ler 10 números e imprimir quantos são pares e quantos são ímpares.

par = 0
impar = 0

for i in range(1,11):

    i = int(input("Digite um número: "))

    if i % 2 == 0:
        par += 1    
    else:
        impar += 1
        

print(f"A quantidade de números pares é {par}")
print(f"A quantidade de números ímpares é {impar}")