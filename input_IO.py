class Input():
	def __init__(self):
		self.__accelerate = False
		self.__decelerate  = False
		self.__left = False
		self.__right = False
		self.__up = False 
		self.__down = False

	def get_accelerate(self): return self.__accelerate
	def get_decelerate(self): return self.__decelerate
	def get_left(self): return self.__left
	def get_right(self): return self.__right
	def get_up(self): return self.__up
	def get_down(self): return self.__down

	def show_attributes(self):
		print(
			f"""
Acceleration Boolean: {self.__accelerate}
Deceleration Boolean: {self.__decelerate}
Left Boolean: {self.__left}
Right Boolean: {self.__right}
Up Boolean: {self.__up}
Down Boolean: {self.__down}
			 """)
	
	# Converts from a six long bit stream to drone input object, (0:2 for acceleration, 2:4 for horizontal turning, 4:6 for vertical turning)
	def convert_bitstream(self,bitstream):
		if len(bitstream) != 6:
			raise ValueError("Input bitstream must be 6 digits long")

		if bitstream[0:2] == "10":
			self.__accelerate = True
			self.__decelerate = False
		elif bitstream[0:2] == "01":
			self.__decelerate = True
			self.__accelerate = False
		else:
			self.__accelerate = False
			self.__decelerate = False

		if bitstream[2:4] == "10":
			self.__left = True
			self.__right = False
		elif bitstream[2:4] == "01":
			self.__right = True
			self.__left = False
		else:
			self.__right = False
			self.__left = False

		if bitstream[4:6] == "10":
			self.__up = True
			self.__down = False
		elif bitstream[4:6] == "01":
			self.__down = True
			self.__up = False
		else:
			self.__up = False
			self.__down = False