"""
Файл для тестирования математического моделирования движения тел
"""
import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest
import numpy as np

from rocket_landing_calculation import (
	calculation_rocket_movement,
	vector_speed,
	rocket_flight_description
)

# __new __.__ defaults__ для создания объектов Task без указания всех полей.


def data_rlc():
	speed = 528.0
	resistance = 12.3
	radius = 87.0
	elevation = 13900.0
	mass = 568.0
	teta = radius
	array = (speed, resistance, radius, elevation, mass, teta)
	return array


@pytest.mark.crm
class TestCRM:
	"""Тест с calculation_rocket_movement"""
	data = data_rlc()
	speed = data[0]
	resistance = data[1]

	def test_calculation_rocket_movement(self):
		result = 1 * 2 / 3 - self.resistance - self.speed
		tr = calculation_rocket_movement(self.speed, self.resistance)
		# assertEqual a==b
		assert tr == result

	def test_calculation_rocket_movement_type(self):
		tr = calculation_rocket_movement(self.speed, self.resistance)
		# assertTrue something
		assert isinstance(tr, (int, float))

	def test_calculation_rocket_movement_less(self):
		tr = calculation_rocket_movement(self.speed, self.resistance)
		result = (1 * 2 / 3 - self.resistance - self.speed) + 1
		# assertLessEqual a <= b
		assert tr <= result


@pytest.mark.crm
@pytest.mark.exception
class TestCRMError:
	"""Тест calculation_rocket_movement с ошибкой"""
	data = data_rlc()
	speed = data[0]
	resistance = data[1]

	def test_calculation_rocket_movement_type_error(self):
		with pytest.raises(TypeError):
			calculation_rocket_movement('(17,', self.resistance)

	def test_calculation_rocket_movement_more_args(self):
		with pytest.raises(TypeError):
			calculation_rocket_movement(self.speed, self.resistance, 54.2)

	def test_calculation_rocket_movement_less_args(self):
		with pytest.raises(TypeError):
			calculation_rocket_movement(self.speed)


@pytest.mark.vs
class TestVS:
	"""Тест vector_speed"""
	data = data_rlc()
	radius = data[2]
	elev = data[3]

	def test_vector_speed(self):
		result = vector_speed(self.radius, self.elev)
		rt = 9.81 * (self.radius ** 2 / ((self.radius + self.elev) ** 2))
		assert result == rt

	def test_vector_speed_isinstance(self):
		res_test = vector_speed(self.radius, self.elev)
		assert isinstance(res_test, (int, float))

	def test_vector_speed_less(self):
		result = vector_speed(self.radius, self.elev)
		rt = 9.81 * (self.radius ** 2 / ((self.radius + self.elev) ** 2))
		rt += 1
		assert result <= rt


@pytest.mark.vs
@pytest.mark.exception
class TestVSError:
	"""Тест vector_speed с ошибкой"""
	data = data_rlc()
	radius = data[2]
	elev = data[3]

	def test_vector_speed_type_error(self):
		with pytest.raises(TypeError):
			vector_speed('(17,', self.elev)

	def test_vector_speed_more_args(self):
		with pytest.raises(TypeError):
			vector_speed(self.radius, self.elev, 13.2)

	def test_vector_speed_less_args(self):
		with pytest.raises(TypeError):
			vector_speed(self.radius)


@pytest.mark.rfd
class TestRFD:
	"""Тест rocket_flight_description"""
	data = data_rlc()
	speed = data[0]
	resistance = data[1]
	vs = vector_speed(data[2], data[3])
	mass = data[4]
	teta = data[5]

	def test_rocket_flight_description(self):
		y = self.speed * np.sin(self.teta)
		x = self.speed * np.cos(self.teta)
		numerator = 1 * 2 / 3 - self.resistance
		rocket_speed = numerator / self.mass - (self.vs * np.sin(self.teta))
		main_teta = - (self.vs * (np.cos(self.teta) / self.speed))

		test_result = [rocket_speed, main_teta, y, x]
		result = rocket_flight_description(
				self.teta,
				self.speed,
				self.mass,
				self.resistance,
				self.vs)
		assert result == test_result

	def test_rocket_flight_description_isinstance(self):
		result = result = rocket_flight_description(
				self.teta,
				self.speed,
				self.mass,
				self.resistance,
				self.vs)
		assert isinstance(result, (list))

	def test_rocket_flight_description_isinstance_objects(self):
		result = rocket_flight_description(
				self.teta,
				self.speed,
				self.mass,
				self.resistance,
				self.vs)
		obj_1 = isinstance(result[0], (float))
		obj_2 = isinstance(result[1], (float))
		obj_3 = isinstance(result[2], (float))
		obj_4 = isinstance(result[3], (float))
		assert obj_1 and obj_2 and obj_3 and obj_4

	def test_rocket_flight_description_less(self):
		result = rocket_flight_description(
				self.teta,
				self.speed,
				self.mass,
				self.resistance,
				self.vs)
		y = self.speed * np.sin(self.teta)
		x = self.speed * np.cos(self.teta)
		numerator = 1 * 2 / 3 - self.resistance
		rocket_speed = numerator / self.mass - (self.vs * np.sin(self.teta))
		main_teta = - (self.vs * (np.cos(self.teta) / self.speed)) + 1
		test_result = [rocket_speed, main_teta, y, x]
		assert result <= test_result


@pytest.mark.rfd
@pytest.mark.exception
class TestRFDError:
	"""Тест rocket_flight_description с ошибкой"""
	data = data_rlc()
	speed = data[0]
	resistance = data[1]
	vs = vector_speed(data[2], data[3])
	mass = data[4]
	teta = data[5]

	def test_rocket_flight_description_error(self):
		with pytest.raises(TypeError):
			rocket_flight_description(
				'(17,',
				self.speed,
				self.mass,
				self.resistance,
				self.vs)

	def test_rocket_flight_description_more_args(self):
		with pytest.raises(TypeError):
			rocket_flight_description(
				self.teta,
				self.speed,
				self.mass,
				self.resistance,
				self.vs,
				12.2)

	def test_rocket_flight_description_less_args(self):
		with pytest.raises(TypeError):
			rocket_flight_description(
				self.teta,
				self.speed,
				self.mass,
				self.resistance)
