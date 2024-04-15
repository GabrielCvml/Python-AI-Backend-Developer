class Animal:
    def __init__(self, nome, nro_patas):
        self.nome = nome
        self.nro_patas = nro_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelos, **kw):       
        self.cor_pelos = cor_pelos
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Onitorrinco(Mamifero,Ave):
    def __init__(self, cor_bico, cor_pelos, nro_patas, nome):
        super.__init__(cor_pelos=cor_pelos, cor_bico=cor_bico, nro_patas=nro_patas, nome=nome)
        

gato = Gato(nome="Gato-Domestico",nro_patas="4", cor_pelos="Laranja")
print(gato)

o = Onitorrinco(nome="Ornithorhynchus anatinus", nro_patas=2, cor_pelos="Marrom escuro", cor_bico="Laranja")

print(o)