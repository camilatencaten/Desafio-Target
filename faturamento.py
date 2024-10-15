import json

def calcular_faturamento(faturamento_diario):
    valores = [entrada["valor"] for entrada in faturamento_diario if entrada["valor"] > 0]

    if not valores:
        return None, None, 0  

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)

    dias_superiores_media = sum(1 for valor in valores if valor > media)
    
    return menor, maior, dias_superiores_media

with open('faturamento.json', 'r') as f:
    faturamento_diario = json.load(f)

menor, maior, dias_superiores_media = calcular_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_superiores_media}")