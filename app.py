"""
Desafio - Sistema Bancário (Depósito, Saque e Extrato)

Para a primeira versão precisamos implementar 3 operações: depósito, saque e extrato.

📌 Regras:
- Deve ser possível depositar valores para a conta bancária, com apenas 1 usuário.
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação do extrato.

- O sistema deve permitir realizar até 3 saques diários,
  com limite máximo de R$ 500,00 por saque.
- Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem
  informando que não será possível sacar o dinheiro por falta de saldo.
- Todos os saques devem ser armazenados em uma variável e exibidos na operação do extrato.

- A operação de extrato deve listar todos os depósitos e saques realizados na conta.
- No fim da listagem, deve ser exibido o saldo atual da conta.
- Se não houver movimentações, deve ser exibida a mensagem:
  "Não foram realizadas movimentações"
"""

# Menu principal
menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair
» """

# Variáveis principais
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 3

# Loop principal do sistema
while True:
    opcao = input(menu)

    # Depósito
    if opcao == "d":
        deposito = float(input("Insira o valor que deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato.append(f"Depósito: R$ {deposito:.2f}")
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
        else:
            print("Valor inválido! O depósito precisa ser maior que R$ 0,00.")

    # Saque
    elif opcao == "s":
        saque = float(input("Insira o valor que deseja sacar: "))

        if numero_saques >= LIMITE_SAQUE:
            print("Você já atingiu o limite de saques diários (3).")

        elif saque > limite:
            print(f"O limite por saque é de R$ {limite:.2f}.")

        elif saque > saldo:
            print("Saldo insuficiente para realizar o saque.")

        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato.append(f"Saque: R$ {saque:.2f}")
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
        else:
            print("Valor inválido! O saque precisa ser maior que R$ 0,00.")


    elif opcao == "e":
        print("\n========== EXTRATO ==========")

        if not extrato:
            print("Não foram realizadas movimentações")
        else:
            for operacao in extrato:
                print(operacao)

        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=============================\n")

    # Sair
    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário! Saindo...")
        break

    # Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
