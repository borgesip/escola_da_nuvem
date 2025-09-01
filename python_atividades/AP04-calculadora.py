# Calculadora

while True:
    print("\n--- Calculadora Python ---")
    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        resultado = 0
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")

        print(f"\n✅ Resultado: {num1} {operador} {num2} = {resultado}")
        break

    except ValueError as e:
        print(f"\n❌ Erro de Entrada: Por favor, insira números válidos e um dos operadores permitidos (+, -, *, /).")
    except ZeroDivisionError:
        print(f"\n❌ Erro Matemático: Não é possível dividir por zero.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
