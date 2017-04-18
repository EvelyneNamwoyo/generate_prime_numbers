def prime_nums(n):
	primes=[]
	if not isinstance(n,int):
		raise ValueError
	else:
		if (n==0 or n==1):
				return ('Zero or one cannot be a prime number')
		elif (n<0):
			return ('Cannot generate prime numbers for negative integers')
		elif n==2:
			primes.append(2)
			return primes
			
		else:
			for i in range(2,n+1):
				for a in range(2,i):
					if i%a==0:
						break
					else:
						primes.append(i)
						break
			return primes
			
		 
print (prime_nums(10))


