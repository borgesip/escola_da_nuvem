# Verificador de Senhas

print("--- Verificador de Senha Forte ---")
print("Critérios: Mínimo 8 caracteres e pelo menos um número.")
print("Digite 'sair' para encerrar.")

while True:
    senha = input("\nCrie sua senha: ")

    if senha.lower() == 'sair':
        print("Operação cancelada.")
        break

    comprimento_ok = len(senha) >= 8
    tem_numero = False

    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    if comprimento_ok and tem_numero:
        print("✅ Senha forte e aceita com sucesso!")
        break
    else:
        print("❌ Senha fraca. Verifique os critérios:")
        if not comprimento_ok:
            print("- Deve ter pelo menos 8 caracteres.")
        if not tem_numero:
            print("- Deve conter pelo menos um número.")
