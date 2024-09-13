# Dicionários!!!
# listas []
# tuplas ()
# strings '' ou ""
# dicionario { chave:valor} -> chave poderá ser uma string ou um inteiro
# O valor pode ser listra, string.

# criando um dicionário

empregados = {'01': ['João', 'Silva'],
              '02': ['Maria', 'das Graças'],
              '03': ['Paulo', 'José']}

# print(type(empregados))
# print(empregados['01'])

# aula02
# adicionando no dicionario
# empregados['04'] = ['José', 'Silva']
# print(empregados)
# print(len(empregados))

# print('01' in empregados)

# apagando informações dos dicionários
# del (empregados['03'])
# print(empregados)

# evitando chaves iguais

# metodos do dicionario
# numero_func = input('Dígite o numero do funcionário: \n')
# nome = input('Dígite o nome e sobrenome do funcionário: \n')

# if empregados.get(numero_func):
#  print('ID do funcionáio já cadastrado')
# else:
#  empregados[numero_func] = [nome]

# print(empregados)

# empregados.setdefault('04', ['Fulano de Tal'])
# print(empregados)
empregados2 = {'04':['Fulano','de Tal'],
               '05':['Beltrano', 'de Tal']}

empregados.update(empregados2)

