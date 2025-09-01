# 1. Area da Circunferencia
PI = 3.14159
raio = float(input("Digite o valor do raio: "))
area = PI * (raio ** 2)

print(f"A={area:.4f}")
print("-----------------")
################################

# 2.Classificador de Idade

idade = int(input("Digite a sua idade: "))

if 0 <= idade <= 12:
    classificacao = "Criança"
elif 13 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 59:
    classificacao = "Adulto"
elif idade >= 60:
    classificacao = "Idoso"
else:
    classificacao = "Idade inválida"

print(f"Com {idade} anos, você é classificado como: {classificacao}")
print("-----------------")
################################

# 3. Calculadora de IMC

peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")

print("-----------------")
################################

# 4. Conversor de Temperatura

temperatura = float(input("Digite o valor da temperatura: "))
unidade_origem = input("Qual a unidade de origem (C, F, K)? ").upper()
unidade_destino = input("Para qual unidade deseja converter (C, F, K)? ").upper()

temp_convertida = 0
calculado = True

if unidade_origem == "C":
    if unidade_destino == "F":
        temp_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == "K":
        temp_convertida = temperatura + 273.15
    elif unidade_destino == "C":
        temp_convertida = temperatura
    else:
        calculado = False
elif unidade_origem == "F":
    if unidade_destino == "C":
        temp_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == "K":
        temp_convertida = (temperatura - 32) * 5/9 + 273.15
    elif unidade_destino == "F":
        temp_convertida = temperatura
    else:
        calculado = False
elif unidade_origem == "K":
    if unidade_destino == "C":
        temp_convertida = temperatura - 273.15
    elif unidade_destino == "F":
        temp_convertida = (temperatura - 273.15) * 9/5 + 32
    elif unidade_destino == "K":
        temp_convertida = temperatura
    else:
        calculado = False
else:
    calculado = False

if calculado:
    print(f"{temperatura:.2f}°{unidade_origem} é igual a {temp_convertida:.2f}°{unidade_destino}")
else:
    print("Unidade de origem ou destino inválida. Use C, F ou K.")
print("-----------------")
################################

# 5. Verificador de Ano Bissexto

ano = int(input("Digite um ano para verificar se é bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    eh_bissexto = True
else:
    eh_bissexto = False

if eh_bissexto:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
print("-----------------")
################################

# 6. Calculadora de Comissão

vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas no mês: "))

comissao = total_vendas * 0.15

salario_total = salario_fixo + comissao

print(f"O funcionário {vendedor} receberá o total de: R$ {salario_total:.2f}")

print("-----------------")
################################

# 7. Calculadora Média

n1, n2, n3, n4 = map(float, input("Digite as 4 notas na mesma linha, separadas por espaço: ").split())

pesos = 2 + 3 + 4 + 1
media = (n1*2 + n2*3 + n3*4 + n4*1) / pesos

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:  # Média entre 5.0 e 6.9
    print("Aluno em exame.")

    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")

    media_final = (media + nota_exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {media_final:.1f}")

