import pytest

from RFTCS.display.format import main_rocket_format


@pytest.mark.format
class TestRocketFormat:
	"""Тест RocketFormat"""
	def test_rocket_total_speed(self):
		test_result = main_rocket_format(23.3, 1)
		result = "Сумма всех скоростей = 23.3 км/час"
		assert test_result == result

	def test_rocket_natural_logarithm(self):
		test_result = main_rocket_format(43.2, 2)
		result = "Натуральный логарифм = 43.2"
		assert test_result == result

	def test_rocket_massa_construction(self):
		test_result = main_rocket_format(21.2, 3)
		result = "Сумма всей конструкции ракеты = 21.2 т"
		assert test_result == result

	def test_rocket_total_oil(self):
		test_result = main_rocket_format(78.2, 4)
		result = "Сумма всего топлива = 78.2 т"
		assert test_result == result


@pytest.mark.format
@pytest.mark.exception
class TestRocketFormatError:
	"""Тест RocketFormat"""

	def test_rocket_total_speed_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.1, 1, 23.1)

	def test_rocket_natural_logarithm_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.1, 2, 23.1)

	def test_rocket_massa_construction_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.1, 3, 23.1)

	def test_rocket_total_oil_more_args(self):
		with pytest.raises(TypeError):
			main_rocket_format(23.1, 4, 23.1)


@pytest.mark.format
class TestFlightFormat:
	"""Тест FlightFormat"""
	def test_flight_resistance_force(self):
		test_result = main_rocket_format(65.2, 5)
		result = "Сила сопротивления = 65.2 H"
		assert test_result == result

	def test_flight_resistance_force_env(self):
		test_result = main_rocket_format(43.6, 5)
		result = "Сила сопротивления = 43.6 H"
		assert test_result == result
