#RECURSION
def fact (x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)


n=int(input("Enter value:"))

#ITERATION
result1=1
for i in range(1,n+1):
	result1=result1*i
print("{}!={}".format(n,result1))

result=fact(n)
print("{}!{}".format(n,result))