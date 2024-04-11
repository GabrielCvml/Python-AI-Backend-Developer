menu =  '''
[0] - Depósito
[1] - Saque
[2] - Extrato
[3] - Sair
'''
saldo = 0
limite_diario = 0
extrato = ""

print(f'''Seja bem vindo ao banco Dio.meBank o que você deseja fazer?
Para começar selecione uma das seguintes opções.''')

while True:
    
    if limite_diario >= 3:
        print("\nLimite de saques diários atingido!")
    if saldo <= 0:
        print("\nValor igual ou abaixo de 0 impossível realizar saque!")

    print(f"{menu}")
    escolha = int(input("Digite a opção desejada:"))

    if escolha == 0:
        print("Opção escolhida [Depósito]")
        while True:
            valor_deposito = float(input("Quantos reais deseja depositar: R$"))
            if valor_deposito < 0:
                print(f"O valor R${valor_deposito} não pode ser menor que 0! Digite novamente.")
            else:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                print("Valor depositado com sucesso!")
                break
    elif escolha == 1 and limite_diario < 3 and saldo > 0:
        print("Opção escolhida [Saque]")
        while True:
            valor_saque = float(input("Quantos reais deseja sacar: R$"))
            if valor_saque > saldo or valor_saque > 500.00:
                    if valor_saque > 500.00:
                        print("O valor do saque não pode ultrapassar R$500,00 reais")
                    else:
                        print(f"Valor selecionado R${valor_saque} é maior que o {saldo}. Por favor selecione outro valor.")
            else:
                saldo -= valor_saque
                extrato += f"R${valor_saque:.2f}\n"
                print("Valor sacado com sucesso!")
                limite_diario+=1
                break
    elif escolha == 2:
        print("Opção escolhida [Extrato]")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif escolha == 3:
        print("Opção escolhida [Sair]")
        print("Obrigado por usar os serviços da Dio.meBank")
        break