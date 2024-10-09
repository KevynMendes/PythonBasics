class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada.")

    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa}' removida.")
        else:
            print(f"Tarefa '{tarefa}' não encontrada.")

    def listar_tarefas(self):
        if self.tarefas:
            print("Tarefas:")
            for i, tarefa in enumerate(self.tarefas, start=1):
                print(f"{i}. {tarefa}")
        else:
            print("Nenhuma tarefa encontrada.")

def menu():
    gerenciador = GerenciadorTarefas()
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Listar Tarefas")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tarefa = input("Digite a tarefa: ")
            gerenciador.adicionar_tarefa(tarefa)
        elif escolha == '2':
            tarefa = input("Digite a tarefa a remover: ")
            gerenciador.remover_tarefa(tarefa)
        elif escolha == '3':
            gerenciador.listar_tarefas()
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
