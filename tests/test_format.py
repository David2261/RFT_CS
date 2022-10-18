import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest

from format import main_rocket_format


@pytest.mark.format
class TestRocketFormat:
	"""Тест RocketFormat"""
	def test_rocket_total_speed(self):
		test_result = main_rocket_format(23.3, 1)
		result = "Сумма всех скоростей = 23.3 м/с" 
		assert test_result == result

	def test_rocket_natural_logarithm(self):
		test_result = main_rocket_format(43.2, 2)
		result = "Натуральный логарифм = 43.2"
		assert test_result == result

	def test_rocket_massa_construction(self):
		test_result = main_rocket_format(21.2, 3)
		result = "Сумма всей конструкции ракеты = 21.2 кг"
		assert test_result == result

	def test_rocket_total_oil(self):
		test_result = main_rocket_format(78.2, 4)
		result = "Сумма всего топлива = 78.2 кг"
		assert test_result == result


@pytest.mark.format
@pytest.mark.exception
class TestRocketFormatError:
	"""Тест RocketFormat"""

	def test_rocket_total_speed_type_error(self):
		with pytest.raises(TypeError):
			main_rocket_format('sad/', 1)

	def test_rocket_total_speed_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.1, 1, 23.1)

	def test_rocket_natural_logarithm_type_error(self):
		with pytest.raises(TypeError):
			main_rocket_format('sda/', 2)

	def test_rocket_natural_logarithm_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.1, 2, 23.1)

	def test_rocket_massa_construction_type_error(self):
		with pytest.raises(TypeError):
			main_rocket_format('dsa/sa', 3)

	def test_rocket_massa_construction_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.1, 3, 23.1)

	def test_rocket_total_oil_type_error(self):
		with pytest.raises(TypeError):
			main_rocket_format('sad/as', 4)

	def test_rocket_total_oil_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.1, 4, 23.1)


@pytest.mark.format
class TestFlightFormat:
	"""Тест FlightFormat"""
	def test_flight_resistance_force(self):
		test_result = main_rocket_format(65.2, 5)
		result = "Сила сопротивления = 65.2 м/с^2"
		assert test_result == result

	def test_flight_resistance_force_env(self):
		test_result = main_rocket_format(43.6, 5)
		result = "Сила сопротивления среды = 43.6 м/с^2"
		assert test_result == result


@pytest.mark.format
@pytest.mark.exception
class TestFlightFormat:
	"""Тест FlightFormat"""

	def test_flight_resistance_force_type_error(self):
		with pytest.raises(TypeError):
			main_rocket_format('sdaa/sa', 6)

	def test_flight_resistance_force_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.2, 6, 231.2)

	def test_flight_resistance_force_env_type_error(self):
		with pytest.raises(TypeError):
			main_rocket_format('sdaa/sa', 6)

	def test_flight_resistance_force_env_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.2, 6, 231.2)