def calcular_fibonacci(quantidade):
    fib_sequence = [0, 1]
    
    for _ in range(2, quantidade):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence

def pertence_fibonacci(numero, fib_sequence):
    return numero in fib_sequence

#
quantidade = 20  
fib_sequence = calcular_fibonacci(quantidade)


print(f"Sequência de Fibonacci (até {quantidade} números): {fib_sequence}")


numero_informado = int(input("Informe um número: "))


if pertence_fibonacci(numero_informado, fib_sequence):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")