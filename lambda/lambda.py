# uma função lambda é uma função anônima
# recebe os argumentos porém só pode execultar uma expressão
# lambda argumentos : expressão

def x(a): return a * 3
print(x(4))


def graus_celsius(f): return (5/9)*(f-32)


print(f'A temperatura em graus celsius é {graus_celsius(32)}')
