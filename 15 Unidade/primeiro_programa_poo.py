'''
João tem uma bicicletaria e gostaria de registrar as vendas de suas biciclentas. Crie um programa onde João informa: cor, modelo, ano, e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

'''

class Bicicleta:

    def __init__(self, cor, modelo, ano, valor, estado="Parado"):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.estado = estado
    
    def buzinar(self):
        print("BIBIIIIIIIII!")

    def parar(self):
        self.estado = "Parado"
        print(self.estado)

    def correr(self):
        self.estado = "Em movimento"
        print(self.estado)

    def get_cor(self):
        return self.cor
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


caloi = Bicicleta("Vermelha","Caloi Arbo", 2009, 2.000)
caloi_1 = Bicicleta("Azul", "Caloi Speed", 2012, 3.000, "Andado")

print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor, caloi.estado)
print(caloi.estado)
caloi.correr()
caloi_1.buzinar()
caloi_1.parar()
print(caloi.get_cor())
print(caloi)
