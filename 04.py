import json
import os
from datetime import datetime

ARQUIVO = "usuarios.json"

def carregar_usuarios():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    else:
        return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)

def criar_conta(username, senha):
    usuarios = carregar_usuarios()
    if username in usuarios:
        print("❌ Usuário já existe.")
        return
    usuarios[username] = {
        "senha": senha,
        "saldo": 0.0,
        "transacoes": []
    }
    salvar_usuarios(usuarios)
    print("✅ Conta criada com sucesso!")

def login(username, senha):
    usuarios = carregar_usuarios()
    if username in usuarios and usuarios[username]["senha"] == senha:
        print(f"✅ Bem-vindo, {username}!")
        return username
    else:
        print("❌ Usuário ou senha inválidos.")
        return None

def registrar_transacao(usuario, tipo, valor):
    usuarios = carregar_usuarios()
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    usuarios[usuario]["transacoes"].append({
        "tipo": tipo,
        "valor": valor,
        "data": data
    })
    salvar_usuarios(usuarios)

def depositar(usuario, valor):
    usuarios = carregar_usuarios()
    usuarios[usuario]["saldo"] += valor
    salvar_usuarios(usuarios)
    registrar_transacao(usuario, "Depósito", valor)
    print(f"💰 Depósito de R${valor:.2f} realizado.")

def sacar(usuario, valor):
    usuarios = carregar_usuarios()
    if usuarios[usuario]["saldo"] >= valor:
        usuarios[usuario]["saldo"] -= valor
        salvar_usuarios(usuarios)
        registrar_transacao(usuario, "Saque", valor)
        print(f"💸 Saque de R${valor:.2f} realizado.")
    else:
        print("❌ Saldo insuficiente.")

def extrato(usuario):
    usuarios = carregar_usuarios()
    print(f"\n📄 Extrato de {usuario}")
    for t in usuarios[usuario]["transacoes"]:
        print(f"{t['data']} | {t['tipo']} | R${t['valor']:.2f}")
    print(f"Saldo atual: R${usuarios[usuario]['saldo']:.2f}")

def menu_principal():
    while True:
        print("\n🏦 SISTEMA BANCÁRIO")
        print("1. Criar Conta")
        print("2. Login")
        print("3. Sair")
        op = input("Escolha uma opção: ")

        if op == "1":
            u = input("Novo usuário: ")
            s = input("Senha: ")
            criar_conta(u, s)
        elif op == "2":
            u = input("Usuário: ")
            s = input("Senha: ")
            logado = login(u, s)
            if logado:
                menu_usuario(logado)
        elif op == "3":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida.")

def menu_usuario(usuario):
    while True:
        print(f"\n🔐 MENU DE {usuario}")
        print("1. Depósito")
        print("2. Saque")
        print("3. Ver Extrato")
        print("4. Sair")
        op = input("Escolha uma opção: ")

        if op == "1":
            try:
                v = float(input("Valor do depósito: "))
                depositar(usuario, v)
            except:
                print("❌ Entrada inválida.")
        elif op == "2":
            try:
                v = float(input("Valor do saque: "))
                sacar(usuario, v)
            except:
                print("❌ Entrada inválida.")
        elif op == "3":
            extrato(usuario)
        elif op == "4":
            print("🔓 Logout realizado.")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu_principal()
