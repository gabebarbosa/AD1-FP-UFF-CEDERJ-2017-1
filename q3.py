#coding: utf-8
l, c = map(int, raw_input().split())

from random import randint
def criar(i, j):
    matriz = []
    for r in range(i):
        matriz.append([])
        for s in range(j):
            matriz[r].append(randint(10,99))
            print(matriz[r][s])
        print()
    return matriz

def mostrar(m):
    if len(m)>3 or len(m[0])>3:
        for r in range(1, len(m)-1):
            for s in range(1, len(m[r])-1):
                if (m[r][s]< m[r-1][s-1]) and (m[r][s]< m[r-1][s]) and (m[r][s]< m[r-1][s+1]) and (m[r][s]< m[r][s-1]) and (m[r][s]< m[r][s+1]) and (m[r][s]< m[r+1][s-1]) and (m[r][s]< m[r+1][s]) and (m[r][s]< m[r+1][s+1]):
                    print()
                    print(m[r-1][s-1], m[r-1][s], m[r-1][s+1])
                    print(m[r][s-1], m[r][s], m[r][s+1])
                    print(m[r+1][s-1], m[r+1][s], m[r+1][s+1])
    return

v = criar(int(l), int(c))

sub_m = mostrar(v)