# Controlando o orçamento mensal
limite = 3000.0
despesas = (float(input("Digite o total de despesas do mês (R$): ")))

if despesas < limite:
    print("Você está dentro do seu orçamento.")
else:
    print("Atenção! Você ultrapassou o limite do orçamento.")
