#!/usr/bin/env python3
"""
В данном файле производиться расчет траектории полета ракеты.
Основные формулы:
	- Полет баллистической ракеты
	- Полет космического аппарата
"""
import numpy as np

from setup.constant import ACCELERATION_FREE_FALL
from setup.settings import FPV

class FlightBallistics:
	""" Балистический полет ракеты, внутри Земли """
	def __init__(self, speed):
		self.speed = speed

	@classmethod
	# Синус двойного угла
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
