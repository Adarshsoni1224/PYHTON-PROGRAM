"""# Write a py script to prnt factors of a given integers using iteration and resursion.

#RECURSION 
def fact (x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
    print("{}!{}".format(n,result))
    result=fact(n)

#Iteration
choice=True
while choice:
    n=int(input("Enter n:"))
    fact=1   
    for i in range (1,n+1):
        fact=fact*i
        print("factorial of {}={}".format(n,fact))

user_choice=int(input("Enter y to continue or n to stop:"))
if user_choice=="n":
    choice=False
else:
    choice=True"""

    # Function to print factors using iteration (manual method)
def print_factors_iterative(num):
    print(f"Factors of {num} (Iterative):")
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, end=' ')
        i = i + 1  # move to next number
    print()  # new line after printing all factors

# Function to print factors using recursion (manual method)
def print_factors_recursive(num, current=1):
    if current > num:
        return  # base case: stop if current exceeds num
    if num % current == 0:
        print(current, end=' ')
    print_factors_recursive(num, current + 1)  # recursive call with next number

# Main code to get input and call both functions
number = int(input("Enter an integer: "))

# Call manual iterative method
print_factors_iterative(number)

# Call manual recursive method
print(f"Factors of {number} (Recursive):")
print_factors_recursive(number)
print()  # add a new line at the end
