for numero in range(0, 11):
    print(numero, end=" - ")
print("\n")
for numero in range(0, 51, 5):
    print(numero, end=" - ")

opcao = -1

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        print("Obrigado!")
        break

    print(f"O último número escolhido: {numero}")