import json

ARQUIVO = "estoque.json"

def carregar_estoque():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open(ARQUIVO, "w") as f:
        json.dump(estoque, f, indent=4)

def adicionar_produto(nome, quantidade, preco):
    estoque = carregar_estoque()
    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    estoque.append(produto)
    salvar_estoque(estoque)
    print("✅ Produto adicionado com sucesso!")

def exibir_estoque():
    estoque = carregar_estoque()
    total_geral = 0

    if not estoque:
        print("📦 Nenhum produto no estoque.")
        return

    print("\n📋 Produtos no Estoque:")
    for i, prod in enumerate(estoque):
        total_produto = prod["quantidade"] * prod["preco"]
        total_geral += total_produto
        print(f"{i+1}. {prod['nome']} | Qtde: {prod['quantidade']} | Preço: R${prod['preco']:.2f} | Total: R${total_produto:.2f}")
    
    print(f"\n💰 Valor Total do Estoque: R${total_geral:.2f}")

def menu():
    while True:
        print("\n📦 MENU ESTOQUE")
        print("1. Adicionar Produto")
        print("2. Exibir Estoque")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            try:
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço unitário (R$): "))
                adicionar_produto(nome, quantidade, preco)
            except ValueError:
                print("❌ Entrada inválida. Tente novamente.")
        elif opcao == "2":
            exibir_estoque()
        elif opcao == "3":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()
