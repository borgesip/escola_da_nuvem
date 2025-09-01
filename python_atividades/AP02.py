# 1. Conversor de Moedas
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

print(f"Valor em Reais: R$ {valor_reais:.2f}")
print("--- Valores Convertidos ---")
print(f"Valor em Dólares: US$ {valor_dolares:.2f}")
print(f"Valor em Euros: € {valor_euros:.2f}")

print("------------------------")

########################################

# 2. Calculadora de Desconto

nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto de {percentual_desconto}%: R$ {valor_desconto:.2f}")
print("--------------------------")
print(f"Preço Final: R$ {preco_final:.2f}")


print("------------------------")

########################################

# 3. Calculadora de Media Escolar

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("--- Média Escolar ---")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print("---------------------")
print(f"Média Final: {media:.2f}")
print("------------------------")

########################################

# 4. Calculadora de Consumo de Combustivel

distancia_percorrida = 300
combustivel_gasto = 25

consumo_medio = distancia_percorrida / combustivel_gasto

print("--- Relatório de Viagem ---")
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print("---------------------------")
print(f"Consumo Médio: {consumo_medio:.2f} km/l")
print("------------------------")

########################################

# 5. Calculadora de Soma com Entrada do Usuário

A = int(input("Digite o primeiro valor inteiro: "))
B = int(input("Digite o segundo valor inteiro: "))

X = A + B

print("X =", X)
print("------------------------")

########################################

# 6. Calculadora de salário por horas trabalhadas

numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

salario = horas_trabalhadas * valor_por_hora

print("NÚMERO =", numero_funcionario)
print(f"SALÁRIO = R$ {salario:.2f}")
print("------------------------")

########################################
