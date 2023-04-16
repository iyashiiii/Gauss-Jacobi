'''it = no. of iteration
a,b,c = 0,0,0
fa = form. of a / def func
fb = form. of b / def
fc = form. of c / def
x = master list of answers'''

it = int(input('Enter no. of iterations:'))
num = 0
#a,b,c = 0,0,0
#i = 0

a = [0]
b = [0]
c = [0]

def fa():
	for i in range(it):
	    a.append((1*b[i]-2*c[i]+12)/5)
	    b.append((-3*a[i]+2*c[i]-25)/8)
	    c.append((-1*a[i]-1*b[i]+6)/4)


fa()

x = [[a[i],b[i],c[i]] for i in range(it)]

for i in x:
	print()
	for x in i:
		print('{:10}'.format("%.4f"%x), end="")
