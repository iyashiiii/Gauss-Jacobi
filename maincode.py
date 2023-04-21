'''it = no. of iteration
a,b,c = 0,0,0
fa = form. of a / def func
fb = form. of b / def
fc = form. of c / def
x = master list of answers'''

#it = int(input('Enter no. of iterations:'))

num = 0
#a,b,c = 0,0,0
#i = 0

af= [0]
bf= [0]
cf= [0]
										#NOTE: i-alter din yung code pag may negative sa first term kasi magiging 4 yung len ng op
	
inp = input()
	
a = inp.index('x')+1
b = inp.index('y')+1
c = inp.index('z')+1
d= inp.index('=')+1
	
x = inp[:a]
y = inp[a:b]
z = inp[b:c]
	
#x	
if '-' in x and len(x) == 2:
	x = -1
elif x == 'x':
	x = 1
else:
	x = int(x.replace('x',''))
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
eq = int(inp[d:])
	
#formula for x1
if y <= 0:
	y = abs(y)
else:
	y = -abs(y)
	
if z <= 0:
	z = abs(z)
else:
	z = -abs(z)
	
	

	







xx = input()
	
a2 = xx.index('x')+1
b2 = xx.index('y')+1
c2 = xx.index('z')+1
d2 = xx.index('=')+1
	
x2 = xx[:a2]
y2 = xx[a2:b2]
z2 = xx[b2:c2]
	
#x	
if '-' in x2 and len(x2) == 2:
	x2 = -1
elif x2 == 'x':
	x2 = 1
else:
	x2 = int(x2.replace('x',''))
#y
if len(y2) != 2:
	y2 = int(y2.replace('y',''))
	
else:
	y2 = int(y2[0]+'1')
#z
if len(z2) != 2:
	z2 = int(z2.replace('z',''))
	
else:
	z2 = int(z2[0]+'1')
#=
eq2 = int(xx[d2:])
	
#formula for x2
if x2 <= 0:
	x2 = abs(x2)
else:
	x2 = -abs(x2)
	
if z2 <= 0:
	z2 = abs(z2)
else:
	z2 = -abs(z2)

	

	



xxx = input()
	
a3 = xxx.index('x')+1
b3 = xxx.index('y')+1
c3 = xxx.index('z')+1
d3 = xxx.index('=')+1
	
x3 = xxx[:a3]
y3 = xxx[a3:b3]
z3 = xxx[b3:c3]
	
#x	
if '-' in x3 and len(x3) == 2:
	x3 = -1
elif x3 == 'x':
	x3 = 1
else:
	x3 = int(x3.replace('x',''))
#y
if len(y3) != 2:
	y3 = int(y3.replace('y',''))
	
else:
	y3 = int(y3[0]+'1')
#z
if len(z3) != 2:
	z3 = int(z3.replace('z',''))
	
else:
	z3 = int(z3[0]+'1')
#=
eq3 = int(xxx[d3:])
	
#formula for x3
if x3 <= 0:
	x3 = abs(x3)
else:
	x3 = -abs(x3)
	
if y3 <= 0:
	y3 = abs(y3)
else:
	y3 = -abs(y3)
	
i=0
no=1
while True:
	af.append(round((y*bf[i] + z*cf[i] + eq)/x,4))
	bf.append(round((x2*af[i] + z2*cf[i] + eq2)/y2,4))
	cf.append(round((x3*af[i] + y3*bf[i] + eq3)/z3,4))
	i+=1
	no+=1
	if [af[i],bf[i],cf[i]] == [af[i-1],bf[i-1],cf[i-1]]:
		break
'''
def ayokona():
for i in op:
	while i != '='
		if i == '+':
			ans1 = int(-(xyz[op.index('+')+1])) * b[i]
		if i == '-':
			ans2 = int(xyz[op.index('-')+1]) * c[i]
	finans = (ans1 + ans2 + eq) / xyz[0]
'''





fin = [[af[i],bf[i],cf[i]] for i in range(len(af))]


#h = [a[i],b[i],c[i]]
#hh = [a[i-1],b[i-1],c[i-1]]

'''
while True:
	fa()
	if h != hh:
		x.append(h)
		i+=1
	else:
		break '''
		
print('Gauss Jacobi\n'.center(30))
p = ['x1','x2','x3']
for i in p:
	print (i.center(9),end='')
print('_____________________________')
for i in fin:
	print()
	for x in i:
		#print('{:10}'.format(x), end="") 
		print('{:10}'.format("%.4f"%x), end="")

print('\n')
print(f'--{no} iterations')