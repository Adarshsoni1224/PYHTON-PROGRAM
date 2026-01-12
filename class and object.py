# # OBJECT ORIENDTED PROGRAMMING SYSTEAM :
# # CLASS AND OBJECT
# class student ( ):
# 		def __init__( self ):
# 				self.name=input("Enter name: ")
# 				self.email=input("Enter email:")

# 		def show ( self ):
# 				print("name:",self.name)
# 				print("email : ",self.email)

# S1=student()
# S1.show()

# S2=student()
# S2.show()

#inheritance
class shape ():
	def __init__(self):
		self.length=int(input("Enter the length : "))
		self.breath=int(input("Entet the breath : "))

	def show_dimension(self):
		print("lenth of the shape :",self.length)
		print("breath of the shape :",self.breath)


# S1=shape()
# S1.show_dimension()
# print()
# S2=shape()
# S2.show_dimension()

class shape_3D(shape):
	def __init__(self):
		super().__init__()
		self.height=int(input("Enter Height : "))

	def show_dimension_3(self):
		super().show_dimension()
		print("Height :",self.height)
		
S1=shape_3D()
S1.show_dimension_3()