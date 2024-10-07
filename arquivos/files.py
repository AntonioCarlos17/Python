# read(n), read(), readline(), readlines()
# precisa estar no mesmo diretorio ou saber todo o caminho do diretório até o arquivo desejado

# print(len(letra.readlines(500)))   retorna a quantidade de linhas dos arquivos
# print(letra.readlines()) retorna uma lista contendo cada umas das linhas

# with open("arquivos/exemplo.txt", "r+", encoding='utf-8') as letra:
# retorna a quantidade de linhas dos arquivos
#    print(len(letra.readlines(500)))

# contando as palavras
with open("arquivos/exemplo.txt", "r+", encoding='utf-8') as letra:
    palavras = letra.read()
    lista_palavras = palavras.split()
    print(f'quantidades de palavras no total: {len(lista_palavras)}')
    set_palavras = set(lista_palavras)
    li = lista_palavras.count('não')
    print(f'quantidade de repetições de palavras: {li}')
    print(f'Quantidades de palavras não repetidas: {len(set_palavras)}')

