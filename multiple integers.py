n=int(input("Enter the repitation"))
List1=[]
for i in range(n):
	x=int(input("Enter value"))
	List1.append(x)

print(List1) 
List2=list(set(List1))
print(List2)