def prime_nums(n):
	primes=[]
	if not isinstance(n,int):
		raise ValueError
	else:
		if n>0:
			if n==2:
				primes.append(2)
				return primes
			elif (n==0 or n==1):
				return ('Zero or one cannot be a prime number')
			else:
				for i in range(2,n+1):
					for a in range(2,i):
						if i%a==0:
							break
						else:
							primes.append(i)
							break
				return primes
		else:
			return ('Cannot generate prime numbers for negative integers')
		 
print (prime_nums(10))

input=length n
looping through all the numbers= O(n)
