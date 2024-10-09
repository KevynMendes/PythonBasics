def conversor_moedas(valor_usd):
    taxa_cambio = 5.25  # Exemplo: 1 USD = 5.25 BRL
    valor_brl = valor_usd * taxa_cambio
    return valor_brl

if __name__ == "__main__":
    valor_usd = float(input("Digite o valor em USD: "))
    print(f"O valor em BRL é: {conversor_moedas(valor_usd):.2f} BRL")
