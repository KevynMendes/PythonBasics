class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nome, senha):
        if nome in self.usuarios:
            print("Usuário já existe!")
        else:
            self.usuarios[nome] = Usuario(nome, senha)
            print("Usuário registrado com sucesso!")

    def autenticar_usuario(self, nome, senha):
        usuario = self.usuarios.get(nome)
        if usuario and usuario.senha == senha:
            print(f"Bem-vindo, {nome}!")
        else:
            print("Nome de usuário ou senha inválidos!")

if __name__ == "__main__":
    sistema = SistemaUsuarios()

    while True:
        print("\n1. Registrar Usuário")
        print("2. Autenticar Usuário")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            sistema.registrar_usuario(nome, senha)
        elif escolha == '2':
            nome = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            sistema.autenticar_usuario(nome, senha)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
