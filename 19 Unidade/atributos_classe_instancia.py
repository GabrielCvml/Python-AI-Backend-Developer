class Estudante:
    escola = "DIO"

    def __init__(self,nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero}) - ({self.escola})"

def  mostrar_valor(*objs):
    for obj in objs:
        print(obj)

a_1 = Estudante("Gabriel", 13432)
a_2 = Estudante("Gabriela", 54312)

mostrar_valor(a_1 , a_2)


Estudante.escola = "Python"
a_3 = Estudante("Marcos", 24324)
a_2.numero = 3
mostrar_valor(a_1, a_2, a_3)

