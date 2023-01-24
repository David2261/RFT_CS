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
	"""Тест CylindricalCavity"""
	burnFuel = 41187.93
	step = 4
	size = 0.45

	# Тестирвание вычисления функции
	def test_volume_cylindrical_cavity(self):
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		result = CC.volume_cylindrical_cavity()
		radius = INITIAL_DISTANCE + self.step * self.size
		check = np.pi * float((pow(radius, 2)) * self.size)
		assert result == check

	# Тестирование типа вывода функции
	def test_volume_cylindrical_cavity_type(self):
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		result = CC.volume_cylindrical_cavity()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_volume_cylindrical_cavity_less(self):
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		result = CC.volume_cylindrical_cavity()
		check = result + 1
		assert result < check

	def test_volume_cylindrical_cavity_more(self):
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		result = CC.volume_cylindrical_cavity()
		check = result - 1
		assert result > check

	def test_volume_cylindrical_cavity_ist_none(self):
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		result = CC.volume_cylindrical_cavity()
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
@pytest.mark.xfail
class TestCylindricalCavityError:
	"""Тест CylindricalCavity с ошибкой"""
	burnFuel = 41187.93
	step = 4
	size = 0.45
	fake = 'fake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_volume_cylindrical_cavity_type_1_args_error(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.fake, self.step, self.size)
			result = CC.volume_cylindrical_cavity()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_volume_cylindrical_cavity_type_2_args_error(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.burnFuel, self.fake, self.size)
			result = CC.volume_cylindrical_cavity()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_volume_cylindrical_cavity_type_3_args_error(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.burnFuel, self.step, self.fake)
			result = CC.volume_cylindrical_cavity()

	# Тестирование на меньшое 1 кол-во аргументов
	def test_volume_cylindrical_cavity_less_to_1_args(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.step, self.size)
			result = CC.volume_cylindrical_cavity()

	# Тестирование на меньшое 2 кол-во аргументов
	def test_volume_cylindrical_cavity_less_to_2_args(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.burnFuel, self.size)
			result = CC.volume_cylindrical_cavity()

	# Тестирование на меньшое 3 кол-во аргументов
	def test_volume_cylindrical_cavity_less_to_3_args(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.burnFuel, self.step)
			result = CC.volume_cylindrical_cavity()

	# Тестирование без аргументов аргументов
	def test_volume_cylindrical_cavity_without_args(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity()
			result = CC.volume_cylindrical_cavity()

	# Тестирование на большее кол-во аргументов
	def test_volume_cylindrical_cavity_more_args(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(
					self.burnFuel,
					self.step,
					self.size,
					self.fake
				)
			result = CC.volume_cylindrical_cavity()


@pytest.mark.rfs
class TestResistance:
	""" Тест для Resistance """
	speed = 450
	thrust_force = 230
	mass =  650

	def test_aerodynamic_pressure(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist._aerodynamic_pressure()
		result = (ATMOSPHERIC_DENSITY * (pow(self.speed, 2))) / 2
		assert result == check

	def test_aerodynamic_pressure_type(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist._aerodynamic_pressure()
		assert isinstance(result, (int, float))

	def test_aerodynamic_pressure_less(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist._aerodynamic_pressure()
		result_more = result + 1
		assert result < result_more

	def test_aerodynamic_pressure_more(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist._aerodynamic_pressure()
		result_more = result - 1
		assert result > result_more

	def test_aerodynamic_pressure_ist_none(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist._aerodynamic_pressure()
		assert result != None

	def test_aerodynamic_drag(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist.aerodynamic_drag()
		Q = resist.aerodynamic_drag()
		Cx = CROSS_SECTION_AREA
		S = Cx
		result = Cx * S * Q
		assert result == check

	def test_aerodynamic_drag_type(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.aerodynamic_drag()
		assert isinstance(result, (int, float))

	def test_aerodynamic_drag_less(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.aerodynamic_drag()
		result_more = result + 1
		assert result < result_more

	def test_aerodynamic_drag_more(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.aerodynamic_drag()
		result_more = result - 1
		assert result > result_more

	def test_aerodynamic_drag_ist_none(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.aerodynamic_drag()
		assert result != None

	def test_gravitation_losses(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist.gravitation_losses()
		G = ACCELERATION_FREE_FALL
		angel = np.sin(FPV)
		res = G * angel
		assert result == check

	def test_gravitation_losses_type(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.gravitation_losses()
		assert isinstance(result, (int, float))

	def test_gravitation_losses_less(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.gravitation_losses()
		result_more = result + 1
		assert result < result_more

	def test_gravitation_losses_more(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.gravitation_losses()
		result_more = result - 1
		assert result > result_more

	def test_gravitation_losses_ist_none(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.gravitation_losses()
		assert result != None

	def test_control_losses(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist.control_losses()
		G = ACCELERATION_FREE_FALL
		angel = np.sin(FPV)
		res = G * angel
		assert result == check

	def test_control_losses_type(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.control_losses()
		assert isinstance(result, (int, float))

	def test_control_losses_less(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.control_losses()
		result_more = result + 1
		assert result < result_more

	def test_control_losses_more(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.control_losses()
		result_more = result - 1
		assert result > result_more

	def test_control_losses_ist_none(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.control_losses()
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestResistanceError:
	""" Тест исключений для Resistance """
	speed = 450
	thrust_force = 230
	mass =  650
	fake = 'fake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_aerodynamic_pressure_type_1_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.fake, self.thrust_force, self.mass)
			result = resist._aerodynamic_pressure()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_aerodynamic_pressure_type_2_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.fake, self.mass)
			result = resist._aerodynamic_pressure()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_aerodynamic_pressure_type_3_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.thrust_force, self.fake)
			result = resist._aerodynamic_pressure()

	# Тестирование на меньшое 1 кол-во аргументов
	def test_aerodynamic_pressure_less_to_1_args(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.thrust_force, self.mass)
			result = resist._aerodynamic_pressure()

	# Тестирование на меньшое 2 кол-во аргументов
	def test_aerodynamic_pressure_less_to_2_args(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.mass)
			result = resist._aerodynamic_pressure()

	# Тестирование на меньшое 3 кол-во аргументов
	def test_aerodynamic_pressure_less_to_3_args(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.thrust_force)
			result = resist._aerodynamic_pressure()

	# Тестирование без аргументов аргументов
	def test_aerodynamic_pressure_without_args(self):
		with pytest.raises(TypeError):
			resist = Resistance()
			result = resist._aerodynamic_pressure()

	# Тестирование на большее кол-во аргументов
	def test_aerodynamic_pressure_more_args(self):
		with pytest.raises(TypeError):
			resist = Resistance(
					self.speed,
					self.thrust_force,
					self.mass,
					self.fake
				)
			result = resist._aerodynamic_pressure()

	# Тестирование на ошибочный 1 тип параметра функции
	def test_aerodynamic_drag_type_1_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.fake, self.thrust_force, self.mass)
			result = resist.aerodynamic_drag()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_aerodynamic_drag_type_2_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.fake, self.mass)
			result = resist.aerodynamic_drag()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_aerodynamic_drag_type_3_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.thrust_force, self.fake)
			result = resist.aerodynamic_drag()

	# Тестирование на ошибочный 1 тип параметра функции
	def test_gravitation_losses_type_1_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.fake, self.thrust_force, self.mass)
			result = resist.gravitation_losses()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_gravitation_losses_type_2_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.fake, self.mass)
			result = resist.gravitation_losses()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_gravitation_losses_type_3_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.thrust_force, self.fake)
			result = resist.gravitation_losses()

	# Тестирование на ошибочный 1 тип параметра функции
	def test_control_losses_type_1_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.fake, self.thrust_force, self.mass)
			result = resist.control_losses()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_control_losses_type_2_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.fake, self.mass)
			result = resist.control_losses()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_control_losses_type_3_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.thrust_force, self.fake)
			result = resist.control_losses()


@pytest.mark.rfs
class TestSpeed:
	"""Тест Speed"""
	thrust_force = 459
	gravitation_losses = 0.45
	mass =  650
	time = 240
	speed_0 = 280

	# Тестирвание вычисления функции
	def test_resultant_force(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		check = speed._resultant_force()
		G = ACCELERATION_FREE_FALL
		result = thrust_force(self.speed_0) * self.gravitation_losses - self.mass * G
		assert result == check

	# Тестирование типа вывода функции
	def test_resultant_force_type(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed._resultant_force()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_resultant_force_less(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed._resultant_force()
		check = result + 1
		assert result < check

	def test_resultant_force_more(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed._resultant_force()
		check = result - 1
		assert result > check

	def test_resultant_force_ist_none(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed._resultant_force()
		assert result != None

	# Тестирвание вычисления функции
	def test_rocket_acceleration(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		check = speed.rocket_acceleration()
		F = speed._resultant_force()
		result = F / self.mass
		assert result == check

	# Тестирование типа вывода функции
	def test_rocket_acceleration_type(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed.rocket_acceleration()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_rocket_acceleration_less(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed.rocket_acceleration()
		check = result + 1
		assert result < check

	def test_rocket_acceleration_more(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed.rocket_acceleration()
		check = result - 1
		assert result > check

	def test_rocket_acceleration_ist_none(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed.rocket_acceleration()
		assert result != None

		# Тестирвание вычисления функции
	def test_rocket_speed(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		check = speed.rocket_speed()
		a = speed.rocket_acceleration()
		result = self.speed_0 + a * self.time
		assert result == check

	# Тестирование типа вывода функции
	def test_rocket_speed_type(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed.rocket_speed()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_rocket_speed_less(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed.rocket_speed()
		check = result + 1
		assert result < check

	def test_rocket_speed_more(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed.rocket_speed()
		check = result - 1
		assert result > check

	def test_rocket_speed_ist_none(self):
		speed = Speed(
			self.thrust_force,
			self.gravitation_losses,
			self.mass,
			self.time,
			self.speed_0
		)
		result = speed.rocket_speed()
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestSpeedError:
	"""Тест Speed с ошибкой"""
	thrust_force = 459
	gravitation_losses = 0.45
	mass =  650
	time = 240
	speed_0 = 280
	fake = 'fake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_resultant_force_type_1_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.fake,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0
			)
			result = speed._resultant_force()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_resultant_force_type_2_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.fake,
				self.mass,
				self.time,
				self.speed_0
			)
			result = speed._resultant_force()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_resultant_force_type_3_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.fake,
				self.time,
				self.speed_0
			)
			result = speed._resultant_force()

	# Тестирование на ошибочный 4 тип параметра функции
	def test_resultant_force_type_4_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.fake,
				self.speed_0
			)
			result = speed._resultant_force()

	# Тестирование на ошибочный 5 тип параметра функции
	def test_resultant_force_type_5_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.fake
			)
			result = speed._resultant_force()

	# Тестирование на меньшое 1 кол-во аргументов
	def test_resultant_force_less_to_1_args(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0
			)
			result = speed._resultant_force()

	# Тестирование на меньшое 2 кол-во аргументов
	def test_resultant_force_less_to_2_args(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.mass,
				self.time,
				self.speed_0
			)
			result = speed._resultant_force()

	# Тестирование на меньшое 3 кол-во аргументов
	def test_resultant_force_less_to_3_args(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.time,
				self.speed_0
			)
			result = speed._resultant_force()

	# Тестирование на меньшое 4 кол-во аргументов
	def test_resultant_force_less_to_4_args(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.speed_0
			)
			result = speed._resultant_force()

	# Тестирование на меньшое 5 кол-во аргументов
	def test_resultant_force_less_to_5_args(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time
			)
			result = speed._resultant_force()

	# Тестирование без аргументов аргументов
	def test_resultant_force_without_args(self):
		with pytest.raises(TypeError):
			speed = Speed()
			result = speed._resultant_force()

	# Тестирование на большее кол-во аргументов
	def test_resultant_force_more_args(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0,
				self.fake
			)
		result = speed._resultant_force()

	# Тестирование на ошибочный 1 тип параметра функции
	def test_rocket_acceleration_type_1_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.fake,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0
			)
			result = speed.rocket_acceleration()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_rocket_acceleration_type_2_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.fake,
				self.mass,
				self.time,
				self.speed_0
			)
			result = speed.rocket_acceleration()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_rocket_acceleration_type_3_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.fake,
				self.time,
				self.speed_0
			)
			result = speed.rocket_acceleration()

	# Тестирование на ошибочный 4 тип параметра функции
	def test_rocket_acceleration_type_4_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.fake,
				self.speed_0
			)
			result = speed.rocket_acceleration()

	# Тестирование на ошибочный 5 тип параметра функции
	def test_rocket_acceleration_type_5_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.fake
			)
			result = speed.rocket_acceleration()

	# Тестирование на ошибочный 1 тип параметра функции
	def test_rocket_speed_type_1_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.fake,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0
			)
			result = speed.rocket_speed()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_rocket_speed_type_2_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.fake,
				self.mass,
				self.time,
				self.speed_0
			)
			result = speed.rocket_speed()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_rocket_speed_type_3_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.fake,
				self.time,
				self.speed_0
			)
			result = speed.rocket_speed()

	# Тестирование на ошибочный 4 тип параметра функции
	def test_rocket_speed_type_4_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.fake,
				self.speed_0
			)
			result = speed.rocket_speed()

	# Тестирование на ошибочный 5 тип параметра функции
	def test_rocket_speed_type_5_args_error(self):
		with pytest.raises(TypeError):
			speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.fake
			)
			result = speed.rocket_speed()


@pytest.mark.rfs
class TestModelFlight:
	"""Тест ModelFlight"""
	mass =  650
	speed_0 = 280
	time = 240
	fuel_flow = 12

	# Тестирвание вычисления функции
	def test_total_resistance(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		check = model._total_resistance()
		speed = model._total_speed()
		tf = thrust_force(self.fuel_flow)
		resistance = Resistance(speed, tf, self.mass)
		cont = resistance.control_losses()
		gl = resistance.gravitation_losses()
		ad = resistance.aerodynamic_drag()
		result = cont + gl + ad
		assert result == check

	# Тестирование типа вывода функции
	def test_total_resistance_type(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_resistance()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_total_resistance_less(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_resistance()
		check = result + 1
		assert result < check

	def test_total_resistance_more(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_resistance()
		check = result - 1
		assert result > check

	def test_total_resistance_ist_none(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_resistance()
		assert result != None

	# Тестирвание вычисления функции
	def test_total_speed(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		check = model._total_speed()
		tf = thrust_force(self.fuel_flow)
		resistance = Resistance(self.speed_0, tf, self.mass)
		gl = resistance.gravitation_losses()
		spd = Speed(tf, gl, self.mass, self.time, self.speed_0)
		result = spd.rocket_speed()
		assert result == check

	# Тестирование типа вывода функции
	def test_total_speed_type(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_speed()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_total_speed_less(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_speed()
		check = result + 1
		assert result < check

	def test_total_speed_more(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_speed()
		check = result - 1
		assert result > check

	def test_total_speed_ist_none(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_speed()
		assert result != None

	# Тестирвание вычисления функции
	def test_total_distance(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		check = model._total_distance()
		speed = model._total_speed()
		res = elliptical_range(speed)
		assert result == check

	# Тестирование типа вывода функции
	def test_total_distance_type(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_distance()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_total_distance_less(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_distance()
		check = result + 1
		assert result < check

	def test_total_distance_more(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_distance()
		check = result - 1
		assert result > check

	def test_total_distance_ist_none(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model._total_distance()
		assert result != None

	# Тестирвание вычисления функции
	def test_model_stack(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		check = model.model_stack()
		resistance = model._total_resistance()
		speed = model._total_speed()
		distance = model._total_distance()
		Beta = tg_Beta(speed)
		result = [resistance, speed, distance, Beta]
		assert result == check

	# Тестирование типа вывода функции
	def test_model_stack_type(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model.model_stack()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_model_stack_less(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model.model_stack()
		check = result + 1
		assert result < check

	def test_model_stack_more(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model.model_stack()
		check = result - 1
		assert result > check

	def test_model_stack_ist_none(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model.model_stack()
		assert result != None


@pytest.mark.rfs
@pytest.mark.exception
class TestModelFlightError:
	"""Тест ModelFlight с ошибкой"""
	mass =  650
	speed_0 = 280
	time = 240
	fuel_flow = 12
	fake = 'fake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_total_resistance_type_1_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.fake,
				self.speed_0,
				self.time,
				self.fuel_flow
			)
			result = model._total_resistance()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_total_resistance_type_2_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.fake,
				self.time,
				self.fuel_flow
			)
			result = model._total_resistance()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_total_resistance_type_3_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.fake,
				self.fuel_flow
			)
			result = model._total_resistance()

	# Тестирование на ошибочный 4 тип параметра функции
	def test_total_resistance_type_4_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fake
			)
			result = model._total_resistance()

	# Тестирование на меньшое 1 кол-во аргументов
	def test_total_resistance_less_to_1_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.speed_0,
				self.time,
				self.fuel_flow
			)
			result = model._total_resistance()

	# Тестирование на меньшое 2 кол-во аргументов
	def test_total_resistance_less_to_2_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.time,
				self.fuel_flow
			)
			result = model._total_resistance()

	# Тестирование на меньшое 3 кол-во аргументов
	def test_total_resistance_less_to_3_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.fuel_flow
			)
			result = model._total_resistance()

	# Тестирование на меньшое 4 кол-во аргументов
	def test_total_resistance_less_to_4_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time
			)
			result = model._total_resistance()

	# Тестирование без аргументов аргументов
	def test_total_resistance_without_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight()
			result = model._total_resistance()

	# Тестирование на большее кол-во аргументов
	def test_total_resistance_more_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow,
				self.fake
			)
			result = model._total_resistance()

	# Тестирование на ошибочный 1 тип параметра функции
	def test_total_speed_type_1_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.fake,
				self.speed_0,
				self.time,
				self.fuel_flow
			)
			result = model._total_speed()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_total_speed_type_2_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.fake,
				self.time,
				self.fuel_flow
			)
			result = model._total_speed()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_total_speed_type_3_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.fake,
				self.fuel_flow
			)
			result = model._total_speed()

	# Тестирование на ошибочный 4 тип параметра функции
	def test_total_speed_type_4_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fake
			)
			result = model._total_speed()

	# Тестирование на ошибочный 1 тип параметра функции
	def test_total_distance_type_1_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.fake,
				self.speed_0,
				self.time,
				self.fuel_flow
			)
			result = model._total_distance()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_total_distance_type_2_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.fake,
				self.time,
				self.fuel_flow
			)
			result = model._total_distance()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_total_distance_type_3_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.fake,
				self.fuel_flow
			)
			result = model._total_distance()

	# Тестирование на ошибочный 4 тип параметра функции
	def test_total_distance_type_4_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fake
			)
			result = model._total_distance()

	# Тестирование на ошибочный 1 тип параметра функции
	def test_model_stack_type_1_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.fake,
				self.speed_0,
				self.time,
				self.fuel_flow
			)
			result = model.model_stack()

	# Тестирование на ошибочный 2 тип параметра функции
	def test_model_stack_type_2_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.fake,
				self.time,
				self.fuel_flow
			)
			result = model.model_stack()

	# Тестирование на ошибочный 3 тип параметра функции
	def test_model_stack_type_3_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.fake,
				self.fuel_flow
			)
			result = model.model_stack()

	# Тестирование на ошибочный 4 тип параметра функции
	def test_model_stack_type_4_args_error(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fake
			)
			result = model.model_stack()
