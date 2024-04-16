from abc import ABC, abstractmethod, abstractproperty

class ContoleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ContoleRemoto):
    def ligar(self):
        print("Ligado!")
    def desligar(self):
        print("Deligado!")
    def marca(self):
        return "LG"

class ControleArCondicionado(ContoleRemoto):
    def ligar(self):
        return super().ligar()
    def desligar(self):
        return super().desligar()
    def marca(self):
        return "LG"

controle = ControleTV()
controle1 = ControleArCondicionado()

controle.ligar()
controle.desligar()
print(controle.marca())

controle1.ligar()
controle1.desligar()
print(controle1.marca())