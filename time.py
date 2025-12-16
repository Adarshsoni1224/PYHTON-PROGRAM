# import time

# # For loop
# start_time_for = time.time()
# n=12
# fact_n=1
# for i in range(1,n+1):
# 	fact_n=fact_n*i
# print("factorial=",fact_n)
# print("==============================")
# end_time_for = time.time()
# time_taken_for = end_time_for - start_time_for
# print(f"Time taken by for loop: {time_taken_for} seconds")
# print("======================================")

# #While loop
# start_time_while = time.time()
# r=12
# fact_r=1
# i=1
# while(i<=r):
# 	fact_r=fact_r*i
# 	i=i+1
# print("factorial=",fact_r)
# print("=======================================")
# end_time_while = time.time()
# time_taken_while = end_time_while - start_time_while
# print(format"Time taken by while loop: {time_taken_while} seconds")
# print("=======================================")


import time
x=int(input("Enter the value :"))
start_time=time.time_ns()
fact=1
for i in range (1,x+1):
	fact=fact*i
print("factorial	of {}={}".format(x,fact))
end_time=time.time_ns()
total_time=end_time-start_time
print("Total time",total_time)