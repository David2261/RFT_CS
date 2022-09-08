import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest
import numpy as np

from rocket_flight_simulation import (
	_body_area,
	resistance_force,
	frontal_area,
	environmental_resistance,
	resistance_force_env,
	gravity_losses,
	aerodynamic_losses,
	loss_speed_on_control
)
from rocket_fuel_calculation import total_speed


def data_rfs():
	height = 120.0
	width = 30.0
	speed = 2500.0
	array = (height, width, speed)
	return array


@pytest.mark.rfs
class TestBodyArea:
	"""Тест _body_area"""
	data = data_rfs()
	height = data[0]
	width = data[1]

	def test_body_area(self):
		test_result = self.height * self.width
		result = _body_area(self.height, self.width)
		assert test_result == result

	def test_body_area_isinstance(self):
		result = _body_area(self.height, self.width)
		assert isinstance(result, (int, float))

	def test_body_area_less(self):
		test_result = self.height * self.width
		result = _body_area(self.height, self.width)
		test_result += 1
		assert result <= test_result


@pytest.mark.rfs
@pytest.mark.exception
class TestBodyAreaError:
	"""Тест _body_area с ошибкой"""
	data = data_rfs()
	height = data[0]
	width = data[1]

	def test_body_area_type_error(self):
		with pytest.raises(TypeError):
			_body_area('(17,', self.width)

	def test_body_area_more_args(self):
		with pytest.raises(TypeError):
			_body_area(self.height, self.width, 23.1)

	def test_body_area_less_args(self):
		with pytest.raises(TypeError):
			_body_area(self.height)


@pytest.mark.rfs
class TestResistanceForce:
	"""Тест resistance_force"""
	data = data_rfs()
	height = data[0]
	width = data[1]

	def test_resistance_force(self):
		area = _body_area(self.height, self.width)
		V = total_speed(420000.0, 5790000.0, 524.0)
		result = 1.2 * (16900 * V ** 2) / 2 * area
		test_result = resistance_force(self.height, self.width)
		assert test_result == result

	def test_resistance_force_isinstance(self):
		result = resistance_force(self.height, self.width)
		assert isinstance(result, (int, float))

	def test_resistance_force_less(self):
		area = _body_area(self.height, self.width)
		V = total_speed(420000.0, 5790000.0, 524.0)
		result = 1.2 * (16900 * V ** 2) / 2 * area
		result += 1
		test_result = resistance_force(self.height, self.width)
		assert test_result <= result


@pytest.mark.rfs
@pytest.mark.exception
class TestResistanceForceError:
	"""Тест resistance_force с ошибкой"""
	data = data_rfs()
	height = data[0]
	width = data[1]

	def test_resistance_force_type_error(self):
		with pytest.raises(TypeError):
			resistance_force('(17,', self.width)

	def test_resistance_force_more_args(self):
		with pytest.raises(TypeError):
			resistance_force(self.height, self.width, 12.2)

	def test_resistance_force_less_args(self):
		with pytest.raises(TypeError):
			resistance_force(self.height)


@pytest.mark.rfs
class TestFrontalArea:
	"""Тест frontal_area с ошибкой"""
	data = data_rfs()
	height = data[0]
	width = data[1]

	def test_frontal_area(self):
		result = 0.14 * self.width * self.height
		test_result = frontal_area(self.width, self.height)
		assert result == test_result

	def test_frontal_area_type(self):
		test_result = frontal_area(self.width, self.height)
		assert isinstance(test_result, (int, float))

	def test_frontal_area_less(self):
		result = 0.14 * self.width * self.height
		result += 1
		test_result = frontal_area(self.width, self.height)
		assert test_result <= result


@pytest.mark.rfs
@pytest.mark.exception
class TestFrontalAreaError:
	"""Тест frontal_area с ошибкой"""
	data = data_rfs()
	height = data[0]
	width = data[1]

	def test_frontal_area_type_error(self):
		with pytest.raises(TypeError):
			frontal_area('sda', self.height)

	def test_frontal_area_less_args(self):
		with pytest.raises(TypeError):
			frontal_area(self.width)

	def test_frontal_area_more_args(self):
		with pytest.raises(TypeError):
			frontal_area(self.width, self.height, 32.1)


@pytest.mark.rfs
class TestEnvironmentalResistance:
	"""Тест environmental_resistance"""
	rocket_form = 169.2

	def test_environmental_resistance(self):
		result = 0.5 * 1.2754 * 0.14 * self.rocket_form
		test_result = environmental_resistance(self.rocket_form)
		assert result == test_result

	def test_environmental_resistance_type(self):
		result = environmental_resistance(self.rocket_form)
		assert isinstance(result, (int, float))

	def test_environmental_resistance_less(self):
		result = 0.5 * 1.2754 * 0.14 * self.rocket_form
		test_result = environmental_resistance(self.rocket_form)
		result += 1
		assert test_result <= result


@pytest.mark.rfs
@pytest.mark.exception
class TestEnvironmentalResistanceError:
	"""Тест environmental_resistance с ошибкой"""
	rocket_form = 169.2

	def test_environmental_resistance_type_error(self):
		with pytest.raises(TypeError):
			environmental_resistance('(17,')

	def test_environmental_resistance_less_agrs(self):
		with pytest.raises(TypeError):
			environmental_resistance()

	def test_environmental_resistance_more_agrs(self):
		with pytest.raises(TypeError):
			environmental_resistance(self.rocket_form, 23.1)


