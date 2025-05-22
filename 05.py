import json
import os

ARQUIVO = "contatos.json"

def carregar_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_contatos(contatos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=4, ensure_ascii=False)

def adicionar_contato():
    print("\n📞 Novo Contato")
    nome = input("Nome completo: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    if not nome or not telefone:
        print("❌ Nome e telefone são obrigatórios!")
        return

    contatos = carregar_contatos()
    contatos.append({
        "nome": nome,
        "telefone": telefone,
        "email": email
    })
    salvar_contatos(contatos)
    print(f"✅ Contato de {nome} salvo com sucesso!")

def buscar_contato():
    termo = input("\n🔍 Digite o nome para buscar: ").strip().lower()
    contatos = carregar_contatos()

    encontrados = [c for c in contatos if termo in c['nome'].lower()]

    if encontrados:
        print("\n📋 Contatos encontrados:")
        for i, c in enumerate(encontrados, 1):
            print(f"{i}. {c['nome']}")
            print(f"   📱 Telefone: {c['telefone']}")
            print(f"   📧 Email: {c['email']}\n")
    else:
        print("😕 Nenhum contato com esse nome foi encontrado.")

def menu():
    while True:
        print("\n==============================")
        print("📇 GERENCIADOR DE CONTATOS")
        print("==============================")
        print("1. Adicionar novo contato")
        print("2. Buscar contato pelo nome")
        print("3. Sair")
        print("==============================")

        escolha = input("O que você deseja fazer? ")

        if escolha == "1":
            adicionar_contato()
        elif escolha == "2":
            buscar_contato()
        elif escolha == "3":
            print("👋 Até logo! Seus contatos estarão guardados com carinho.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
