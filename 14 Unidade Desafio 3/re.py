import re

#fullmach - procura precisa de uma padrão igual!
#seach - procura um valor parecido dentro da string - somente a primeira vez que ela aparece
#findall - procura todas as vezes que aparece

# . - qual caracter que não seja /n - (pular linha) . - vale a quantidade. para representa o . se usa \.
# ^ - procura se no inicio da string. 
# $ - procura se o fina da string.
# [^] - Dentro de um conjunto [] retorna diferente
# \w - pergunta se é um alfanumerico. [a-z]
# \W - se não é um alfa numérico [@,#,%,&,etc....]
# \s - caracter vazio 
# \S - caracter não vazio
# \d - Se é um número de 0-9
# \D - Tudo aquilo que não é um número.
# [] - conjunto de possibilidade
# [a-z] - Todas as letras de "a" a "z" minusculas ex: [a-d], [a-p], etc....
# [A-Z] - Maiusculas - misturados [a-mA-Z]
# [0-9] - Qualquer numero - misturados [a-mA-Z0-9]
# + -  [a-mA-Z0-9]+ Repetição uma ou mais vezes, caso não aparecer apresetera erro ex: [a-mA-Z0-9]+ 
# * -  [a-mA-Z0-9]* 0 ou mais vezes.
# ? -  [a-mA-Z0-9]? 0 ou 1 vezes.
# {x} -  [a-mA-Z0-9]{2} numeros de vezes que o pradão tem que se repetir
# {x,y} -  [a-mA-Z0-9]{2:5} o minimo e o minimo
# \ - usado para caracteris especiais.


#CPF
# 463.343.132-23
'''
string = "463.343.132-23"
pattern = re.compile("[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}")
x = re.fullmatch(pattern,string)
print(x)'''

#EMAIL gabrielon@email.com.br
'''
string = "gabrielon@email.com"
pattern = re.compile("[\w]+@[\w]+\.com[\.a-zA-Z]{0,5}")
x = re.fullmatch(pattern, string)
print(x)'''

#TELEFONE

string = "(83) 93232-2323"
pattern = re.compile("\([0-9]{2}\)\s9[0-9]{4}\-[0-9]{4}")
x = re.fullmatch(pattern, string)
print(x)