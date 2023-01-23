import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest
import numpy as np

from setup.constant import EARTH_RADIUS
from setup.settings import (
	INITIAL_DISTANCE,
	BEGIN_RADIUS_ROCKET
)
from rocket_flight_simulation import (
	distance_N_step,
	tg_Beta,
	CylindricalCavity
)


@pytest.mark.rfs
class TestDistanceNStep:
	""" Тест для distance_N_step """
	fuelFlow = 581
	n = 3

	def test_distance_n_step(self):
		result = distance_N_step(self.fuelFlow, self.n)
		R_0 = INITIAL_DISTANCE
		distance = R_0 - self.n * self.fuelFlow
		assert result == distance

	def test_distance_n_step_type(self):
		result = distance_N_step(self.fuelFlow, self.n)
		assert isinstance(result, (int, float))

	def test_distance_n_step_less(self):
		result = distance_N_step(self.fuelFlow, self.n)
		result_more = result + 1
		assert result < result_more

	def test_distance_n_step_more(self):
		result = distance_N_step(self.fuelFlow, self.n)
		result_more = result - 1
		assert result > result_more

	def test_distance_n_step_ist_none(self):
		result = distance_N_step(self.fuelFlow, self.n)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestDistanceNStepError:
	""" Тест исключений для distance_N_step """
	fuelFlow = 581
	n = 3
	fake = 'fake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_distance_n_step_type_1_args_error(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fake, self.n)

	# Тестирование на ошибочный 2 тип параметра функции
	def test_distance_n_step_type_2_args_error(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fuelFlow, self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_distance_n_step_less_args(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fake)

	# Тестирование на большее кол-во аргументов
	def test_distance_n_step_more_args(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fuelFlow, self.fake, 2343)


@pytest.mark.rfs
class TestTgBeta:
	""" Тест для tg_Beta """
	speed = 581

	def test_tg_beta(self):
		check = tg_Beta(self.speed)
		v = (self.speed * BEGIN_RADIUS_ROCKET) / 398_621
		result = v / (2 * np.sqrt(abs(1 - v)))
		assert result == check

	def test_tg_beta_type(self):
		result = tg_Beta(self.speed)
		assert isinstance(result, (int, float))

	def test_tg_beta_less(self):
		result = tg_Beta(self.speed)
		result_more = result + 1
		assert result < result_more

	def test_tg_beta_more(self):
		result = tg_Beta(self.speed)
		result_more = result - 1
		assert result > result_more

	def test_tg_beta_ist_none(self):
		result = tg_Beta(self.speed)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestTgBetaError:
	""" Тест исключений для tg_Beta """
	speed = 581
	fake = 'fake'

	# Тестирование на ошибочный тип параметра функции
	def test_tg_beta_type_args_error(self):
		with pytest.raises(TypeError):
			result = tg_Beta(self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_tg_beta_less_args(self):
		with pytest.raises(TypeError):
			result = tg_Beta()

	# Тестирование на большее кол-во аргументов
	def test_tg_beta_more_args(self):
		with pytest.raises(TypeError):
			result = tg_Beta(self.speed, self.fake)


@pytest.mark.rfs
class TestEllipticalRange:
	""" Тест для elliptical_range """
	speed = 581

	def test_elliptical_range(self):
		check = elliptical_range(self.speed)
		R = EARTH_RADIUS
		Tang = tg_Beta(self.speed)
		result = 2 * R * np.arctan(Tang)
		assert result == check

	def test_elliptical_range_type(self):
		result = elliptical_range(self.speed)
		assert isinstance(result, (int, float))

	def test_elliptical_range_less(self):
		result = elliptical_range(self.speed)
		result_more = result + 1
		assert result < result_more

	def test_elliptical_range_more(self):
		result = elliptical_range(self.speed)
		result_more = result - 1
		assert result > result_more

	def test_elliptical_range_ist_none(self):
		result = elliptical_range(self.speed)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestEllipticalRangeError:
	""" Тест исключений для elliptical_range """
	speed = 581
	fake = 'fake'

	# Тестирование на ошибочный тип параметра функции
	def test_elliptical_range_type_args_error(self):
		with pytest.raises(TypeError):
			result = elliptical_range(self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_elliptical_range_less_args(self):
		with pytest.raises(TypeError):
			result = elliptical_range()

	# Тестирование на большее кол-во аргументов
	def test_elliptical_range_more_args(self):
		with pytest.raises(TypeError):
			result = elliptical_range(self.speed, self.fake)


@pytest.mark.rfs
class TestCylindricalCavity:
	"""Тест _body_area"""
	U = 41187.93
	n = 4
	L = 0.45

	# Тестирвание вычисления функции
	def test_volume_cylindrical_cavity(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		R_0 = INITIAL_DISTANCE
		_cc = R_0 + self.n * self.U
		check = np.pi * float((_cc**2) * self.L)
		assert result == check

	# Тестирование типа вывода функции
	def test_volume_cylindrical_cavity_type(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_volume_cylindrical_cavity_less(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		check = result + 1
		assert result < check

	def test_volume_cylindrical_cavity_more(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		check = result - 1
		assert result > check

	def test_volume_cylindrical_cavity_ist_none(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestCylindricalCavityError:
	"""Тест _body_area с ошибкой"""
	...
