#!/usr/bin/env python3
"""
В данном файле производиться расчет траектории полета ракеты.
Основные формулы:
	- Полет баллистической ракеты
	- Полет космического аппарата
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Union

import numpy as np
import logging
import logging.config

from .exceptions.exception import (
	invalid_import,
	invalid_type,
	invalid_zero_division
)
from .setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")

try:
	from .setup.constant import ACCELERATION_FREE_FALL
	from .setup.settings import FPV
	# import core_api as CA # CPython API
except ImportError as e:
	logger.error(invalid_import(e))
	raise ImportError(invalid_import(e))


@dataclass
class TypeFB:
	speed: Union[int, float]


class FlightBallistics(TypeFB):
	log_info.info("Запуск класса 'FlightBallistics'")
	""" Балистический полет ракеты, внутри Земли """

	def __init__(self, speed):
		self.speed = speed

	def _double_angle_sine(self):
		""" Синус двойного угла, градусов """
		try:
			# res = CA.double_angle_sine()
			res = 2 * np.sin(self.speed) * np.cos(self.speed)
			log_info.info("Запуск функции '_double_angle_sine'")
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		return res

	def flight_range(self):
		""" Дальность полета, км """
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
		return res

	def flight_time(self):
		""" Время полета ракеты, ч """
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
		return res


if __name__ == "__main__":
	speed = 'fake'
	b = FlightBallistics(speed)
	print(b.flight_range())
	print(b.flight_time())
	# -2760.2377351443233
	# 31.05456216260517
