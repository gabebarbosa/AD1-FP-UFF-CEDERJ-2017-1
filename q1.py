#coding: utf-8
x, y = map(float, raw_input().split())
if ((x == 0.0) and (y == 0.0)):
	print "Não existem pontos!" 
else:
	sum_x = 0.0
	sum_y = 0.0
	i = 0
	while not((x == 0.0) and (y == 0.0)):
		sum_x = sum_x + x
		sum_y = sum_y + y
		x, y = map(float, raw_input().split())
		i += 1
	print "%0.2f %0.2f"%(sum_x/i, sum_y/i)