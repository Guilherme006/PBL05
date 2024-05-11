# Dado um vetor A de tamanho N e um vetor B de tamanho N, crie um programa 
# que calcule a soma dos elementos desses vetores e armazene o resultado em 
# um vetor C de tamanho N. Regras:

# a. O tamanho dos vetores A, B e C é fornecido pelo usuário.
# b. Os elementos dos vetores A e B são fornecidos pelo usuário.
# c. A soma dos elementos de A[i] e B[i] deve ser armazenada em C[i].
# d. O vetor C deve ser exibido na tela após o cálculo.

# Exemplo de entrada/saída:
# Entrada:
# Tamanho dos vetores: 5
# Vetor A: 1 2 3 4 5
# Vetor B: 6 7 8 9 10
# Saída:
# Vetor C: 7 9 11 13 15



# Possibilidade de vetores com tamanhos diferentes. Se o índice de um vetor não existir no outro, soma com 0.
print("Posibilidade de vetores de tamanhos diferentes")
tamanho_vetor_A = int(input("\nDigite o número desejável para o tamanho do vetor A: "))
tamanho_vetor_B = int(input("Digite o número desejável para o tamanho do vetor B: "))


vetor_A = [0] * tamanho_vetor_A
vetor_B = [0] * tamanho_vetor_B


print("\nVetor A:")
for i in range(tamanho_vetor_A):
    vetor_A[i] = int(input("Digite um número inteiro: "))


print("\nVetor B:")
for i in range(tamanho_vetor_B):
    vetor_B[i] = int(input("Digite um número inteiro: "))


tamanho_vetor_C = max(tamanho_vetor_A, tamanho_vetor_B)  
vetor_C = [0] * tamanho_vetor_C

for i in range(tamanho_vetor_C):
    soma = (vetor_A[i] if i < tamanho_vetor_A else 0) + (vetor_B[i] if i < tamanho_vetor_B else 0)
    vetor_C[i] = soma

print("\nVetor A:", vetor_A)
print("Vetor B:", vetor_B)
print("Vetor C:", vetor_C)




# Vetores com mesmo tamanho
print("\nVetores de tamanhos iguais")
tamanho_vetor = int(input("\nDigite o número desejável para o tamanho do vetor: "))

vetor_A = [0] * tamanho_vetor
vetor_B = [0] * tamanho_vetor


print("\nVetor A:")
for i in range(tamanho_vetor):
    vetor_A[i] = int(input("Digite um número inteiro: "))


print("\nVetor B:")
for i in range(tamanho_vetor):
    vetor_B[i] = int(input("Digite um número inteiro: "))


vetor_C = [0] * tamanho_vetor  


for i in range(len(vetor_C)):
    vetor_C[i] = vetor_A[i] + vetor_B[i]

print("\nVetor A:", vetor_A)
print("Vetor B:", vetor_B)
print("Vetor C:", vetor_C)

