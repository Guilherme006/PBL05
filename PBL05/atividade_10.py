# Dado um vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete 
# mais vezes.

vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

numero_mais_repetido = None
quantidade_mais_repetida = 0

for numero in vetor:
    quantidade = vetor.count(numero)
    if quantidade > quantidade_mais_repetida:
        numero_mais_repetido = numero
        quantidade_mais_repetida = quantidade

print("O número que se repete mais vezes é:", numero_mais_repetido)

