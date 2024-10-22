try:
  x = int(input('Dígite um número:'))
except ValueError as erro:
  print(f'Aconteceu um erro do tipo: {erro}')

print(f'O número dígitado foi {x}')
print('O prigramna segue normalmente')
