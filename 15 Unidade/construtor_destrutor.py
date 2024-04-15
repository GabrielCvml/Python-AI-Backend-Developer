class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removido")

    def falar(self):
        print("Au")
    

cao_1 = Cachorro("Pretinho","preto")
cao_1.falar()