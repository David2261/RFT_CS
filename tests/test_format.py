import unittest

from test_main import *
from format import RocketFormat, FlightFormat


class TestRocketFormat(unittest.TestCase):
	def setUp(self):
		self.rocket_format = RocketFormat()

	def test_rocket_total_speed(self):
		self.assertEqual(
				self.rocket_format._rocket_total_speed(23.3),
				"Сумма всех скоростей = 23.3 м/с"
				)

	def test_rocket_natural_logarithm(self):
		self.assertEqual(
				self.rocket_format._rocket_natural_logarithm(43.2),
				"Натуральный логарифм = 43.2"
				)

	def test_rocket_massa_construction(self):
		self.assertEqual(
				self.rocket_format._rocket_massa_construction(21.2),
				"Сумма всей конструкции ракеты = 21.2 кг"
				)

	def test_rocket_total_oil(self):
		self.assertEqual(
				self.rocket_format._rocket_total_oil(78.2),
				"Сумма всего топлива = 78.2 кг"
				)


class TestFlightFormat(unittest.TestCase):
	def setUp(self):
		self.fight_format = FlightFormat()

	def test_flight_resistance_force(unittest.TestCase):
		self.assertEqual(
				self.fight_format._flight_resistance_force(65.2),
				"Сила сопротивления = 65.2 м/с^2"
				)

	def test_flight_resistance_force_env(unittest.TestCase):
		self.assertEqual(
				self.fight_format._flight_resistance_force_env(43.6),
				"Сила сопротивления среды = 43.6 м/с^2"
				)


if __name__ == "__main__":
	unittest.main()

