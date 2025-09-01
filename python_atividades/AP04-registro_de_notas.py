# Registro de Notas

notas_validas = []

print("--- Sistema de Registro de Notas ---")
print("Digite as notas dos alunos (0 a 10). Digite 'fim' para terminar.")

while True:
    entrada = input("Digite a próxima nota: ")

    if entrada.lower() == 'fim':
        break  # Sai do loop

    try:
        nota = float(entrada)

        if 0 <= nota <= 10:
            notas_validas.append(nota)
            print(f"Nota {nota} adicionada com sucesso.")
        else:
            print("❌ Erro: A nota deve estar entre 0 e 10. Tente novamente.")

    except ValueError:
        print("❌ Erro: Entrada inválida. Por favor, insira um número ou 'fim'.")

if notas_validas:
    media = sum(notas_validas) / len(notas_validas)
    print("\n--- Resultados Finais ---")
    print(f"Total de notas registradas: {len(notas_validas)}")
    print(f"A média da turma é: {media:.2f}")
else:
    print("\nNenhuma nota válida foi registrada.")
