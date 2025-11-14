#Create 
var_x={2,3,4.5,6,6.3,"Mohit",2,3}
print(var_x)
print(type(var_x))

#Read
for i in var_x:
	print(i)

#Update 
#1=Adding a item 
var_x.add("Adarsh")
print(var_x)

#Removing
var_x.remove(2)
print(var_x)
var_x.discard(3)
print(var_x)

#var_x.remove(54)
#print(var_x)

var_x.discard(54)
print(var_x)