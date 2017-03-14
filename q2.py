#coding: utf-8
n = input(int)
i = 0
x = [None]*n
y = [None]*n

while i < n:
	x[i], y[i] = map(int, raw_input().split())
	# testa primeiro loop e atrinui à variaveis para teste
	if i == 0:
		x_min = x[i]
		y_min = y[i]
		x_max = x[i]
		y_max = y[i]

	# testes maiores e menores x e y
	if x[i] < x_min:
		x_min = x[i]
	if y[i] < y_min:
		y_min = y[i]
	if x[i] > x_max:
		x_max = x[i]
	if y[i] > y_max:
		y_max = y[i]

	# acrescenta contadora
	i = i + 1


print "xMin = %i"%x_min
print "yMin = %i"%y_min
print "xMax = %i"%x_max
print "yMax = %i"%y_max

rx1 = x_min
ry1 = y_min
rx2 = x_max//2
ry2 = y_max//2

total_pontos = 0
i = 0
print "Pontos dentro do retângulo:"
while i < n:
	if x[i] > rx1 and x[i] < rx2 and y[i] > ry1 and y[i] < ry2 :
		total_pontos = total_pontos + 1
		print "%i %i"%(x[i], y[i])
	i = i + 1
print "Total de Pontos: %i"%total_pontos