"""
Файл для тестирования математического моделирования движения тел
"""
import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest

from rocket_landing_calculation import (
	calculation_rocket_movement,
	vector_speed,
	rocket_flight_description
)

# __new __.__ defaults__ для создания объектов Task без указания всех полей.


def data_crm():
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
	data = data_crm()
	speed = data[0]
	resistance = data[1]

	def test_calculation_rocket_movement(self):
		result = 1 * 2 / 3 - self.resistance - self.speed
		tr = calculation_rocket_movement(self.speed, self.resistance)
		# assertEqual a==b
		assert tr == result

	def test_calculation_rocket_movement_fail(self):
		with pytest.raises(TypeError):
			calculation_rocket_movement('(17,', self.resistance)

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
	"""Тест calculation_rocket_movement с faile"""
	data = data_crm()
	speed = data[0]
	resistance = data[1]

	def test_calculation_rocket_movement_type_error(self):
		with pytest.raises(TypeError):
			calculation_rocket_movement('(17,', self.resistance)

	def test_calculation_rocket_movement_fail(self):
		with pytest.raises(TypeError):
			calculation_rocket_movement(self.speed, self.resistance, 54.2)
