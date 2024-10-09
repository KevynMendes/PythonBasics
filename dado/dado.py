import random

def lancar_dados(num_lancamentos):
    resultados = {i: 0 for i in range(1, 7)}
    
    for _ in range(num_lancamentos):
        resultado = random.randint(1, 6)
        resultados[resultado] += 1

    return resultados

if __name__ == "__main__":
    num_lancamentos = int(input("Quantas vezes você quer lançar o dado? "))
    resultados = lancar_dados(num_lancamentos)

    print("Resultados dos lançamentos:")
    for numero, contagem in resultados.items():
        print(f"{numero}: {contagem} vez(es)")
