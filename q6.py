#coding: utf-8
n, m = map(int, raw_input().split())
l =[]
c = -1
while int(n)!=0 or int(m)!=0:
    amb = []
    for r in range(int(m)):
        amb.append([])
        f = raw_input()
        for i in range(int(n)):
            amb[r] = f.split()
    c += 1
    l.append(amb)
    print(l[c])
    n, m = input().split()
print(l)

def espalha(a, i, j): 
    linhas = len(a[0]) - 1
    colunas = len(a) - 1
    if a[i][j] == "I":
        if j > 0:
            a[i][j-1] = "I"
        if i > 0:
            a[i-1][j] = "I"
        if j < linhas:
            a[i][j+1] = "I"
        if i < colunas:
            a[i+1][j] = "I"

    if j < linhas:
        return espalha(a, i, j+1)
    else:
        if i < colunas:
            return espalha(a, i+1, j)
        else:
            return None

for i in range(len(l)):
    espalha(l[i], 0, 0)
