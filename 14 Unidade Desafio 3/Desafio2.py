# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html
####
# Módulo 're' que fornece operações com expressões regulares.
import re


def validate_numero_telefone(phone_number):
    pattern = re.compile("\([0-9]{2}\)\s9[0-9]{4}\-[0-9]{4}")
    # : Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):  
        print("Número de telefone válido.")
    else:
        print("Número de telefone inválido.")
        # : Agora crie um return, para retornar que o número de telefone é válido:
       
       # : Crie um else e return, caso não o número de telefone seja inválido:
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()
validate_numero_telefone(phone_number)
# : Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.

# Imprime o resultado:
