def inverter_string(texto):
    string_invertida = ""
    
    # Percorre a string de trás para frente
    for i in range(len(texto) - 1, -1, -1):
        string_invertida += texto[i]
        
    return string_invertida

# Solicita uma string ao usuário
texto_informado = input("Informe uma string para inverter: ")

# Inverte a string
resultado = inverter_string(texto_informado)

# Exibe o resultado
print(f"String invertida: {resultado}")