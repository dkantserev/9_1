n = int(input())

def algoritm(f):
	l=list()
	for i in range(1,f+1):
		l.append(factorial(i))
	l.sort(reverse=True)
	return l

def factorial(n):
	r=1
	for i in range(1,n+1):
		r*=i
	return r
	
print(f'factorial n = {factorial(n)}')
print(algoritm(factorial(n)))
