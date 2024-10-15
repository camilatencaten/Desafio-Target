def calcular_percentuais(faturamento_estados):
    total = sum(faturamento_estados.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}
    return total, percentuais

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento, percentuais = calcular_percentuais(faturamento_estados)

print(f"Total de faturamento mensal: R${total_faturamento:.2f}")
print("Percentual de faturamento por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")