#Dictionary

#KEY-VALUE PAIR : ( BOTH ARE HETEROGENEOUS )
#
#
#

#Operation
#CRUD
	#C - Create
	#R - Read
	#U - Update
    #D- Delete 



dic1={"name":"Adarsh","Email":"adarshsoni1224","Contact":"7771091422"}
print(dic1)

print("===================")

#READ
#1=read only key 
for i in dic1:
	print(i)
	print(dic1[i])

print("===================")

#2=read only values
for i in dic1.values():
	print(i)

print("===================")

#3=reading key values pair
for i,j in dic1.items():
	print(i)
	print(j) 

print("===================")

#UPDATE

#1= Add new item
dic1["City"]="Bhopal"
print(dic1)

print("====================")

#2=changes value
dic1["name"]=input("Enter new name")
print(dic1)

print("====================")

#3=delete an item 
dic1.pop("name")
print(dic1)
print("====================")