def check_prime(x):
	for i in range (2,x):
		if x%i==0:
			return True
		else:
			return False
n=int(input("Enter value:"))
factors=[]
for i in range(2,n):
	if n%i==0:
		factors.append(i)
prime_factors=[]
composite_factors=[]
for m in factors:
	result=check_prime(m)
	if result==True:
		composite_factors.append(m)
else:
	prime_factors.append(m)
	print("Factors:",factors)
	print("Prime factors:",prime_factors)
	print("composite_factors:",composite_factors)