@pytest.mark.rfs
class TestResistanceForceEnv:
	"""Тест resistance_force_env"""
	data = data_rfs()
	h = data[0]
	w = data[1]
	speed = data[2]

	def test_resistance_force_env(self):
		test_result = resistance_force_env(self.h, self.w, self.speed)
		fa = frontal_area(self.w, self.h)
		result = environmental_resistance(fa * (self.speed ** 2))
		assert round(test_result) == round(result)

	def test_resistance_force_env_type(self):
		result = resistance_force_env(self.h, self.w, self.speed)
		assert isinstance(result, (int, float))

	def test_resistance_force_env_less(self):
		test_result = resistance_force_env(self.h, self.w, self.speed)
		fa = frontal_area(self.w, self.h)
		result = environmental_resistance(fa * (self.speed ** 2))
		result += 1
		assert test_result <= result


@pytest.mark.rfs
@pytest.mark.exception
class TestResistanceForceEnvError:
	"""Тест resistance_force_env с ошибкой"""
	data = data_rfs()
	h = data[0]
	w = data[1]
	speed = data[2]

	def test_resistance_force_env_type_error(self):
		with pytest.raises(TypeError):
			environmental_resistance('(17,', self.w, self.speed)

	def test_resistance_force_env_less_agrs(self):
		with pytest.raises(TypeError):
			environmental_resistance(self.h, self.w)

	def test_resistance_force_env_more_agrs(self):
		with pytest.raises(TypeError):
			environmental_resistance(self.h, self.w, self.speed, 23.1)


@pytest.mark.rfs
class TestGravityLosses:
	"""Тест gravity_losses"""
	gamma = 13.2

	def test_gravity_losses(self):
		test_result = gravity_losses(self.gamma)
		result = 9.81 * np.cos(self.gamma)
		assert test_result == result

	def test_gravity_losses_type(self):
		result = gravity_losses(self.gamma)
		assert isinstance(result, (int, float))

	def test_gravity_losses_less(self):
		test_result = gravity_losses(self.gamma)
		result = 9.81 * np.cos(self.gamma)
		result += 1
		assert test_result <= result


@pytest.mark.rfs
@pytest.mark.exception
class TestGravityLossesError:
	"""Тест gravity_losses с ошибками"""
	gamma = 13.2

	def test_gravity_losses_type_error(self):
		with pytest.raises(TypeError):
			gravity_losses('sda/')

	def test_gravity_losses_less_agrs(self):
		with pytest.raises(TypeError):
			gravity_losses()

	def test_gravity_losses_more_agrs(self):
		with pytest.raises(TypeError):
			gravity_losses(self.gamma, 23.1)


@pytest.mark.rfs
class TestAerodynamicLosses:
	"""Тест aerodynamic_losses"""
	A = 45.23
	m = 528.0

	def test_aerodynamic_losses(self):
		result = self.A / self.m
		test_result = aerodynamic_losses(self.A, self.m)
		assert test_result == result

	def test_aerodynamic_losses_type(self):
		result = aerodynamic_losses(self.A, self.m)
		assert isinstance(result, (int, float))

	def test_aerodynamic_losses_less(self):
		result = self.A / self.m
		test_result = aerodynamic_losses(self.A, self.m)
		result += 1
		assert test_result <= result


@pytest.mark.rfs
@pytest.mark.exception
class TestAerodynamicLossesError:
	"""Тест aerodynamic_losses с ошибками"""
	A = 45.23
	m = 528.0

	def test_aerodynamic_losses_type_error(self):
		with pytest.raises(TypeError):
			aerodynamic_losses('(sde/', self.m)

	def test_aerodynamic_losses_less_args(self):
		with pytest.raises(TypeError):
			aerodynamic_losses(self.A)

	def test_aerodynamic_losses_more_args(self):
		with pytest.raises(TypeError):
			aerodynamic_losses(self.A, self.m, 23.1)


@pytest.mark.rfs
class TestLossSpeedControl:
	"""Тест loss_speed_on_control"""
	F = 4567.23
	m = 528.0
	alpha = 13.7

	def test_loss_speed_control(self):
		test_result = loss_speed_on_control(self.F, self.m, self.alpha)
		result = (self.F / self.m) * (1 - np.cos(self.alpha))
		assert test_result == result

	def test_loss_speed_control_type(self):
		result = loss_speed_on_control(self.F, self.m, self.alpha)
		assert isinstance(result, (int, float))

	def test_loss_speed_control_less(self):
		test_result = loss_speed_on_control(self.F, self.m, self.alpha)
		result = (self.F / self.m) * (1 - np.cos(self.alpha))
		result += 1
		assert test_result <= result


@pytest.mark.rfs
@pytest.mark.exception
class TestLossSpeedControlError:
	"""Тест loss_speed_on_control с ошибками"""
	F = 4567.23
	m = 528.0
	alpha = 13.7

	def test_loss_speed_control_type_error(self):
		with pytest.raises(TypeError):
			loss_speed_on_control('(sde/', self.m)

	def test_loss_speed_control_less_args(self):
		with pytest.raises(TypeError):
			loss_speed_on_control(self.F)

	def test_loss_speed_control_more_args(self):
		with pytest.raises(TypeError):
			loss_speed_on_control(self.F, self.m, self.alpha, 231.1)
