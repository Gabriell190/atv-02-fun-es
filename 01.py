import json
from datetime import datetime
from operator import itemgetter

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(descricao, prazo):
    tarefas = carregar_tarefas()
    tarefa = {
        "descricao": descricao,
        "prazo": prazo,
        "concluida": False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    tarefas_ordenadas = sorted(tarefas, key=itemgetter("prazo"))
    for i, t in enumerate(tarefas_ordenadas):
        status = "✅" if t["concluida"] else "❌"
        print(f"{i+1}. [{status}] {t['descricao']} (Prazo: {t['prazo']})")

def marcar_concluida(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("✅ Tarefa marcada como concluída!")
    else:
        print("❌ Índice inválido.")

def menu():
    while True:
        print("\n📋 MENU")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            desc = input("Descrição da tarefa: ")
            prazo = input("Prazo (1992-02-05): ")
            try:
                datetime.strptime(prazo, "%Y-%m-%d")  # Validação de data
                adicionar_tarefa(desc, prazo)
            except ValueError:
                print("❌ Formato de data inválido.")
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            listar_tarefas()
            try:
                indice = int(input("Número da tarefa para concluir: ")) - 1
                marcar_concluida(indice)
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcao == "4":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()
