# Faça um algoritmo que leia 10 números inteiros, armazene-os em um vetor e 
# imprima em ordem crescente.

# numeros = [0] * 10

# for i in range(len(numeros)):

#     numeros[i] = int(input("Digite um número inteiro: "))
    
# numeros.sort() # usado em listas
# print("Os números em ordem crescentes são", numeros) 



numeros = [0] * 10


for i in range(len(numeros)):
    numeros[i] = int(input("Digite um número inteiro: "))


for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]


print("Números em ordem crescente:", numeros)
