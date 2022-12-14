"""
Файл для тестирования математического моделирования движения тел
"""
import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest
import numpy as np

from rocket_flight_trajectory import FlightBallistics
from setup.constant import ACCELERATION_FREE_FALL
from setup.settings import FPV


@pytest.mark.rft
class TestFlightBallistics:
	""" Тестирование функций расчета баллистики """
	speed = 29000

	@classmethod
	# Синус двойного угола 
	def _double_angle_sine(cls):
		A = FPV
		return 2 * np.sin(A) * np.cos(A)

	# Тестирвание вычисления функции
	def test_flight_range(self):
		G = ACCELERATION_FREE_FALL
		A = FPV
		sine = self._double_angle_sine()
		answer = ((self.speed ** 2) * sine) / (2 * G)
		result = FlightBallistics(self.speed)
		assert result.flight_range() == answer

	# Тестирование типа вывода функции
	def test_flight_range_type(self):
		result = FlightBallistics(self.speed)
		res = result.flight_range()
		assert isinstance(res, (float, int))

	# Тестирование на логическую операцию функции
	def test_flight_range_less(self):
		G = ACCELERATION_FREE_FALL
		A = FPV
		sine = self._double_angle_sine()
		answer = ((self.speed ** 2) * sine) / (2 * G)
		result = FlightBallistics(self.speed)
		assert result.flight_range() < (answer + 1)

	# Тестирвание вычисления функции
	def test_flight_time(self):
		G = ACCELERATION_FREE_FALL
		A = FPV
		answer = ((2 * self.speed * np.sin(A)) / G)
		result = FlightBallistics(self.speed)
		assert result.flight_time() == answer

	# Тестирование типа вывода функции
	def test_flight_range_type(self):
		result = FlightBallistics(self.speed)
		res = result.flight_time()
		assert isinstance(res, (float, int))

	# Тестирование на логическую операцию функции
	def test_flight_time_less(self):
		G = ACCELERATION_FREE_FALL
		A = FPV
		answer = ((2 * self.speed * np.sin(A)) / G)
		result = FlightBallistics(self.speed)
		assert result.flight_time() < (answer + 1)


@pytest.mark.rft
@pytest.mark.exception
class TestFlightBallisticsError:
	""" Тестирование исключений функций расчета баллистики """
	speed = 'false'

	# Тестирование на ошибочный тип параметра функции
	def test_flight_range_type_error(self):
		with pytest.raises(TypeError):
			res = FlightBallistics(self.speed)
			res.flight_range()

	# Тестирование на меньшое кол-во аргументов
	def test_flight_range_less_args(self):
		with pytest.raises(TypeError):
			res = FlightBallistics()
			res.flight_range()

	# Тестирование на большее кол-во аргументов
	def test_flight_range_more_args(self):
		with pytest.raises(TypeError):
			res = FlightBallistics(2323, self.speed)
			res.flight_range()

	# Тестирование на ошибочный тип параметра функции
	def test_flight_time_type_error(self):
		with pytest.raises(TypeError):
			res = FlightBallistics(self.speed)
			res.flight_time()

	# Тестирование на меньшое кол-во аргументов
	def test_flight_time_less_args(self):
		with pytest.raises(TypeError):
			res = FlightBallistics()
			res.flight_time()

	# Тестирование на большее кол-во аргументов
	def test_flight_time_more_args(self):
		with pytest.raises(TypeError):
			res = FlightBallistics(self.speed, 2323)
			res.flight_time()
