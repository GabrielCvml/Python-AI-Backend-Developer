class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa("Gabriel", 20)
print(p.nome, p.idade)


p2 = Pessoa.criar_apartir_data_nascimento(2004, "01", 10, "Gabriel")
print(p2.nome, p2.idade)


print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(15))