import random
# Used to create the bit stream for drone inputs 
class BitStream():
	def __inti__(self):
		self.__stream = ""
		self.__total_len = 0
		self.__indivdual_movements = 0
		self.__movement_dict = {}
	
	def get_stream(self): return self.__stream
	def get_total_len(self): return self.__total_len
	def get_individual_movements(self): return self.__indivdual_movements
	def get_movement_dict(self): return self.__movement_dict

	# define valid movement options to bitstream values
	def create_movement_dict(self):
		self.__movement_dict = {
			"thrust":{
				"accelerate":"01",
				"decelerate":"10",
				"neutral":"00"
			},
			"turn":{
				"turn_left":"01",
				"turn_right":"10",
				"no_turn":"00"
			},
			"tilt":{
				"tilt_up":"01",
				"tilt_down":"10",
				"no_tilt":"00"
			}
		}

		return self.__movement_dict

	# create a valid random bitstream with 'num' individual total movements
	def create_random_bitstream(self,num):
		if num <= 0:
			raise ValueError("num input must be larger than 0")

		temp_string = ""
		# create 'num' amount of complete and valid individual movements
		for i in range(0,num):
			# add a random bitstream value for all valid sub categories of movement_dictionary
			for key_value in self.__movement_dict.items():
					temp_string += random.choice(list(key_value[1].values()))

		print(temp_string)
		self.__stream = temp_string
		self.__indivdual_movements = num
		self.__total_len = num*len(self.__movement_dict)

