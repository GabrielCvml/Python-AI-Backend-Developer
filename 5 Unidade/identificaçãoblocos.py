def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!")
    else:
        print("Valor não pode ser sacado!")

def depositar(valor):
    saldo = 100
    saldo += valor

    print(saldo);

depositar(100)
