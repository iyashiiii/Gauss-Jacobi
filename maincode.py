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

a = [0]
b = [0]
c = [0]

#i=0

def fa():
	i=0
	while True:
		a.append(round((1*b[i]-2*c[i]+12)/5, 4))
		b.append(round((-3*a[i]+2*c[i]-25)/8,4))
		c.append(round((-1*a[i]-1*b[i]+6)/4,4))
		i+=1

		if [a[i],b[i],c[i]] == [a[i-1],b[i-1],c[i-1]]:
			break


fa()

x = [[a[i],b[i],c[i]] for i in range(len(a))]
print(a)

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

print(x)

for i in x:
	print()
	for x in i:
		#print('{:10}'.format(x), end="") 
		print('{:10}'.format("%.4f"%x), end="") 
