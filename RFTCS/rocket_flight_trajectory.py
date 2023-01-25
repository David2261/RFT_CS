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

from exceptions.exception import (
	invalid_import,
	invalid_kbi,
	invalid_type,
	invalid_zero_division,
	invalid_general
)
from setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")

try:
	from setup.constant import ACCELERATION_FREE_FALL
	from setup.settings import FPV
except ImportError as e:
	logger.error(invalid_import(e))
	raise ImportError(invalid_import(e))


class FlightBallistics:
	log_info.info("Запуск класса 'FlightBallistics'")
	""" Балистический полет ракеты, внутри Земли """

	def __init__(self, speed):
		self.speed = speed

	# Синус двойного угла
	def _double_angle_sine(self):
		try:
			A = FPV
			res = 2 * np.sin(A) * np.cos(A)
			log_info.info("Запуск функции '_double_angle_sine'")
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except (IOError, Exception) as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)
		return res

	# Дальность полета
	def flight_range(self):
		try:
			G = ACCELERATION_FREE_FALL
			sine = self._double_angle_sine()
			res = ((self.speed**2) * sine) / (2 * G)
			log_info.info("Запуск функции 'flight_range'")
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except ZeroDivisionError as zde:
			logger.error(invalid_zero_division(zde))
			raise ZeroDivisionError(invalid_zero_division(zde))
		except (IOError, Exception) as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)
		return res

	# Время полета ракеты
	def flight_time(self):
		try:
			G = ACCELERATION_FREE_FALL
			A = FPV
			res = (2 * self.speed * np.sin(A)) / G
			log_info.info("Запуск функции 'flight_time'")
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except ZeroDivisionError as zde:
			logger.error(invalid_zero_division(zde))
			raise ZeroDivisionError(invalid_zero_division(zde))
		except (IOError, Exception) as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)
		return res


if __name__ == "__main__":
	speed = 234
	b = FlightBallistics(speed)
	print(b.flight_range())
	print(b.flight_time())
	# -2760.2377351443233
	# 31.05456216260517
