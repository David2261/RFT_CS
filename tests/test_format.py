import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest

from format import RocketFormat, FlightFormat


@pytest.mark.format
class TestRocketFormat:
	"""Тест RocketFormat"""
	def test_rocket_total_speed(self):
		test_result = RocketFormat._rocket_total_speed(23.3)
		result = "Сумма всех скоростей = 23.3 м/с" 
		assert test_result == result

	def test_rocket_natural_logarithm(self):
		test_result = RocketFormat._rocket_natural_logarithm(43.2)
		result = "Натуральный логарифм = 43.2"
		assert test_result == result

	def test_rocket_massa_construction(self):
		test_result = RocketFormat._rocket_massa_construction(21.2)
		result = "Сумма всей конструкции ракеты = 21.2 кг"
		assert test_result == result

	def test_rocket_total_oil(self):
		test_result = RocketFormat._rocket_total_oil(78.2)
		result = "Сумма всего топлива = 78.2 кг"
		assert test_result == result


@pytest.mark.format
@pytest.mark.exception
class TestRocketFormatError:
	"""Тест RocketFormat"""
	rf = RocketFormat()

	def test_rocket_total_speed_type_error(self):
		with pytest.raises(TypeError):
			self.rf._rocket_total_speed('sad/')

	def test_rocket_total_speed_more_args(self):
		with pytest.raises(TypeError):
			self.rf._rocket_total_speed(23.1, 23.1)

	def test_rocket_natural_logarithm_type_error(self):
		with pytest.raises(TypeError):
			self.rf._rocket_natural_logarithm('sda/')

	def test_rocket_natural_logarithm_more_args(self):
		with pytest.raises(TypeError):
			self.rf._rocket_natural_logarithm(23.1, 23.1)

	def test_rocket_massa_construction_type_error(self):
		with pytest.raises(TypeError):
			self.rf._rocket_massa_construction('dsa/sa')

	def test_rocket_massa_construction_more_args(self):
		with pytest.raises(TypeError):
			self.rf._rocket_massa_construction(23.1, 23.1)

	def test_rocket_total_oil_type_error(self):
		with pytest.raises(TypeError):
			self.rf._rocket_total_oil('sad/as')

	def test_rocket_total_oil_more_args(self):
		with pytest.raises(TypeError):
			self.rf._rocket_total_oil(23.1, 23.1)


@pytest.mark.format
class TestFlightFormat:
	"""Тест FlightFormat"""
	def test_flight_resistance_force(self):
		test_result = FlightFormat._flight_resistance_force(65.2)
		result = "Сила сопротивления = 65.2 м/с^2"
		assert test_result == result

	def test_flight_resistance_force_env(self):
		test_result = FlightFormat._flight_resistance_force_env(43.6)
		result = "Сила сопротивления среды = 43.6 м/с^2"
		assert test_result == result


@pytest.mark.format
@pytest.mark.exception
class TestFlightFormat:
	"""Тест FlightFormat"""
	ff = FlightFormat()

	def test_flight_resistance_force_type_error(self):
		with pytest.raises(TypeError):
			self.ff._flight_resistance_force('sdaa/sa')

	def test_flight_resistance_force_more_args(self):
		with pytest.raises(TypeError):
			self.ff._flight_resistance_force(23.2, 231.2)

	def test_flight_resistance_force_env_type_error(self):
		with pytest.raises(TypeError):
			self.ff._flight_resistance_force_env('sdaa/sa')

	def test_flight_resistance_force_env_more_args(self):
		with pytest.raises(TypeError):
			self.ff._flight_resistance_force_env(23.2, 231.2)