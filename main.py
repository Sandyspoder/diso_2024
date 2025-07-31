from obstacles import Drone, Building
from input_IO import Input
from bitstream import BitStream
def main():
	drone = Drone(0,0,0)
	building = Building(0,0,0)
	if drone.building_collision(building):
		print(1)
	bitstream = BitStream()
	bitstream.create_movement_dict()
	bitstream.create_random_bitstream(1)
	x= bitstream.get_stream()
	print(type(x))
	

if __name__ == "__main__":
    main()
