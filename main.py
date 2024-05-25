menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
total_depositos = 0


while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        deposito = float(input("Informe o valor do deposito: "))
        if deposito > 0:
            print("Deposito efetuado com sucesso")
            extrato += f"Deposito: {deposito:.2f}\n"
            total_depositos = total_depositos + deposito
            saldo = total_depositos + saldo
        else:
            print("Valor invalido")
                
    
    elif opcao == "s":
        print("Saque")
        saque = float(input("Informe o valor do saque: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Não é possível sacar o dinheiro, limite diário atingido")
        elif saque > saldo:
            print("Não é possível sacar o dinheiro por falta de saldo")  
        elif saque > limite:
            print("O valor do saque excede o limite permitido")
        elif saque > 0:
            saldo -= saque
            numero_saques += 1  # Incrementar o número de saques
            print("Saque efetuado com sucesso")
            extrato += f"Saque: {saque:.2f}\n"

    
    elif opcao == "e":
        print("---Extrato---")
        print(f"Saldo: R${saldo:.2f}")
        print(extrato)

    elif opcao == "q":
        break

    else: print("Operação invalida, por favor selecione novamente a operação desejada.")
