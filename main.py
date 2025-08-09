from obstacles import Drone, Building
from input_IO import Input
from bitstream import BitStream
import time 
import matplotlib.pyplot as plt

def main():
	
	# initialise plot and objects 
	ax = plt.figure().add_subplot(projection='3d')
	ax.plot(0,0,0)
	ax.legend()
	plt.show()
	drone = Drone(0,0,0)
	building = Building(0,0,0)
	bitstream = BitStream(1)
	# create random bitstream
	bitstream.create_random_bitstream()
	x= bitstream.get_stream()
	print(x)

	# convert bitstream to input values
	input = Input()
	input.convert_bitstream(x)

	drone.show_position()
	drone.user_input_updates(input)
	drone.show_attributes()

	for i in range(0,bitstream.get_individual_movements()):
		drone.update_position()
		drone.show_position()
		if drone.building_collision(building):
			print("Collision!")
		time.sleep(1)

if __name__ == "__main__":
    main()
