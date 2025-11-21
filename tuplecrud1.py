""""""""#Create 
"""y=(1,2,3,4)

#Read 
for i in range (len(y)):
	print(i)
	print(y[i])

for i in y:
	print(i)"""

"""product=(1,2,3,4)
x=1
for i in product:
	x *=i

print(x)"""

# Create a tuple of tuples
students = (
    ("Harsh", 20, "B.Tech"),
    ("Adarsh", 18, "BCA"),
    ("Aman", 21, "BCA")
)

# Print the entire tuple
print("Tuple of Tuples:")
print(students)

# Access the first tuple
print("\nFirst student's details:", students[0])

# Access specific elements
print("Name of first student:", students[0][0])
print("Age of second student:", students[0][1])
print("Course of third student:", students[0][2])

print("\nFirst student's details:", students[1])

print("Name of first student:", students[1][0])
print("Age of second student:", students[1][1])
print("Course of third student:", students[1][2])


print("\nFirst student's details:", students[2])

print("Name of first student:", students[2][0])
print("Age of second student:", students[2][1])
print("Course of third student:", students[2][2])

