import time
import os.path


def geraLog(texto, nome_arquivo):
  if os.path.isfile('log.txt') is False:
    print('criando arquivo')
  else:
    now = time.localtime()
    now_formatado = time.strftime('%d/%m/%y as %H:%M:%S', now)  # formato BR
    # now_formatado = time.strftime('%x as %X')  # formato US

    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
      arquivo.write(f'{now_formatado} -> {texto} \n')


geraLog('Teste novo', 'log.txt')
