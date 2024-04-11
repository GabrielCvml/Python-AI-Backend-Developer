MAIOR_DE_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "));

if idade >= MAIOR_DE_IDADE:
    print("Maior de idade!")
if idade < MAIOR_DE_IDADE:
    print("Ainda não é maior de idade!")

if idade >= MAIOR_DE_IDADE:
    print("Maior de idade!")
else:
    print("Ainda não é maior de idade!")

if idade >= MAIOR_DE_IDADE:
    print("Maior de idade!")
elif idade == IDADE_ESPECIAL:
    print("Meia idade!")
else:
    print("Ainda não é maior de idade!")

# if aninhado

if idade >= 18:
    if idade >= 18:
        print("OI")
    elif idade <= 17:
        print("OIE")
elif idade <= 17:
    if idade >= 4:
        print("OQ");
    else:
        print("minha nossa")

# if ternario

