import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Eu tenho um número entre 1 e 100. Tente adivinhá-lo!")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_adivinhacao()
