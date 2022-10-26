import numpy as np

from setup.constant import ACCELERATION_FREE_FALL, FPV


class FlightBallistics:
	""" Балистический полет ракеты, внутри Земли """
	def __init__(self, speed):
		self.speed = speed

	@classmethod
	# Синус двойного угола 
	def _double_angle_sine(cls):
		A = FPV
		return 2 * np.sin(A) * np.cos(A)

	# Дальность полета
	def flight_range(self):
		G = ACCELERATION_FREE_FALL
		A = FPV
		sine = self._double_angle_sine()
		return ((self.speed ** 2) * sine) / (2 * G)

	# Время полета ракеты
	def flight_time(self):
		G = ACCELERATION_FREE_FALL
		A = FPV
		return ((2 * self.speed * np.sin(A)) / G)







