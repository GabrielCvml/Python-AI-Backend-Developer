nome, idade, profissoa, linhagem =  "Gabriel", 20, "Programador", "Python"

print("Ola meu nome é %s. Tenho %i anos, trabalho como %s, com a linguagem %s" %(nome, idade, profissoa, linhagem))
print("Ola meu nome é {}. Tenho {} anos, trabalho como {}, com a linguagem {}".format(nome, idade, profissoa, linhagem))
print(f"Ola meu nome é {nome}. Tenho {idade} anos, trabalho como {profissoa}, com a linguagem {linhagem}")
print("Ola meu nome é {name}. Tenho {age} anos, trabalho como {work}, com a linguagem {language}".format(name=nome, age=idade, work=profissoa, language=linhagem))


valor = 3.14159

print(f"Valor de PI: {valor:.2f}")
print(f"Valor de PI: {valor:10.2f}")
