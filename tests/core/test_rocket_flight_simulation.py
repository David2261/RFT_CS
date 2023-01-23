import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest
import numpy as np

from setup.constant import (
	ATMOSPHERIC_DENSITY,
	ACCELERATION_FREE_FALL,
	CROSS_SECTION_AREA,
	UNIVERSAL_GAS_CONSTANT,
	EARTH_RADIUS
)
from setup.settings import (
	INITIAL_DISTANCE,
	AVERAGE_MOLAR_MASS,
	BURNING_TEMPERATURE,
	FPV,
	TVV,
	BEGIN_RADIUS_ROCKET
)
from rocket_flight_simulation import (
	distance_N_step,
	tg_Beta,
	elliptical_range,
	mass_rocket,
	amount_gas_released,
	overpressure,
	thrust_force,
	impuls,
	height_rocket,
	CylindricalCavity,
	Resistance,
	Speed,
	ModelFlight
)


@pytest.mark.rfs
class TestDistanceNStep:
	""" Тест для distance_N_step """
	fuelFlow = 581
	n = 3

	def test_distance_n_step(self):
		check = distance_N_step(self.fuelFlow, self.n)
		result = INITIAL_DISTANCE - self.n * self.fuelFlow
		assert check == result

	def test_distance_n_step_type(self):
		result = distance_N_step(self.fuelFlow, self.n)
		assert isinstance(result, (int, float))

	def test_distance_n_step_less(self):
		result = distance_N_step(self.fuelFlow, self.n)
		result_more = result + 1
		assert result < result_more

	def test_distance_n_step_more(self):
		result = distance_N_step(self.fuelFlow, self.n)
		result_more = result - 1
		assert result > result_more

	def test_distance_n_step_ist_none(self):
		result = distance_N_step(self.fuelFlow, self.n)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestDistanceNStepError:
	""" Тест исключений для distance_N_step """
	fuelFlow = 581
	n = 3
	fake = 'fake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_distance_n_step_type_1_args_error(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fake, self.n)

	# Тестирование на ошибочный 2 тип параметра функции
	def test_distance_n_step_type_2_args_error(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fuelFlow, self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_distance_n_step_less_args(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fake)

	# Тестирование без аргументов
	def test_distance_n_step_less_args(self):
		with pytest.raises(TypeError):
			result = distance_N_step()

	# Тестирование на большее кол-во аргументов
	def test_distance_n_step_more_args(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fuelFlow, self.fake, 2343)


@pytest.mark.rfs
class TestTgBeta:
	""" Тест для tg_Beta """
	speed = 581

	def test_tg_beta(self):
		check = tg_Beta(self.speed)
		v = (self.speed * BEGIN_RADIUS_ROCKET) / 398_621
		result = v / (2 * np.sqrt(abs(1 - v)))
		assert result == check

	def test_tg_beta_type(self):
		result = tg_Beta(self.speed)
		assert isinstance(result, (int, float))

	def test_tg_beta_less(self):
		result = tg_Beta(self.speed)
		result_more = result + 1
		assert result < result_more

	def test_tg_beta_more(self):
		result = tg_Beta(self.speed)
		result_more = result - 1
		assert result > result_more

	def test_tg_beta_ist_none(self):
		result = tg_Beta(self.speed)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestTgBetaError:
	""" Тест исключений для tg_Beta """
	speed = 581
	fake = 'fake'

	# Тестирование на ошибочный тип параметра функции
	def test_tg_beta_type_args_error(self):
		with pytest.raises(TypeError):
			result = tg_Beta(self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_tg_beta_less_args(self):
		with pytest.raises(TypeError):
			result = tg_Beta()

	# Тестирование на большее кол-во аргументов
	def test_tg_beta_more_args(self):
		with pytest.raises(TypeError):
			result = tg_Beta(self.speed, self.fake)


@pytest.mark.rfs
class TestEllipticalRange:
	""" Тест для elliptical_range """
	speed = 581

	def test_elliptical_range(self):
		check = elliptical_range(self.speed)
		R = EARTH_RADIUS
		Tang = tg_Beta(self.speed)
		result = 2 * R * np.arctan(Tang)
		assert result == check

	def test_elliptical_range_type(self):
		result = elliptical_range(self.speed)
		assert isinstance(result, (int, float))

	def test_elliptical_range_less(self):
		result = elliptical_range(self.speed)
		result_more = result + 1
		assert result < result_more

	def test_elliptical_range_more(self):
		result = elliptical_range(self.speed)
		result_more = result - 1
		assert result > result_more

	def test_elliptical_range_ist_none(self):
		result = elliptical_range(self.speed)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestEllipticalRangeError:
	""" Тест исключений для elliptical_range """
	speed = 581
	fake = 'fake'

	# Тестирование на ошибочный тип параметра функции
	def test_elliptical_range_type_args_error(self):
		with pytest.raises(TypeError):
			result = elliptical_range(self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_elliptical_range_less_args(self):
		with pytest.raises(TypeError):
			result = elliptical_range()

	# Тестирование на большее кол-во аргументов
	def test_elliptical_range_more_args(self):
		with pytest.raises(TypeError):
			result = elliptical_range(self.speed, self.fake)


@pytest.mark.rfs
class TestMassRocket:
	""" Тест для mass_rocket """
	emptyRocket = 581
	fuelWidth = 400

	def test_mass_rocket(self):
		check = mass_rocket(self.emptyRocket, self.fuelWidth)
		result = float(self.emptyRocket + self.fuelWidth)
		assert result == check

	def test_mass_rocket_type(self):
		result = mass_rocket(self.emptyRocket, self.fuelWidth)
		assert isinstance(result, (int, float))

	def test_mass_rocket_less(self):
		result = mass_rocket(self.emptyRocket, self.fuelWidth)
		result_more = result + 1
		assert result < result_more

	def test_mass_rocket_more(self):
		result = mass_rocket(self.emptyRocket, self.fuelWidth)
		result_more = result - 1
		assert result > result_more

	def test_mass_rocket_ist_none(self):
		result = mass_rocket(self.emptyRocket, self.fuelWidth)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestMassRocketError:
	""" Тест исключений для mass_rocket """
	emptyRocket = 581
	fuelWidth = 400
	fake = 'fake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_mass_rocket_1_type_args_error(self):
		with pytest.raises(TypeError):
			result = mass_rocket(self.emptyRocket, self.fake)

	# Тестирование на ошибочный 2 тип параметра функции
	def test_mass_rocket_2_type_args_error(self):
		with pytest.raises(TypeError):
			result = mass_rocket(self.fake, self.fuelFlow)

	# Тестирование на меньшое кол-во аргументов
	def test_mass_rocket_less_args(self):
		with pytest.raises(TypeError):
			result = mass_rocket()

	# Тестирование на большее кол-во аргументов
	def test_mass_rocket_more_args(self):
		with pytest.raises(TypeError):
			result = mass_rocket(self.emptyRocket, self.fuelFlow, self.fake)


@pytest.mark.rfs
class TestAmountGasReleased:
	""" Тест для amount_gas_released """
	mass = 581

	def test_amount_gas_released(self):
		check = amount_gas_released(self.mass)
		result = float(self.mass / AVERAGE_MOLAR_MASS)
		assert result == check

	def test_amount_gas_released_type(self):
		result = amount_gas_released(self.mass)
		assert isinstance(result, (int, float))

	def test_amount_gas_released_less(self):
		result = amount_gas_released(self.mass)
		result_more = result + 1
		assert result < result_more

	def test_amount_gas_released_more(self):
		result = amount_gas_released(self.mass)
		result_more = result - 1
		assert result > result_more

	def test_amount_gas_released_ist_none(self):
		result = amount_gas_released(self.mass)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestAmountGasReleasedError:
	""" Тест исключений для amount_gas_released """
	mass = 581
	fake = 'fake'

	# Тестирование на ошибочный тип параметра функции
	def test_amount_gas_released_type_args_error(self):
		with pytest.raises(TypeError):
			result = amount_gas_released(self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_mass_rocket_less_args(self):
		with pytest.raises(TypeError):
			result = amount_gas_released()

	# Тестирование на большее кол-во аргументов
	def test_mass_rocket_more_args(self):
		with pytest.raises(TypeError):
			result = amount_gas_released(self.mass, self.fake)


@pytest.mark.rfs
class TestAmountGasReleased:
	""" Тест для amount_gas_released """
	mass = 581

	def test_amount_gas_released(self):
		check = amount_gas_released(self.mass)
		result = float(self.mass / AVERAGE_MOLAR_MASS)
		assert result == check

	def test_amount_gas_released_type(self):
		result = amount_gas_released(self.mass)
		assert isinstance(result, (int, float))

	def test_amount_gas_released_less(self):
		result = amount_gas_released(self.mass)
		result_more = result + 1
		assert result < result_more

	def test_amount_gas_released_more(self):
		result = amount_gas_released(self.mass)
		result_more = result - 1
		assert result > result_more

	def test_amount_gas_released_ist_none(self):
		result = amount_gas_released(self.mass)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestAmountGasReleasedError:
	""" Тест исключений для amount_gas_released """
	mass = 581
	fake = 'fake'

	# Тестирование на ошибочный тип параметра функции
	def test_amount_gas_released_type_args_error(self):
		with pytest.raises(TypeError):
			result = amount_gas_released(self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_amount_gas_released_less_args(self):
		with pytest.raises(TypeError):
			result = amount_gas_released()

	# Тестирование на большее кол-во аргументов
	def test_amount_gas_released_more_args(self):
		with pytest.raises(TypeError):
			result = amount_gas_released(self.mass, self.fake)


@pytest.mark.rfs
class TestOverpressure:
	""" Тест для overpressure """
	step = 3

	def test_overpressure(self):
		check = overpressure(self.step)
		h = AVERAGE_MOLAR_MASS * UNIVERSAL_GAS_CONSTANT * BURNING_TEMPERATURE
		res = float(h / self.step)
		assert result == check

	def test_overpressure_type(self):
		result = overpressure(self.step)
		assert isinstance(result, (int, float))

	def test_overpressure_less(self):
		result = overpressure(self.step)
		result_more = result + 1
		assert result < result_more

	def test_overpressure_more(self):
		result = overpressure(self.step)
		result_more = result - 1
		assert result > result_more

	def test_overpressure_ist_none(self):
		result = overpressure(self.step)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestOverpressureError:
	""" Тест исключений для overpressure """
	step = 3
	fake = 'fake'

	# Тестирование на ошибочный тип параметра функции
	def test_overpressure_type_args_error(self):
		with pytest.raises(TypeError):
			result = overpressure(self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_overpressure_less_args(self):
		with pytest.raises(TypeError):
			result = overpressure()

	# Тестирование на большее кол-во аргументов
	def test_overpressure_more_args(self):
		with pytest.raises(TypeError):
			result = overpressure(self.step, self.fake)


@pytest.mark.rfs
class TestThrustForse:
	""" Тест для thrust_force """
	pressure = 1400

	def test_thrust_force(self):
		check = thrust_force(self.pressure)
		result = self.pressure * CROSS_SECTION_AREA
		assert result == check

	def test_thrust_force_type(self):
		result = thrust_force(self.pressure)
		assert isinstance(result, (int, float))

	def test_thrust_force_less(self):
		result = thrust_force(self.pressure)
		result_more = result + 1
		assert result < result_more

	def test_thrust_force_more(self):
		result = thrust_force(self.pressure)
		result_more = result - 1
		assert result > result_more

	def test_thrust_force_ist_none(self):
		result = thrust_force(self.pressure)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestThrustForseError:
	""" Тест исключений для thrust_force """
	pressure = 1400
	fake = 'fake'

	# Тестирование на ошибочный тип параметра функции
	def test_thrust_force_type_args_error(self):
		with pytest.raises(TypeError):
			result = thrust_force(self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_thrust_force_less_args(self):
		with pytest.raises(TypeError):
			result = thrust_force()

	# Тестирование на большее кол-во аргументов
	def test_thrust_force_more_args(self):
		with pytest.raises(TypeError):
			result = thrust_force(self.pressure, self.fake)


@pytest.mark.rfs
class TestImpuls:
	""" Тест для impuls """
	pressure = 1400
	time = 300

	def test_impuls(self):
		check = impuls(self.pressure, self.time)
		tf = thrust_force(self.pressure)
		result = float(tf * self.time)
		assert result == check

	def test_impuls_type(self):
		result = impuls(self.pressure, self.time)
		assert isinstance(result, (int, float))

	def test_impuls_less(self):
		result = impuls(self.pressure, self.time)
		result_more = result + 1
		assert result < result_more

	def test_impuls_more(self):
		result = impuls(self.pressure, self.time)
		result_more = result - 1
		assert result > result_more

	def test_impuls_ist_none(self):
		result = impuls(self.pressure, self.time)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestImpulsError:
	""" Тест исключений для impuls """
	pressure = 1400
	time = 300
	fake = 'fake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_impuls_type_args_error(self):
		with pytest.raises(TypeError):
			result = impuls(self.fake, self.time)

	# Тестирование на ошибочный 2 тип параметра функции
	def test_impuls_type_args_error(self):
		with pytest.raises(TypeError):
			result = impuls(self.pressure, self.fake)

	# Тестирование на меньшое кол-во аргументов
	def test_impuls_less_to_1_args(self):
		with pytest.raises(TypeError):
			result = impuls(self.pressure)

	# Тестирование на меньшое кол-во аргументов
	def test_impuls_less_to_2_args(self):
		with pytest.raises(TypeError):
			result = impuls(self.time)

	# Тестирование без аргументов аргументов
	def test_impuls_without_args(self):
		with pytest.raises(TypeError):
			result = impuls()

	# Тестирование на большее кол-во аргументов
	def test_impuls_more_args(self):
		with pytest.raises(TypeError):
			result = impuls(self.pressure, self.time, self.fake)


@pytest.mark.rfs
class TestHeightRocket:
	""" Тест для height_rocket """
	heightStart = 120
	heightStage = 280
	stage = 3

	def test_height_rocket(self):
		check = height_rocket(
			self.heightStart,
			self.heightStage,
			self.stage
		)
		result = float(self.heightStart + self.heightStage * self.stage)
		assert result == check

	def test_height_rocket_type(self):
		result = height_rocket(
			self.heightStart,
			self.heightStage,
			self.stage
		)
		assert isinstance(result, (int, float))

	def test_height_rocket_less(self):
		result = height_rocket(
			self.heightStart,
			self.heightStage,
			self.stage
		)
		result_more = result + 1
		assert result < result_more

	def test_height_rocket_more(self):
		result = height_rocket(
			self.heightStart,
			self.heightStage,
			self.stage
		)
		result_more = result - 1
		assert result > result_more

	def test_height_rocket_ist_none(self):
		result = height_rocket(
			self.heightStart,
			self.heightStage,
			self.stage
		)
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestHeightRocketError:
	""" Тест исключений для height_rocket """
	heightStart = 120
	heightStage = 280
	stage = 3
	fake = 'fake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_height_rocket_type_1_args_error(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.fake,
						self.heightStage,
						self.stage
					)

	# Тестирование на ошибочный 2 тип параметра функции
	def test_height_rocket_type_2_args_error(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.fake,
						self.stage
					)

	# Тестирование на ошибочный 3 тип параметра функции
	def test_height_rocket_type_3_args_error(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.heightStage,
						self.fake
					)

	# Тестирование на меньшое 1 кол-во аргументов
	def test_height_rocket_less_to_1_args(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStage,
						self.stage
					)

	# Тестирование на меньшое 2 кол-во аргументов
	def test_height_rocket_less_to_2_args(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.stage
					)

	# Тестирование на меньшое 3 кол-во аргументов
	def test_height_rocket_less_to_3_args(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.heightStage,
					)

	# Тестирование без аргументов аргументов
	def test_height_rocket_without_args(self):
		with pytest.raises(TypeError):
			result = height_rocket()

	# Тестирование на большее кол-во аргументов
	def test_height_rocket_more_args(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.heightStage,
						self.stage,
						self.fake
					)


@pytest.mark.rfs
@pytest.mark.xfail
class TestCylindricalCavity:
	"""Тест _body_area"""
	U = 41187.93
	n = 4
	L = 0.45

	# Тестирвание вычисления функции
	def test_volume_cylindrical_cavity(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		R_0 = INITIAL_DISTANCE
		_cc = R_0 + self.n * self.U
		check = np.pi * float((_cc**2) * self.L)
		assert result == check

	# Тестирование типа вывода функции
	def test_volume_cylindrical_cavity_type(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_volume_cylindrical_cavity_less(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		check = result + 1
		assert result < check

	def test_volume_cylindrical_cavity_more(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		check = result - 1
		assert result > check

	def test_volume_cylindrical_cavity_ist_none(self):
		CC = CylindricalCavity(self.U, self.n, self.L)
		result = CC.volume_cylindrical_cavity()
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestCylindricalCavityError:
	"""Тест _body_area с ошибкой"""
	...
