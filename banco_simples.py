print("Bem-vindo ao Banco Richard's Finance\n")

menu = """
Escolha uma opcao:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()
    
    if opcao == "d":
        print("Depositar".center(20, "#"))
        
        valor = float(input("Digite o valor do depósito: "))
        
        if valor > 0:	
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!")
            
        else:
            print("Valor inválido")
        
    elif opcao == "s":
        print("Sacar".center(20, "#"))
    
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor do saque: "))
            
            if valor > limite_diario:
                print("O valor ultrapassa o limite para saque")
                continue
            
            elif valor > saldo:
                print("Saldo insuficiente")
                
            else:  
                saldo -= valor
                extrato += f"Saque de R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} efetuado com sucesso!")
        
        else:
            print("Limite de saques diários atingido")
    
    elif opcao == "e":
        print("Extrato".center(20, "#"))
        if extrato == "":
            print("Nenhuma movimentação realizada")
        else:
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
    
    elif opcao == "q":
        print("Sair")
        print("Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente")