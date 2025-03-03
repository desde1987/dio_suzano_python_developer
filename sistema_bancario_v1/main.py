# Desafio Sistema Bancário - Versão 01


import os
from datetime import date

menu = """
SISTEMA BANCÁRIO V1
-------------------

Comandos:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

Selecione uma opção: 
"""

LIMITE_SAQUES_DIARIOS = 3
LIMITE_SAQUE_VALOR = 500

# a variável "movimentacoes" é uma lista de tuplas.
# cada tupla deve possuir os seguintes itens: operação | data | valor
# por meio das movimentações vamos guardar os dados necessários para o
# montar o extrato e também para controlar o saldo.
movimentacoes = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("Pressione <ENTER> para continuar...")
    clear()


def obter_saldo():
    total = 0
    for mov in movimentacoes:
        total += mov[2]
    return total


def saque_permitido():
    count = 0
    for mov in movimentacoes:
        if mov[1] == date.today() and mov[0] == "s":
            count += 1
    return True if count < LIMITE_SAQUES_DIARIOS else False


def numero_valido(input: str):
    input = input.replace(".", "")
    return input.isnumeric()


def depositar():
    valor = input("Informe valor: ")
    valor = float(valor) if numero_valido(valor) else None
    if (valor == None) or (valor <= 0):
        print("Valor inválido.")
        return
    movimentacoes.append(("d", date.today(), valor))


def sacar():
    if not saque_permitido():
        print("Limite de saques diários excedido.")
        return
    valor = input("Informe valor: ")
    valor = float(valor) if numero_valido(valor) else None
    if (valor == None) or (valor <= 0):
        print("Valor inválido.")
        return
    if valor > LIMITE_SAQUE_VALOR:
        print("Valor de saque excede to limite permitido na operação.")
        return
    if valor > obter_saldo():
        print("Saldo insuficiente para esta operação de saque.")
        return
    movimentacoes.append(("s", date.today(), valor * -1))


def extrato():
    print("EXTRATO DA CONTA")
    if len(movimentacoes) > 0:
        print("Movimentações:")
    for mov in movimentacoes:
        print(f"Operação: [{mov[0]}] Data: [{mov[1]}] Valor: [R$ {mov[2]}]")
    print(f"Saldo: R$ {obter_saldo()}")


def sair():
    os.sys.exit()


def main():
    while True:
        opcao = input(menu)
        match opcao:
            case "d":
                clear()
                depositar()
                pause()
            case "s":
                clear()
                sacar()
                pause()
            case "e":
                clear()
                extrato()
                pause()
            case "q":
                clear()
                sair()
            case _:
                clear()
                print("Opção inválida.")


if __name__ == "__main__":
    main()
