# metodos úteis em dicionários são: Keys(), values(), items()

from copy import copy


dias = {'Sex': 'Sexta', 'Seg': 'Segunda', 'Qua': 'Quarta', 'Qui': 'Quinta'}

# chaves = dias.keys()
# print(chaves)
# for chave in chaves:
#  print(chave)

# values = dias.values()
# for value in values:
#  print(value, end=' ')

# for item in dias.items():
#   print(item)

# dias.pop('Sex')
# print(dias)

#dias_copy = dias
#dias_copy['Dom']='Domingo'
#print(dias)
import copy
dias_copy = copy.deepcopy(dias)
dias_copy['Dom']='Domingo'

print(f'Dicionário dias: {dias}')
print(f'Dicionário dias_copy: {dias_copy}')
