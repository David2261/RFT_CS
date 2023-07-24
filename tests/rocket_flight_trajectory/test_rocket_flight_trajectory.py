"""
Файл для тестирования математического моделирования движения тел
"""
from typing import Any
import pytest
import numpy as np

from RFTCS.rocket_flight_trajectory import FlightBallistics
from RFTCS.setup.constant import ACCELERATION_FREE_FALL
from RFTCS.setup.settings import FPV


@pytest.mark.rft
class TestFlightBallistics:
	""" Тестирование функций расчета баллистики """
	speed = 29000

	# Тестирвание вычисления функции
	def test_double_angle_sine(self) -> bool:  # type: ignore[return]
		FB = FlightBallistics(self.speed)
		check = FB._double_angle_sine()
		result = 2 * np.sin(self.speed) * np.cos(self.speed)
		assert result == check

	# Тестирование типа вывода функции
	def test_double_angle_sine_type(self) -> bool:  # type: ignore[return]
		result = FlightBallistics(self.speed)
		res = result._double_angle_sine()
		assert isinstance(res, (float, int))

	# Тестирование на логическую операцию функции
	def test_double_angle_sine_less(self) -> bool:  # type: ignore[return]
		FB = FlightBallistics(self.speed)
		result = FB._double_angle_sine()
		check = result + 1
		assert result < check

	# Тестирование на логическую операцию функции
	def test_double_angle_sine_more(self) -> bool:  # type: ignore[return]
		FB = FlightBallistics(self.speed)
		result = FB._double_angle_sine()
		check = result - 1
		assert result > check

	# Тестирвание вычисления функции
	def test_flight_range(self) -> bool:  # type: ignore[return]
		G = ACCELERATION_FREE_FALL
		FB = FlightBallistics(self.speed)
		result = FB.flight_range()
		sine = FB._double_angle_sine()
		answer = ((self.speed ** 2) * sine) / (2 * G)
		assert result == answer

	# Тестирование типа вывода функции
	def test_flight_range_type(self) -> bool:  # type: ignore[return]
		result = FlightBallistics(self.speed)
		res = result.flight_range()
		assert isinstance(res, (float, int))

	# Тестирование на логическую операцию функции
	def test_flight_range_less(self) -> bool:  # type: ignore[return]
		FB = FlightBallistics(self.speed)
		result = FB.flight_range()
		check = result + 1
		assert result < check

	# Тестирвание вычисления функции
	def test_flight_time(self) -> bool:  # type: ignore[return]
		G = ACCELERATION_FREE_FALL
		A = FPV
		answer = ((2 * self.speed * np.sin(A)) / G)
		result = FlightBallistics(self.speed)
		assert result.flight_time() == answer

	# Тестирование типа вывода функции
	def test_flight_time_type(self) -> bool:  # type: ignore[return]
		result = FlightBallistics(self.speed)
		res = result.flight_time()
		assert isinstance(res, (float, int))

	# Тестирование на логическую операцию функции
	def test_flight_time_less(self) -> bool:  # type: ignore[return]
		G = ACCELERATION_FREE_FALL
		A = FPV
		answer = ((2 * self.speed * np.sin(A)) / G)
		result = FlightBallistics(self.speed)
		assert result.flight_time() < (answer + 1)

	# Тестирование на логическую операцию функции
	def test_flight_time_more(self) -> bool:  # type: ignore[return]
		G = ACCELERATION_FREE_FALL
		A = FPV
		answer = ((2 * self.speed * np.sin(A)) / G)
		result = FlightBallistics(self.speed)
		assert result.flight_time() > (answer - 1)


@pytest.mark.rft
@pytest.mark.exception
class TestFlightBallisticsError:
	""" Тестирование исключений функций расчета баллистики """
	speed = 29000
	fake = 'fake'

	# Тестирование без аргументов
	def test_double_angle_sine_without_args(self) -> Any:
		with pytest.raises(TypeError):
			ballistic = FlightBallistics(None)
			result = ballistic._double_angle_sine()
			return result

	# Тестирование на большее кол-во аргументов
	def test_double_angle_sine_more_args(self) -> Any:
		with pytest.raises(TypeError):
			ballistic = FlightBallistics(
					self.speed,
					self.fake)  # type: ignore[call-arg]
			result = ballistic._double_angle_sine()
			return result

	# Тестирование на ошибочный тип параметра функции
	def test_flight_range_type_error(self) -> Any:
		with pytest.raises(TypeError):
			res = FlightBallistics(self.fake)
			return res.flight_range()

	# Тестирование на меньшое кол-во аргументов
	def test_flight_range_less_args(self) -> Any:
		with pytest.raises(TypeError):
			res = FlightBallistics(None)
			return res.flight_range()

	# Тестирование на большее кол-во аргументов
	def test_flight_range_more_args(self) -> Any:
		with pytest.raises(TypeError):
			res = FlightBallistics(
					self.speed,
					self.fake)  # type: ignore[call-arg]
			return res.flight_range()

	# Тестирование на ошибочный тип параметра функции
	def test_flight_time_type_error(self) -> Any:
		with pytest.raises(TypeError):
			res = FlightBallistics(self.fake)
			return res.flight_time()

	# Тестирование на меньшое кол-во аргументов
	def test_flight_time_less_args(self) -> Any:
		with pytest.raises(TypeError):
			res = FlightBallistics(None)
			return res.flight_time()

	# Тестирование на большее кол-во аргументов
	def test_flight_time_more_args(self) -> Any:
		with pytest.raises(TypeError):
			res = FlightBallistics(
					self.speed,
					self.fake)  # type: ignore[call-arg]
			return res.flight_time()
