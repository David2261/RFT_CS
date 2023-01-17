#!/usr/bin/env python3
"""
В данном файле производиться расчет траектории полета ракеты.
Основные формулы:
	- Полет баллистической ракеты
	- Полет космического аппарата
"""
import sys
import numpy as np
import logging
import logging.config

from exceptions.exception import invalid_import
from setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")

try:
	from setup.constant import ACCELERATION_FREE_FALL
	from setup.settings import FPV
except ImportError as e:
	logger.error(invalid_import(e))
	sys.exit(1)


class FlightBallistics:
	log_info.info("Запуск класса 'FlightBallistics'")
	""" Балистический полет ракеты, внутри Земли """

	def __init__(self, speed):
		self.speed = speed

	@classmethod
	# Синус двойного угла
	def _double_angle_sine(cls):
		try:
			A = FPV
			res = 2 * np.sin(A) * np.cos(A)
			log_info.info("Запуск функции '_double_angle_sine'")
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res

	# Дальность полета
	def flight_range(self):
		try:
			G = ACCELERATION_FREE_FALL
			sine = self._double_angle_sine()
			res = ((self.speed**2) * sine) / (2 * G)
			log_info.info("Запуск функции 'flight_range'")
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res

	# Время полета ракеты
	def flight_time(self):
		try:
			G = ACCELERATION_FREE_FALL
			A = FPV
			res = (2 * self.speed * np.sin(A)) / G
			log_info.info("Запуск функции 'flight_time'")
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res


if __name__ == "__main__":
	speed = 234
	b = FlightBallistics(speed)
	print(b.flight_range())
	print(b.flight_time())
	# -2760.2377351443233
	# 31.05456216260517
