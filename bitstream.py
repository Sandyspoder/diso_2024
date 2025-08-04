import random
from constants import MOVEMENT_DICT
# Used to create the bit stream for drone inputs 
class BitStream:
	def __init__(self,indivdual_movements):
		if indivdual_movements <= 0:
			raise ValueError("number of individual movements must be at least 1")

		self.__movement_dict = MOVEMENT_DICT
		self.__indivdual_movements = indivdual_movements
		# take the first value of the dict keys and find its bitstream length
		# assume that the dictionary keys are the same length
		self.__movement_dict_list = list(map(lambda x: len(list(x[1].values())[0]), MOVEMENT_DICT.items()))
		self.__total_len = sum(self.__movement_dict_list)
		self.__stream = "".zfill(self.__total_len)

	def get_stream(self): return self.__stream
	def get_total_len(self): return self.__total_len
	def get_individual_movements(self): return self.__indivdual_movements
	def get_movement_dict(self): return self.__movement_dict

	# create a valid random bitstream with 'num' individual total movements
	def create_random_bitstream(self):
		temp_string = ""
		# create 'num' amount of complete and valid individual movements
		for i in range(0,self.__indivdual_movements):
			# add a random bitstream value for all valid sub categories of movement_dict
			for key_value in self.__movement_dict.items():
					temp_string += random.choice(list(key_value[1].values()))
		# Update object attributes 
		self.__stream = temp_string

	# create a valid null bitstream string 
	def create_null_bitstream(self,num):
		self.__stream = "".zfill(self.__total_len)
		

