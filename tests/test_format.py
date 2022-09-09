import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest

from format import RocketFormat, FlightFormat


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
