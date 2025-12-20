try:
	a=int(input("Enter the value:"))
	b=int(input("Enter the value:"))
	c=a/b
	print("{}/{}={}".format(a,b,c))

except  ZeroDivisionError:
	print("Denominator can`t zero")
except  ValueError:
	print("only integer values are allowed")
else:
	print("I am done get lost")
finally:
	print("excecution complete successfully")

# class NumError(Exception):
# 	pass 


# try:
#     n=int(input("Enter n:"))
#     if n<0:
#     	raise ValueError("-ve value not allowed")
#     else : 
#     	fact=1   
#     	for i in range (1,n+1):
#         	fact=fact*i
#         print("factorial of {}={}".format(n,fact))

# except ValueError as e:
# 	print(e)

