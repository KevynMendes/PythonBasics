def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia

if __name__ == "__main__":
    n = int(input("Quantos termos da sequência de Fibonacci você deseja gerar? "))
    print(f"A sequência de Fibonacci com {n} termos é: {fibonacci(n)}")
