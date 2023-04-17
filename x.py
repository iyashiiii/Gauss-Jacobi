

def x():
	x = input()
	l = [i for i in x] #split input
	xyz = []            #nums
	op = []             #operations
	eq = []             #equal sign

	nums = '0123456789' #guide
	var = 'xyz'
	operations = '+-*='

	a = [0]
	b = [0]
	c = [0]

	#print(l)
	for i in l:
		if i in nums:
			xyz.append(i)
			#l.remove(i)

		elif i in operations:
			xyz.append(' ')
			op.append(i)
	n = 0
	for i in xyz[::-1]:
		if i != ' ':
			eq.append(i)
			n+=1
		else:
			eq = int(''.join(eq[::-1]))
			
			for x in xyz[xyz.index(i)::-1]:
				while n!= 0:
					n-=1
					xyz.pop() #xyz.index(i)+4)
			break

	xyz  = ''.join(xyz).split()
	last = []

	#final()
	#print(xyz[xyz.index(' ')+1])
	'''
	print(eq)
	print(xyz)
	print(op)
	print(last) '''

	'''
	['5', 'x', '+', '1', '2', 'y', '-', '1', 'z', '=', '1', '5']
	15
	['5', '12', '1']
	['+', '-', '=']  '''

	#def ayokona():
	for i in op:
		if i != '=':
			if i == '+':
				ans1 = -(int(xyz[op.index('+')+1])) * b[0]
			if i == '-':
				ans2 = int(xyz[op.index('-')+1]) * c[0]
		else:
			finans = (ans1 + ans2 + eq) / int(xyz[0])

	return finans


	'''
	def final():
		if '*' in op:
				last.append( int(xyz[op.index('*')]) * int(xyz[op.index('*')+1]) )
				xyz.pop(op.index('*'))
				xyz.pop(op.index('*'))

		if '+' in op:
			if len(xyz) != 1:
				last.append( int(xyz[op.index('+')]) + int(xyz[op.index('+')+1]) )
				xyz.pop(op.index('+'))
				xyz.pop(op.index('+'))
				op.pop(op.index('+'))
			else:
				last[0] = int(xyz[0])+last[0]
				xyz.clear()
				op.pop(op.index('+'))
		
		if '-' in op:
			if len(xyz) != 1:
				last.append( int(xyz[op.index('-')]) - int(xyz[op.index('-')+1]) )
				xyz.pop(op.index('-'))
				xyz.pop(op.index('-'))
				op.pop(op.index('-'))
			else:
				last[0] =last[0] - int(xyz[0])
				xyz.clear()
				op.pop(op.index('+'))
		if '=' in op:
			last = last[0]/eq

	'''




	'''
	y = '5x+2y-z=15'
	yy = [i for i in y]
	yy.remove('x')
	print(yy) '''
def y():
	y = input()
	l = [i for i in y] #split input
	xyz = []            #nums
	op = []             #operations
	eq = []             #equal sign

	nums = '0123456789' #guide
	var = 'xyz'
	operations = '+-*='

	a = [0]
	b = [0]
	c = [0]

	#print(l)
	for i in l:
		if i in nums:
			xyz.append(i)
			#l.remove(i)

		elif i in operations:
			xyz.append(' ')
			op.append(i)
	n = 0
	for i in xyz[::-1]:
		if i != ' ':
			eq.append(i)
			n+=1
		else:
			eq = int(''.join(eq[::-1]))
			
			for x in xyz[xyz.index(i)::-1]:
				while n!= 0:
					n-=1
					xyz.pop() #xyz.index(i)+4)
			break

	xyz  = ''.join(xyz).split()
	last = []
	op.insert(1,' ')
	#final()
	#print(xyz[xyz.index(' ')+1])
	'''
	print(eq)
	print(xyz)
	print(op)
	print(last) '''

	'''
	['5', 'x', '+', '1', '2', 'y', '-', '1', 'z', '=', '1', '5']
	15
	['5', '12', '1']
	['+', '-', '=']  '''
	
	#def ayokona():
	if len(op) == len(xyz):
		op.insert(1,' ')
		for i in op:
			if i != '=':
				if i == '+' and i == op[0]:
					ans1 = -(int(xyz[op.index('+')])) * a[0]
				if i == '-' and i == op[0]:
					ans1 = int(xyz[op.index('-')]) * a[0]
				if i == '+' and i == op[2]:
					ans2 = -(int(xyz[op.index('+')])) * c[0]
				if i == '-' and i == op[2]:
					ans2 = int(xyz[op.index('-')]) * c[0]
			else:
				finans = (ans1 + ans2 + eq) / int(xyz[1])

	else:
		for i in op:
			if i == op[0]:
				ans1 = -(int(xyz[0])) * a[0]
				continue
			if i != '=':
				if i == '+' and i == op[2]:
					ans2 = -(int(xyz[op.index('+')])) * c[0]
				if i == '-'and i == op[2]:
					ans2 = int(xyz[op.index('-')]) * c[0]

			else:
				finans = (ans1 + ans2 + eq) / int(xyz[1])
		

	return finans
	'''
	def final():
		if '*' in op:
				last.append( int(xyz[op.index('*')]) * int(xyz[op.index('*')+1]) )
				xyz.pop(op.index('*'))
				xyz.pop(op.index('*'))

		if '+' in op:
			if len(xyz) != 1:
				last.append( int(xyz[op.index('+')]) + int(xyz[op.index('+')+1]) )
				xyz.pop(op.index('+'))
				xyz.pop(op.index('+'))
				op.pop(op.index('+'))
			else:
				last[0] = int(xyz[0])+last[0]
				xyz.clear()
				op.pop(op.index('+'))
		
		if '-' in op:
			if len(xyz) != 1:
				last.append( int(xyz[op.index('-')]) - int(xyz[op.index('-')+1]) )
				xyz.pop(op.index('-'))
				xyz.pop(op.index('-'))
				op.pop(op.index('-'))
			else:
				last[0] =last[0] - int(xyz[0])
				xyz.clear()
				op.pop(op.index('+'))
		if '=' in op:
			last = last[0]/eq

	'''




	'''
	y = '5x+2y-z=15'
	yy = [i for i in y]
	yy.remove('x')
	print(yy) '''


#x=x()
y=y()

#print(x)
print(y)