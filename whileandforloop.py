print("for loops")
print("===============")
n=int(input("Enter the value :"))
fact_n=1
for i in range(1,n+1):
	fact_n=fact_n*i
print("factorial=",fact_n)

print("===============")
print("while loop")
print("===============")
r=int(input("Enter the value:"))
fact_r=1
i=1
while(i<=r):
	fact_r=fact_r*i
	i=i+1
print("factorial=",fact_r)