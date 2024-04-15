import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Valor depositado")
    else:
        print("ERRO, Valor não pode ser depositado!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Valor de saque não pode ser maior que o saldo")
    elif valor > limite:
        print("O limite de saque é de R$500.00!")
    elif numero_saques >= limite_saques:
        print("Limite de saques diários atingidos! Tente mais tarde.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        print("Valor sacado com sucesso!")
        numero_saques += 1
    else:
        print("ERRO, operação invalidada.")
    
    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def nova_conta(agencia, numero_conta, usuarios):
        cpf = input("Infome seu CPF: ")
        usuario = filtro_usuarios(cpf, usuarios)
        if usuario:
            print("conta criada")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        else:
            print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def novo_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuarios:
        print("Usuário já se encontra no sistema!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtro_usuarios(cpf, usarios):
    usarios_filtrado = [usuario for usuario in usarios if usuario["cpf"] == cpf]
    return usarios_filtrado[0] if usarios_filtrado else None

def main():
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao  = menu()

        if opcao == "1":
            valor = float(input("Coloque o valor a ser depositado: R$"))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: R$"))
            saldo, extrato = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES,)
        elif opcao == "3":
             extrato(saldo, extrato=extrato)
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta: contas.append(conta)
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6":
            novo_usuario(usuarios)
        elif opcao == "7":
            print("Obrigado por usar nossos serviços!")
            break
        else:
            print("OPÇÃO INEXISTENTE!")
        