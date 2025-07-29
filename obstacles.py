import math
from constants import *
# All objects that have a physical collision interaction are defined here

class Enviroment():
	def __init__():
		self._x_upper = ENVIROMENT_X_UPPER_BOUND
		self._x_lower = ENVIROMENT_X_LOWER_BOUND
		self._y_upper = ENVIROMENT_Y_UPPER_BOUND
		self._y_lower = ENVIROMENT_Y_UPPER_BOUND
		self._z_upper = ENVIROMENT_Z_UPPER_BOUND
		self._z_lower = ENVIROMENT_Z_LOWER_BOUND

class Obstacles():
	def __init__(self,x,y,z,radius):
		self._x = x
		self._y = y
		self._z = z
		self._radius = radius

	def get_x(self): return self._x
	def get_y(self): return self._y
	def get_z(self): return self._z
	def get_radius(self): return self._radius
	
# This object creates a cylinder starting at x,y,z= 0 with a radius of BUILDING_RADIUS up to z 
class Building(Obstacles):
	def __init__(self,x,y,z,radius=BUILDING_RADIUS):
		super().__init__(x,y,z,radius)

# This object creates a sphere at position x,y,x with a radius of DRONE_RADIUS
class Drone(Obstacles):
	def __init__(self,x,y,z,radius=DRONE_RADIUS):
		super().__init__(x,y,z,radius)
		self._weight = DRONE_WEIGHT
		self._horizontal_angle = DRONE_HORIZONTAL_ANGLE
		self._vertical_angle = DRONE_VERTICAL_ANGLE	
		self._speed = 0

	def get_horizontal_angle(self): return self._horizontal_angle
	def get_vertical_angle(self): return self._vertical_angle
	def get_velocity(self): return self._speed

	# Updates the Drone parameters based on the input parameters
	def user_input_updates(self,input):
		if input.get_accelerate():
			if self._speed <= DRONE_MAX_SPEED - DRONE_ACCELERATION:
				self._speed += DRONE_ACCELERATION
		elif input.get_decelerate():
			if self._speed >= DRONE_DECELERATION:
				self._speed -= DRONE_DECELERATION

		if input.get_left():
			self._horizontal_angle -= DRONE_HORIZONTAL_TURNING_SPEED
		elif input.get_right():
			self._horizontal_angle += DRONE_HORIZONTAL_TURNING_SPEED	
		
		if input.get_up():
			self._vertical_angle += DRONE_VERTICAL_TURNING_SPEED
		elif input.get_down():
			self._vertical_angle -+ DRONE_VERTICAL_TURNING_SPEED

	# Update the cartesian coordinates, given any deviation from the y axis starting orientation
	def update_position(self):
		self.x += self._speed * math.sin(math.radians(self._horizontal_angle))
		self.y += self._speed * math.cos(math.radians(self._horizontal_angle))
		self.z += self._speed * math.sin(math.radians(self._vertical_angle))

	#  Shows building to drone if in rendering distance
	def render_building(self):
		pass

	# Finds if drone has collided with building
	def building_collision(self,building):
		if not isinstance(building,Building):
			raise TypeError("Input Object should be a Building object")

		if (
			self._x is None or self._y is None or self._z is None or
			self._radius is None or building.get_x() is None or
			building.get_y() is None or building.get_z() is None or 
			building.get_radius() is None
		):
			raise Exception("Object collision calculation not possible, as one of the x,y,z or radius values are not defined")

		# checks if drone is higher than the building, if true then no collision can occur
		if self._z-self._radius > building.get_z():
			return False
		# checks if drone occupies the same xy plane position as the building
		elif ((self._x-building.get_x())**2 + (self._y-building.get_y())**2) > (self._radius+building.get_radius())**2:
			print(2)
			return False
		
		print(f"The Drone collided with a building whilst at position: \nx = {self._x}\ny = {self._y}\nz = {self._z}\n")
		return True

	def enviroment_collision(self,enviroment):
		if not isinstance(enviroment,Enviroment):
			raise TypeError("enviroment Object should be an Enviroment object")
		
		def collision_text(self):
			print(f"The Drone collided with the enviroment whilst at position: \nx = {self._x}\ny = {self._y}\nz = {self._z}\n")

		if self._z - self.radius < enviroment._z_lower:
			self.collision_text()
			return True
		elif self._z + self.radius > enviroment._z_upper:
			self.collision_text()
			return True
		elif self._x - self.radius < enviroment._x_lower:
			self.collision_text()
			return True
		elif self._x + self.radius > enviroment._x_upper:
			self.collision_text()
			return True
		elif self._y - self.radius > enviroment._y_lower:
			self.collision_text()
			return True
		elif self._y + self.radius < enviroment._y_upper:
			self.collision_text()
			return True
		
		return False