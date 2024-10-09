def contador_palavras(texto):
    palavras = texto.split()
    return len(palavras)

if __name__ == "__main__":
    texto = input("Digite um texto: ")
    total_palavras = contador_palavras(texto)
    print(f"O total de palavras é: {total_palavras}")
