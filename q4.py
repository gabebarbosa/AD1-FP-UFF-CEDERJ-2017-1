#coding: utf-8
def perfeito(n):
	if (n%2 != 0):
		return False
	else:
		i = 1
		soma = 0
		while i < n :
			if (n%i == 0):
				soma = soma + i
			i = i + 1
		if soma == n:
			return True
		else:
			return False

qt_teste = input(int)
i = 0

while (i < qt_teste):
	n = input(int)

	if perfeito(n):
		print "%i é perfeito"%n
	else:
		print "%i não é perfeito"%n
	i = i + 1