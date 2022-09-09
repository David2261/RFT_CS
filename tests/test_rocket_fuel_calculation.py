"""
Файл для тестирования расчетов топлива ракеты
"""
import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import numpy as np
import pytest

from rocket_fuel_calculation import (
	natural_logarithm,
	euler,
	total_speed,
	total_oil,
	massa_construction_rocket
)


def data_rfc():
	# empty mass
	me = 524.0
	# full mass
	mf = 579.0
	Isp = 4200.0
	speed = 2500.0
	array = (me, mf, Isp, speed)
	return array


@pytest.mark.rfc
class TestNaturalLogarithm:
	"""Тест natural_logarithm"""
	data = data_rfc()
	Me = data[0]
	Mf = data[1]

	def test_natural_logarithm(self):
		test_result = natural_logarithm(self.Mf, self.Me)
		result = np.log(self.Mf / self.Me)
		assert test_result == result

	def test_natural_logarithm_type(self):
		result = natural_logarithm(self.Mf, self.Me)
		assert isinstance(result, (int, float))

	def test_natural_logarithm_less(self):
		test_result = natural_logarithm(self.Mf, self.Me)
		result = np.log(self.Mf / self.Me) + 1
		assert test_result <= result


@pytest.mark.rfc
@pytest.mark.exception
class TestNaturalLogarithmError:
	"""Тест natural_logarithm с ошибкой"""
	data = data_rfc()
	Me = data[0]
	Mf = data[1]

	def test_natural_logarithm_type_error(self):
		with pytest.raises(TypeError):
			natural_logarithm('sdsa/', self.Me)

	def test_natural_logarithm_less_args(self):
		with pytest.raises(TypeError):
			natural_logarithm(self.Mf)

	def test_natural_logarithm_more_args(self):
		with pytest.raises(TypeError):
			natural_logarithm(self.Mf, self.Me, 23.2)


@pytest.mark.rfc
class TestEuler:
	"""Тест euler"""
	data = data_rfc()
	Isp = data[2]
	speed = data[3]

	def test_euler(self):
		test_result = euler(self.speed, self.Isp)
		result = np.exp(self.speed / (self.Isp * 9.81))
		assert test_result == result

	def test_euler_type(self):
		result = euler(self.speed, self.Isp)
		assert isinstance(result, (int, float))

	def test_euler_less(self):
		test_result = euler(self.speed, self.Isp)
		result = np.exp(self.speed / (self.Isp * 9.81))
		result += 1
		assert test_result <= result


@pytest.mark.rfc
@pytest.mark.exception
class TestEulerError:
	"""Тест euler с ошибкой"""
	data = data_rfc()
	Isp = data[2]
	speed = data[3]

	def test_euler_type_error(self):
		with pytest.raises(TypeError):
			natural_logarithm('sdsa/', self.Isp)

	def test_euler_less_args(self):
		with pytest.raises(TypeError):
			natural_logarithm(self.speed)

	def test_euler_more_args(self):
		with pytest.raises(TypeError):
			natural_logarithm(self.speed, self.Isp, 23.2)


@pytest.mark.rfc
class TestTotalSpeed:
	"""Тест total_speed"""
	data = data_rfc()
	Me = data[0]
	Mf = data[1]
	Isp = data[2]

	def test_total_speed(self):
		test_result = total_speed(self.Isp, self.Mf, self.Me)
		natural_log = natural_logarithm(self.Mf, self.Me)
		result = self.Isp * 9.81 * natural_log
		assert test_result == result

	def test_total_speed_less(self):
		test_result = total_speed(self.Isp, self.Mf, self.Me)
		natural_log = natural_logarithm(self.Mf, self.Me)
		result = self.Isp * 9.81 * natural_log + 1
		assert test_result <= result

	def test_total_speed_type(self):
		result = total_speed(self.Isp, self.Mf, self.Me)
		assert isinstance(result, (int, float))


@pytest.mark.rfc
@pytest.mark.exception
class TestTotalSpeedError:
	"""Тест total_speed с ошибкой"""
	data = data_rfc()
	Me = data[0]
	Mf = data[1]
	Isp = data[2]

	def test_total_speed_type_error(self):
		with pytest.raises(TypeError):
			total_speed('ssd/', self.Mf, self.Me)

	def test_total_speed_less_args(self):
		with pytest.raises(TypeError):
			total_speed(self.Isp, self.Mf)

	def test_total_speed_more_args(self):
		with pytest.raises(TypeError):
			total_speed(self.Isp, self.Mf, self.Me, 23.1)


@pytest.mark.rfc
class TestTotalOil:
	"""Тест total_oil"""
	data = data_rfc()
	Me = data[0]
	Isp = data[2]
	speed = data[3]

	def test_total_oil(self):
		test_result = total_oil(self.Isp, self.speed, self.Me)
		e = euler(self.speed, self.Isp)
		result = self.Me * (e - 1)
		assert test_result == result

	def test_total_oil_less(self):
		test_result = total_oil(self.Isp, self.speed, self.Me)
		e = euler(self.speed, self.Isp)
		result = self.Me * (e - 1) + 1
		assert test_result <= result

	def test_total_oil(self):
		result = total_oil(self.Isp, self.speed, self.Me)
		assert isinstance(result, (int, float))


@pytest.mark.rfc
@pytest.mark.exception
class TestTotalOilError:
	"""Тест total_oil с ошибкой"""
	data = data_rfc()
	Me = data[0]
	Isp = data[2]
	speed = data[3]

	def test_total_speed_type_error(self):
		with pytest.raises(TypeError):
			total_oil('ssd/', self.speed, self.Me)

	def test_total_speed_less_args(self):
		with pytest.raises(TypeError):
			total_oil(self.Isp, self.speed)

	def test_total_speed_more_args(self):
		with pytest.raises(TypeError):
			total_oil(self.Isp, self.speed, self.Me, 23.1)


@pytest.mark.rfc
class TestMassConstructionRocket:
	"""Тест massa_construction_rocket"""
	data = data_rfc()
	Me = data[0]
	Isp = data[2]
	speed = data[3]
	Mp = total_oil(Isp, speed, Me)

	def test_mass_construction_rocket(self):
		test_result = massa_construction_rocket(self.Mp)
		result = self.Mp / 400
		assert test_result == result

	def test_mass_construction_rocket_less(self):
		test_result = massa_construction_rocket(self.Mp)
		result = self.Mp / 400 + 1
		assert test_result <= result

	def test_mass_construction_rocket_type(self):
		result = massa_construction_rocket(self.Mp)
		assert isinstance(result, (int, float))


@pytest.mark.rfc
@pytest.mark.exception
class TestMassConstructionRocketError:
	"""Тест massa_construction_rocket с ошибкой"""
	data = data_rfc()
	Me = data[0]
	Isp = data[2]
	speed = data[3]
	Mp = total_oil(Isp, speed, Me)

	def test_mass_construction_rocket_type_error(self):
		with pytest.raises(TypeError):
			massa_construction_rocket('ssd/')

	def test_mass_construction_rocket_less_args(self):
		with pytest.raises(TypeError):
			massa_construction_rocket()

	def test_mass_construction_rocket_more_args(self):
		with pytest.raises(TypeError):
			massa_construction_rocket(self.Mp, 23.1)