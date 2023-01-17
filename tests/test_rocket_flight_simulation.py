import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest
import numpy as np

# from setup.constant import (
# 	ATMOSPHERIC_PRESSURE,
# 	ATMOSPHERIC_DENSITY,
# 	ACCELERATION_FREE_FALL,
# 	CROSS_SECTION_AREA,
# 	VOLUME_EMPTY_CC,
# 	UNIVERSAL_GAS_CONSTANT
# )
from setup.settings import INITIAL_DISTANCE
# FUEL_DENSITY,
# AVERAGE_MOLAR_MASS,
# BURNING_TEMPERATURE,
# FPV,
# TVV
from rocket_flight_simulation import (
	# distance_N_step,
	# mass_rocket,
	# amount_gas_released,
	# overpressure,
	# thrust_force,
	# impuls,
	# height_rocket,
	CylindricalCavity
	# Resistance,
	# Speed
)


@pytest.mark.rfs
class TestCylindricalCavity:
	"""Тест _body_area"""
	U = 41187.93
	n = 4
	L = 0.45

	# Тестирвание вычисления функции
	def test_volume_cylindrical_cavity(self):
		result = CylindricalCavity(self.U, self.n, self.L)
		R_0 = INITIAL_DISTANCE
		R_n = R_0 + self.n * self.U
		answer = np.pi * float((R_n ** 2) * self.L)
		assert result.volume_cylindrical_cavity() == answer

	# Тестирование типа вывода функции
	def test_volume_cylindrical_cavity_type(self):
		result = CylindricalCavity(self.U, self.n, self.L)
		res = result.volume_cylindrical_cavity()
		assert isinstance(res, (float, int))

	# Тестирование на логическую операцию функции
	def test_volume_cylindrical_cavity_less(self):
		result = CylindricalCavity(self.U, self.n, self.L)
		R_n = result._double_angle_sine()
		answer = np.pi * float((R_n ** 2) * self.L)
		assert result.volume_cylindrical_cavity() < (answer + 1)


@pytest.mark.rfs
@pytest.mark.exception
class TestCylindricalCavityError:
	"""Тест _body_area с ошибкой"""
	...
