import json
import os

ARQUIVO = "assentos.json"
LINHAS = 5
COLUNAS = 6

def criar_assentos_vazios():
    return [["O" for _ in range(COLUNAS)] for _ in range(LINHAS)]

def carregar_assentos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    else:
        assentos = criar_assentos_vazios()
        salvar_assentos(assentos)
        return assentos

def salvar_assentos(assentos):
    with open(ARQUIVO, "w") as f:
        json.dump(assentos, f)

def exibir_mapa(assentos):
    print("\n🎟️  Mapa de Assentos (O = Livre, X = Reservado):")
    print("   " + " ".join([str(i+1) for i in range(COLUNAS)]))
    for i, linha in enumerate(assentos):
        print(f"{i+1}  " + " ".join(linha))

def reservar_assento(linha, coluna):
    assentos = carregar_assentos()
    if assentos[linha][coluna] == "X":
        print("❌ Assento já reservado!")
    else:
        assentos[linha][coluna] = "X"
        salvar_assentos(assentos)
        print("✅ Reserva realizada com sucesso!")

def cancelar_reserva(linha, coluna):
    assentos = carregar_assentos()
    if assentos[linha][coluna] == "O":
        print("❌ Este assento já está livre!")
    else:
        assentos[linha][coluna] = "O"
        salvar_assentos(assentos)
        print("✅ Reserva cancelada com sucesso!")

def menu():
    while True:
        print("\n📅 MENU RESERVAS")
        print("1. Visualizar Mapa de Assentos")
        print("2. Reservar Assento")
        print("3. Cancelar Reserva")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_mapa(carregar_assentos())
        elif opcao == "2":
            try:
                l = int(input("Linha (1 a 5): ")) - 1
                c = int(input("Coluna (1 a 6): ")) - 1
                reservar_assento(l, c)
            except:
                print("❌ Entrada inválida.")
        elif opcao == "3":
            try:
                l = int(input("Linha (1 a 5): ")) - 1
                c = int(input("Coluna (1 a 6): ")) - 1
                cancelar_reserva(l, c)
            except:
                print("❌ Entrada inválida.")
        elif opcao == "4":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()
