# Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a
# tabuada de 1 a 10 do valor lido.

numero = int(input("Digite um número de 1 a 10: "))

for i in range(1,11):

    if numero <= 10:
        print(f"{numero} x {i} = {numero * i}")

if numero > 10:
    print("Número inválido. Digite um número de 1 a 10!")
