import random
import string

def gerador_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    print(f"Sua senha gerada é: {gerador_senha(tamanho)}")
