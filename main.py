from obstacles import Drone, Building
from input_IO import Input
from bitstream import BitStream
import time 

def main():
	drone = Drone(0,0,0)
	building = Building(0,0,0)
	if drone.building_collision(building):
		print(1)
	bitstream = BitStream(1)
	bitstream.create_random_bitstream()
	x= bitstream.get_stream()

	print(x)
	input = Input()
	input.convert_bitstream(x)

	drone.show_position()
	drone.user_input_updates(input)
	drone.show_attributes()
	while True:
		drone.update_position()
		drone.show_position()
		time.sleep(1)

if __name__ == "__main__":
    main()
