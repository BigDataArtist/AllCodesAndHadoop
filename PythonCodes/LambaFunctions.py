'''
list =[1,3,6,9,12,15,20,24,26]
print(list)
print(filter(lambda x:x%3==0,list))

print(map(lambda x:x%3==0,list))

print(map(lambda x:x*2+10,list))
print(reduce(lambda x,y:x+y,list))
'''
'''
def make_incremnetor(n,y):
	return(lambda x:x+n+y)

inc1 = make_incremnetor(8,2)
inc2 = make_incremnetor(6,8)

print(inc1(40),inc2(6))
'''
'''
nums = range(2,50)
for i in range(2,9):
	nums = filter(lambda x : x==i or x%i!=0,nums)
print(nums)	
'''
'''
sentence = 'It is raining cats and dogs'
words = sentence.split()
print(words)


length = map(lambda word : len(word),words)
print(length)
'''
'''
f = reduce(lambda x,y:x+y,range(1,101))
print(f)
'''
'''
for n in range(2,10):
	print(n)
	for x in range(2,n):
		print(x)
		if n%x==0:
			print(n,'equals',x,'*',n//x)
			break
	else:
			print(n, 'is a prime number')	
'''	
'''
result=[]
a,b=0,1
while b<1000:
	result.append(b)
	a,b=b,a+b
return result
	'''

def traingle_area(base,height):
	area = base*height*(1.0/2)
	return area
T=traingle_area(10,12)
print(T)










