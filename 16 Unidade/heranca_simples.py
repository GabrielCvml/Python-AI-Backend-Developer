class Veiculo:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor 
        self.placa = placa
        self.nro_rodas = nro_rodas

    def ligar_motor(self):
        print("Motor ligado!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Camilhao(Veiculo):
    def __init__(self, cor, placa, nro_rodas, carregado):
        super().__init__(cor, placa, nro_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("Preta", 217933, 2)
print(moto)
moto.ligar_motor()

carro = Carro("Prata", 321322, 4)
print(carro)
carro.ligar_motor()

camilhao = Camilhao("Azul", 1324355, 8, False)
print(camilhao)
camilhao.ligar_motor()
camilhao.esta_carregado()
