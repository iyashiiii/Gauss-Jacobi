x = '5x+12y-1z=15'
l = [i for i in x] #split input
xyz = []            #nums
op = []             #operations
eq = []             #equal sign
nums = '0123456789' #guide
var = 'xyz'
operations = '+-*='
print(l)
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

def final():
	for i in op:
		if '*' in op:
			yield int(xyz[op.index('*')]) * int(xyz[op.index('*')+1])
		elif '+' in op:
			yield last.append(int(xyz[op.index(i)]) + int(xyz[op.index(i)+1]))
		elif '-' in op:
			yield last.append(int(xyz[op.index(i)]) - int(xyz[op.index(i)+1]))

       


#print(xyz[xyz.index(' ')+1])
print(eq)
print(xyz)
print(op)





'''
y = '5x+2y-z=15'
yy = [i for i in y]
yy.remove('x')
print(yy) '''