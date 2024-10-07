with open('teste.txt', 'r', encoding="utf-8") as aki:
  letra = aki.readline()
  print(f'{letra}')

with open('teste.txt', 'w') as file:
  file.write('Meu curso de Python \n')
  file.write('Aqui na DevSamurai')


with open('teste.txt', 'r', encoding="utf-8") as aki:
  letra = aki.read()
  print(f'{letra}')


with open('teste.txt', 'a', encoding="utf-8") as file:
  file.write('\nÉ muito legal!!!')


with open('teste.txt', 'r', encoding="utf-8") as aki:
  letra = aki.read()
  print(f'{letra}')
