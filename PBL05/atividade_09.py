# Faça um algoritmo que solicita ao usuário um texto qualquer. Calcule quantas 
# vogais existem no texto. Imprima quais vogais existem no texto e quantas são.


texto = input("Digite um texto: ").lower()  # Converte o texto para minúsculas para facilitar a contagem
contador_a = contador_e = contador_i = contador_o = contador_u = 0

for letra in texto:
    if letra == 'a':
        contador_a += 1
    elif letra == 'e':
        contador_e += 1
    elif letra == 'i':
        contador_i += 1
    elif letra == 'o':
        contador_o += 1
    elif letra == 'u':
        contador_u += 1

total_vogais = contador_a + contador_e + contador_i + contador_o + contador_u

print("Quantidade total de vogais:", total_vogais)
print("Vogais presentes no texto e suas contagens:")
if contador_a > 0:
    print(f"a: {contador_a}")
if contador_e > 0:
    print(f"e: {contador_e}")
if contador_i > 0:
    print(f"i: {contador_i}")
if contador_o > 0:
    print(f"o: {contador_o}")
if contador_u > 0:
    print(f"u: {contador_u}")


