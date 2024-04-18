menu = """

 [d]Depositar
 [s]Sacar
 [e]Extrato
 [q]Sair


 => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito")) 
        
        if valor > 0:
            saldo += valor
            extrato+= f"Desposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é invalido.")


    elif opcao == "s":
        valor = float(input("informe o valor do saque:"))

        execedeu_saldo = valor > saldo

        execedeu_limite = valor > limite

        execedeu_saques = numero_saques >= LIMITE_SAQUES
    
        if execedeu_saldo:
         print("Operação falhou! Você não tem saldo suficiente.")

        elif execedeu_limite:
         print("Operação falhou! Valor de saque excede o limite.")

        elif execedeu_saques:
         print("Operação falhou! Número maximo de saques exedico.")

        elif valor > 0:
         saldo -= valor
         extrato +=f"Saque: R$ {valor:.2f}\n"
         numero_saques +=1

        else:
         print("operação falhou! O valor informado é invalido.")

    elif opcao == "e":
       print("\n================Extrato============")
       print("Não foram realizadas movimentações."if not extrato else extrato)
       print(f"\nSaldo: R${saldo:.2f}")
       print("================================d")
    
    
    elif opcao == "q":
       break

    else:
       print("Operação inválida, por favor selecione novamente a operação desejada.")     



    