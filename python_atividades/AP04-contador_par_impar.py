# Contador de Pares e Impares

qtd_pares = 0
qtd_impares = 0

print("--- Contador de Pares e Ímpares ---")
print("Digite números inteiros. Digite 'fim' para ver o resultado.")

while True:
    entrada = input("Digite um número: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"{numero} é Par.")
            qtd_pares += 1
        else:
            print(f"{numero} é Ímpar.")
            qtd_impares += 1

    except ValueError:
        print("❌ Entrada inválida. Por favor, insira um número INTEIRO ou 'fim'.")

print("\n--- Relatório Final ---")
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")
