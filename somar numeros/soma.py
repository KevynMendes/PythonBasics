def somar_lista(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    print(f"A soma da lista é: {somar_lista(lista)}")
''