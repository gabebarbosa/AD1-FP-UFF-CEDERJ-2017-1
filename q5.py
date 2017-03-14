#coding: utf-8
a, b = map(int, raw_input().split())
m = []

for r in range(int(b)):
    m.append([])
    f = input()
    for i in range(int(a)):
        m[r] = f.split()
def verifica(m, i, j):
    tam_l = len(m[0])
    tam_c = len(m)
    if m[i][j] == "." and i == 0 and j == 0:
        return "Esse mapa não leva a lugar algum"
    if i <= tam_c and j <= tam_l:
        if m[i][j] == "*":
            return "Esse mapa leva ao tesouro"
        if m[i][j] == ">":
            m[i][j] = "x"
            c = 1
            while j+c < tam_l:
                if m[i][j+c] == ".":
                    c += 1
                elif m[i][j - c] == "<":
                    return "Esse mapa não leva a lugar algum"
                else:
                    return verifica(m, i, j+c)
            return "Esse mapa não leva a lugar algum"

        if m[i][j] == "<":
            m[i][j] = "x"
            c = 1
            while j-c >= 0:
                if m[i][j - c] == ".":
                    c += 1
                elif m[i][j - c] == ">":
                    return "Esse mapa não leva a lugar algum"
                else:
                    return verifica(m, i, j-c)
            return "Esse mapa não leva a lugar algum"
        if m[i][j] == "v":
            m[i][j] = "x"
            c = 1
            while i+c < tamColuna:
                if m[i+c][j] == ".":
                    c += 1
                elif m[i + c][j] == "^":
                    return "Esse mapa não leva a lugar algum"
                else:
                    return verifica(m, i+c, j)
            return "Esse mapa não leva a lugar algum"
        if m[i][j] == "^":
            m[i][j] = "x"
            c = 1
            while i-c >= 0:
                if m[i-c][j] == ".":
                    c += 1
                elif m[i - c][j] == "v":
                    return "Esse mapa não leva a lugar algum"
                else:
                    return verifica(m, i-c, j)
            return "Esse mapa não leva a lugar algum"
        if m[i][j] == "x":
            return "Esse mapa não leva a lugar algum"
    else:
        return "Esse mapa não leva a lugar algum"


r = verifica(m, a, b)
print (r)