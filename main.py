from obstacles import Drone, Building
from input_IO import Input
def main():
	drone = Drone(0,0,0)
	building = Building(0,0,0)
	if drone.building_collision(building):
		print(1)

if __name__ == "__main__":
    main()
