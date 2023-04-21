def x1():
	x = input()
	
	a = x.index('x')+1
	b = x.index('y')+1
	c = x.index('z')+1
	d = x.index('=')+1
	
	xf = x[:a]
	y = x[a:b]
	z = x[b:c]
	
	#x	
	if '-' in xf and len(xf) == 2:
		xf = -1
	elif xf == 'x':
		xf = 1
	else:
		xf = int(xf.replace('x',''))
	#y
	if len(y) != 2:
		y = int(y.replace('y',''))
	
	else:
		y = int(y[0]+'1')
	#z
	if len(z) != 2:
		z = int(z.replace('z',''))
	
	else:
		z = int(z[0]+'1')
	#=
	eq = int(x[d:])
	
	print(xf,y,z,eq)
	print(type(xf),type(y),type(z),type(eq))
	
	#formula for x1
	if y <= 0:
		y = abs(y)
	else:
		y = -abs(y)
	
	if z <= 0:
		z = abs(z)
	else:
		z = -abs(z)
	
	print(xf,y,z,eq)
	
	finans = (y*b[i] + z*c[i] + eq)/xf
	
	print(round(finans,4))

x1()