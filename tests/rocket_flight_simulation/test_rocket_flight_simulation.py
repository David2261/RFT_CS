import pytest
import numpy as np

from RFTCS.setup.constant import (
	ATMOSPHERIC_DENSITY,
	ACCELERATION_FREE_FALL,
	CROSS_SECTION_AREA,
	UNIVERSAL_GAS_CONSTANT,
	EARTH_RADIUS
)
from RFTCS.setup.settings import (
	INITIAL_DISTANCE,
	AVERAGE_MOLAR_MASS,
	BURNING_TEMPERATURE,
	FPV,
	TVV,
	BEGIN_RADIUS_ROCKET
)
from RFTCS.rocket_flight_simulation import (
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
from data import (
	fuelFlow,
	size,
	fake,
	engine,
	weight_empty_rocket,
	weight_fuel_rocket,
	quantity,
	container_pressure,
	time_timer,
	height_begin_place,
	height_stage_place,
	stage_rocket,
	burn_fuel_rocket,
	burn_step_rocket,
	burn_size_rocket,
	thrust_force_rocket,
	mass_rocket,
	gravitation_losses_space,
	start_speed
)


@pytest.mark.rfs
class TestDistanceNStep:
	""" Тест для distance_N_step """
	def __init__(fuelFlow=fuelFlow, size=size):
		fuelFlow = fuelFlow
		size = size

	def test_distance_n_step(self):
		test = distance_N_step(self.fuelFlow, self.size)
		result = INITIAL_DISTANCE - self.size * self.fuelFlow
		assert test == result

	def test_distance_n_step_type(self):
		result = distance_N_step(self.fuelFlow, self.size)
		assert isinstance(result, (int, float))

	def test_distance_n_step_less(self):
		result = distance_N_step(self.fuelFlow, self.size)
		result_more = result + 1
		assert result < result_more

	def test_distance_n_step_more(self):
		result = distance_N_step(self.fuelFlow, self.size)
		result_more = result - 1
		assert result > result_more

	def test_distance_n_step_ist_none(self):
		result = distance_N_step(self.fuelFlow, self.size)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestDistanceNStepError:
	""" Тест исключений для distance_N_step """
	def __init__(fuelFlow=fuelFlow, size=size, fake=fake):
		fuelFlow = fuelFlow
		n = size
		fake = fake

	# Тестирование на ошибочный 1 тип параметра функции
	def test_distance_n_step_type_1_args_error(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fake, self.n)
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_distance_n_step_type_2_args_error(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fuelFlow, self.fake)
			return result

	# Тестирование на меньшое кол-во аргументов
	def test_distance_n_step_less_args(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fake)
			return result

	# Тестирование без аргументов
	def test_distance_n_step_without_args(self):
		with pytest.raises(TypeError):
			result = distance_N_step()
			return result

	# Тестирование на большее кол-во аргументов
	def test_distance_n_step_more_args(self):
		with pytest.raises(TypeError):
			result = distance_N_step(self.fuelFlow, self.fake, 2343)
			return result


@pytest.mark.rfs
class TestTgBeta:
	""" Тест для tg_Beta """
	def __init__(engine=engine, fake=fake):
		speed = engine

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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestTgBetaError:
	""" Тест исключений для tg_Beta """
	def __init__(engine=engine, fake=fake):
		speed = engine
		fake = fake

	# Тестирование на ошибочный тип параметра функции
	def test_tg_beta_type_args_error(self):
		with pytest.raises(TypeError):
			result = tg_Beta(self.fake)
			return result

	# Тестирование на меньшое кол-во аргументов
	def test_tg_beta_less_args(self):
		with pytest.raises(TypeError):
			result = tg_Beta()
			return result

	# Тестирование на большее кол-во аргументов
	def test_tg_beta_more_args(self):
		with pytest.raises(TypeError):
			result = tg_Beta(self.speed, self.fake)
			return result


@pytest.mark.rfs
class TestEllipticalRange:
	""" Тест для elliptical_range """
	def __init__(engine=engine):
		speed = engine

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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestEllipticalRangeError:
	""" Тест исключений для elliptical_range """
	def __init__(engine=engine, fake=fake):
		speed = engine
		fake = fake

	# Тестирование на ошибочный тип параметра функции
	def test_elliptical_range_type_args_error(self):
		with pytest.raises(TypeError):
			result = elliptical_range(self.fake)
			return result

	# Тестирование на меньшое кол-во аргументов
	def test_elliptical_range_less_args(self):
		with pytest.raises(TypeError):
			result = elliptical_range()
			return result

	# Тестирование на большее кол-во аргументов
	def test_elliptical_range_more_args(self):
		with pytest.raises(TypeError):
			result = elliptical_range(self.speed, self.fake)
			return result


@pytest.mark.rfs
class TestMassRocket:
	""" Тест для mass_rocket """
	def __init__(weight_empty_rocket=weight_empty_rocket, weight_fuel_rocket=weight_fuel_rocket):
		emptyRocket = weight_empty_rocket
		fuelWidth = weight_fuel_rocket

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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestMassRocketError:
	""" Тест исключений для mass_rocket """
	def __init__(
		weight_empty_rocket=weight_empty_rocket,
		weight_fuel_rocket=weight_fuel_rocket,
		fake=fake):
		emptyRocket = weight_empty_rocket
		fuelWidth = weight_fuel_rocket
		fake = fake

	# Тестирование на ошибочный 1 тип параметра функции
	def test_mass_rocket_1_type_args_error(self):
		with pytest.raises(TypeError):
			result = mass_rocket(self.emptyRocket, self.fake)
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_mass_rocket_2_type_args_error(self):
		with pytest.raises(TypeError):
			result = mass_rocket(self.fake, self.fuelWidth)
			return result

	# Тестирование на меньшое кол-во аргументов
	def test_mass_rocket_less_args(self):
		with pytest.raises(TypeError):
			result = mass_rocket()
			return result

	# Тестирование на большее кол-во аргументов
	def test_mass_rocket_more_args(self):
		with pytest.raises(TypeError):
			result = mass_rocket(self.emptyRocket, self.fuelWidth, self.fake)
			return result


@pytest.mark.rfs
class TestAmountGasReleased:
	""" Тест для amount_gas_released """
	def __init__(weight_empty_rocket=weight_empty_rocket):
		mass = weight_empty_rocket

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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestAmountGasReleasedError:
	""" Тест исключений для amount_gas_released """
	def __init__(weight_empty_rocket=weight_empty_rocket, fake=fake):
		mass = weight_empty_rocket
		fake = fake

	# Тестирование на ошибочный тип параметра функции
	def test_amount_gas_released_type_args_error(self):
		with pytest.raises(TypeError):
			result = amount_gas_released(self.fake)
			return result

	# Тестирование на меньшое кол-во аргументов
	def test_amount_gas_released_less_args(self):
		with pytest.raises(TypeError):
			result = amount_gas_released()
			return result

	# Тестирование на большее кол-во аргументов
	def test_amount_gas_released_more_args(self):
		with pytest.raises(TypeError):
			result = amount_gas_released(self.mass, self.fake)
			return result


@pytest.mark.rfs
class TestOverpressure:
	""" Тест для overpressure """
	def __init__(quantity=quantity):
		step = quantity

	def test_overpressure(self):
		check = overpressure(self.step)
		h = AVERAGE_MOLAR_MASS * UNIVERSAL_GAS_CONSTANT * BURNING_TEMPERATURE
		result = float(h / self.step)
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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestOverpressureError:
	""" Тест исключений для overpressure """
	def __init__(quantity=quantity, fake=fake):
		step = quantity
		fake = fake

	# Тестирование на ошибочный тип параметра функции
	def test_overpressure_type_args_error(self):
		with pytest.raises(TypeError):
			result = overpressure(self.fake)
			return result

	# Тестирование на меньшое кол-во аргументов
	def test_overpressure_less_args(self):
		with pytest.raises(TypeError):
			result = overpressure()
			return result

	# Тестирование на большее кол-во аргументов
	def test_overpressure_more_args(self):
		with pytest.raises(TypeError):
			result = overpressure(self.step, self.fake)
			return result


@pytest.mark.rfs
class TestThrustForse:
	""" Тест для thrust_force """
	def __init__(container_pressure=container_pressure):
		pressure = container_pressure

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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestThrustForseError:
	""" Тест исключений для thrust_force """
	def __init__(container_pressure=container_pressure, fake=fake):
		pressure = container_pressure
		fake = fake

	# Тестирование на ошибочный тип параметра функции
	def test_thrust_force_type_args_error(self):
		with pytest.raises(TypeError):
			result = thrust_force(self.fake)
			return result

	# Тестирование на меньшое кол-во аргументов
	def test_thrust_force_less_args(self):
		with pytest.raises(TypeError):
			result = thrust_force()
			return result

	# Тестирование на большее кол-во аргументов
	def test_thrust_force_more_args(self):
		with pytest.raises(TypeError):
			result = thrust_force(self.pressure, self.fake)
			return result


@pytest.mark.rfs
class TestImpuls:
	""" Тест для impuls """
	def __init__(container_pressure=container_pressure, time_timer=time_timer):
		pressure = container_pressure
		time = time_timer

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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestImpulsError:
	""" Тест исключений для impuls """
	def __init__(
		container_pressure=container_pressure,
		time_timer=time_timer,
		fake=fake):
		pressure = container_pressure
		time = time_timer
		fake = fake

	# Тестирование на ошибочный 1 тип параметра функции
	def test_impuls_type_to_1_args_error(self):
		with pytest.raises(TypeError):
			result = impuls(self.fake, self.time)
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_impuls_type_to_2_args_error(self):
		with pytest.raises(TypeError):
			result = impuls(self.pressure, self.fake)
			return result

	# Тестирование на меньшое кол-во аргументов
	def test_impuls_less_to_1_args(self):
		with pytest.raises(TypeError):
			result = impuls(self.pressure)
			return result

	# Тестирование на меньшое кол-во аргументов
	def test_impuls_less_to_2_args(self):
		with pytest.raises(TypeError):
			result = impuls(self.time)
			return result

	# Тестирование без аргументов аргументов
	def test_impuls_without_args(self):
		with pytest.raises(TypeError):
			result = impuls()
			return result

	# Тестирование на большее кол-во аргументов
	def test_impuls_more_args(self):
		with pytest.raises(TypeError):
			result = impuls(self.pressure, self.time, self.fake)
			return result


@pytest.mark.rfs
class TestHeightRocket:
	""" Тест для height_rocket """
	def __init__(
		height_begin_place=height_begin_place,
		height_stage_place=height_stage_place,
		stage_rocket=stage_rocket):
		heightStart = height_begin_place
		heightStage = height_stage_place
		stage = stage_rocket

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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestHeightRocketError:
	""" Тест исключений для height_rocket """
	def __init__(
		height_begin_place=height_begin_place,
		height_stage_place=height_stage_place,
		stage_rocket=stage_rocket,
		fake=fake):
		heightStart = height_begin_place
		heightStage = height_stage_place
		stage = stage_rocket
		fake = fake

	# Тестирование на ошибочный 1 тип параметра функции
	def test_height_rocket_type_1_args_error(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.fake,
						self.heightStage,
						self.stage
					)
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_height_rocket_type_2_args_error(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.fake,
						self.stage
					)
			return result

	# Тестирование на ошибочный 3 тип параметра функции
	def test_height_rocket_type_3_args_error(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.heightStage,
						self.fake
					)
			return result

	# Тестирование на меньшое 1 кол-во аргументов
	def test_height_rocket_less_to_1_args(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStage,
						self.stage
					)
			return result

	# Тестирование на меньшое 2 кол-во аргументов
	def test_height_rocket_less_to_2_args(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.stage
					)
			return result

	# Тестирование на меньшое 3 кол-во аргументов
	def test_height_rocket_less_to_3_args(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.heightStage,
					)
			return result

	# Тестирование без аргументов аргументов
	def test_height_rocket_without_args(self):
		with pytest.raises(TypeError):
			result = height_rocket()
			return result

	# Тестирование на большее кол-во аргументов
	def test_height_rocket_more_args(self):
		with pytest.raises(TypeError):
			result = height_rocket(
						self.heightStart,
						self.heightStage,
						self.stage,
						self.fake
					)
			return result


@pytest.mark.rfs
class TestCylindricalCavity:
	"""Тест CylindricalCavity"""
	def __init__(
		burn_fuel_rocket=burn_fuel_rocket,
		burn_step_rocket=burn_step_rocket,
		burn_size_rocket=burn_size_rocket):
		burnFuel = burn_fuel_rocket
		step = burn_step_rocket
		size = burn_size_rocket

	# Тестирвание вычисления функции
	def test_volume_cylindrical_cavity(self):
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		check = CC.volume_cylindrical_cavity()
		R_0 = INITIAL_DISTANCE
		R_n = R_0 + self.step * self.burnFuel
		result = np.pi * float((pow(R_n, 2)) * self.size)
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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestCylindricalCavityError:
	"""Тест CylindricalCavity с ошибкой"""
	def __init__(
		burn_fuel_rocket=burn_fuel_rocket,
		burn_step_rocket=burn_step_rocket,
		burn_size_rocket=burn_size_rocket,
		fake=fake):
		burnFuel = burn_fuel_rocket
		step = burn_step_rocket
		size = burn_size_rocket
		fake = fake

	# Тестирование на ошибочный 1 тип параметра функции
	def test_volume_cylindrical_cavity_type_1_args_error(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.fake, self.step, self.size)
			result = CC.volume_cylindrical_cavity()
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_volume_cylindrical_cavity_type_2_args_error(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.burnFuel, self.fake, self.size)
			result = CC.volume_cylindrical_cavity()
			return result

	# Тестирование на ошибочный 3 тип параметра функции
	def test_volume_cylindrical_cavity_type_3_args_error(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.burnFuel, self.step, self.fake)
			result = CC.volume_cylindrical_cavity()
			return result

	# Тестирование на меньшое 1 кол-во аргументов
	def test_volume_cylindrical_cavity_less_to_1_args(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.step, self.size)
			result = CC.volume_cylindrical_cavity()
			return result

	# Тестирование на меньшое 2 кол-во аргументов
	def test_volume_cylindrical_cavity_less_to_2_args(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.burnFuel, self.size)
			result = CC.volume_cylindrical_cavity()
			return result

	# Тестирование на меньшое 3 кол-во аргументов
	def test_volume_cylindrical_cavity_less_to_3_args(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity(self.burnFuel, self.step)
			result = CC.volume_cylindrical_cavity()
			return result

	# Тестирование без аргументов аргументов
	def test_volume_cylindrical_cavity_without_args(self):
		with pytest.raises(TypeError):
			CC = CylindricalCavity()
			result = CC.volume_cylindrical_cavity()
			return result

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
			return result


@pytest.mark.rfs
class TestResistance:
	""" Тест для Resistance """
	def __init__(
		engine=engine,
		thrust_force_rocket=thrust_force_rocket,
		mass_rocket=mass_rocket):
		speed = engine
		thrust_force = thrust_force_rocket
		mass = mass_rocket

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
		assert result is not None

	def test_aerodynamic_drag(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist.aerodynamic_drag()
		Cx = CROSS_SECTION_AREA
		S = Cx
		Q = resist._aerodynamic_pressure()
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
		assert result is not None

	def test_gravitation_losses(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist.gravitation_losses()
		G = ACCELERATION_FREE_FALL
		angel = np.sin(FPV)
		result = G * angel
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
		assert result is not None

	def test_control_losses(self):
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist.control_losses()
		angel = 1 - np.cos(TVV)
		result = (self.thrust_force / self.mass) * angel
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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestResistanceError:
	""" Тест исключений для Resistance """
	def __init__(
		engine=engine,
		thrust_force_rocket=thrust_force_rocket,
		mass_rocket=mass_rocket,
		fake=fake):
		speed = engine
		thrust_force = thrust_force_rocket
		mass = mass_rocket
		fake = fake

	# Тестирование на ошибочный 1 тип параметра функции
	def test_aerodynamic_pressure_type_1_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.fake, self.thrust_force, self.mass)
			result = resist._aerodynamic_pressure()
			return result

	# Тестирование на меньшое 1 кол-во аргументов
	def test_aerodynamic_pressure_less_to_1_args(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.thrust_force, self.mass)
			result = resist._aerodynamic_pressure()
			return result

	# Тестирование на меньшое 2 кол-во аргументов
	def test_aerodynamic_pressure_less_to_2_args(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.mass)
			result = resist._aerodynamic_pressure()
			return result

	# Тестирование на меньшое 3 кол-во аргументов
	def test_aerodynamic_pressure_less_to_3_args(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.thrust_force)
			result = resist._aerodynamic_pressure()
			return result

	# Тестирование без аргументов аргументов
	def test_aerodynamic_pressure_without_args(self):
		with pytest.raises(TypeError):
			resist = Resistance()
			result = resist._aerodynamic_pressure()
			return result

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
			return result

	# Тестирование на ошибочный 1 тип параметра функции
	def test_aerodynamic_drag_type_1_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.fake, self.thrust_force, self.mass)
			result = resist.aerodynamic_drag()
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_control_losses_type_2_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.fake, self.mass)
			result = resist.control_losses()
			return result

	# Тестирование на ошибочный 3 тип параметра функции
	def test_control_losses_type_3_args_error(self):
		with pytest.raises(TypeError):
			resist = Resistance(self.speed, self.thrust_force, self.fake)
			result = resist.control_losses()
			return result


@pytest.mark.rfs
class TestSpeed:
	"""Тест Speed"""
	def __init__(
		thrust_force_rocket=thrust_force_rocket,
		gravitation_losses_space=gravitation_losses_space,
		mass_rocket=mass_rocket,
		time_timer=time_timer,
		start_speed=start_speed):
		thrust_force = thrust_force_rocket
		gravitation_losses = gravitation_losses_space
		mass = mass_rocket
		time = time_timer
		speed_0 = start_speed

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
		result = thrust_force(self.speed_0) \
			* self.gravitation_losses - self.mass * G
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
		assert result is not None

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
		assert result is not None

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
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestSpeedError:
	"""Тест Speed с ошибкой"""
	def __init__(
		thrust_force_rocket=thrust_force_rocket,
		gravitation_losses_space=gravitation_losses_space,
		mass_rocket=mass_rocket,
		time_timer=time_timer,
		start_speed=start_speed,
		fake=fake):
		thrust_force = thrust_force_rocket
		gravitation_losses = gravitation_losses_space
		mass = mass_rocket
		time = time_timer
		speed_0 = start_speed
		fake = fake

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

	# Тестирование без аргументов аргументов
	def test_resultant_force_without_args(self):
		with pytest.raises(TypeError):
			speed = Speed()
			result = speed._resultant_force()
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result


@pytest.mark.rfs
class TestModelFlight:
	"""Тест ModelFlight"""
	def __init__(
		mass_rocket=mass_rocket,
		start_speed=start_speed,
		time_timer=time_timer,
		fuelFlow=fuelFlow):
		mass = mass_rocket
		speed_0 = start_speed
		time = time_timer
		fuel_flow = fuelFlow

	# Тестирвание вычисления функции
	def test_total_resistance(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		check = round(model._total_resistance())
		speed = model._total_speed()
		resistance = Resistance(speed, thrust_force(self.fuel_flow), self.mass)
		cont = resistance.control_losses()
		gl = resistance.gravitation_losses()
		ad = resistance.aerodynamic_drag()
		result = round(cont + gl + ad)
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
		assert result is not None

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
		assert result is not None

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
		result = elliptical_range(speed)
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
		assert result is not None

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
		assert isinstance(result, (float, int, list))

	def test_model_stack_ist_none(self):
		model = ModelFlight(
			self.mass,
			self.speed_0,
			self.time,
			self.fuel_flow
		)
		result = model.model_stack()
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestModelFlightError:
	"""Тест ModelFlight с ошибкой"""
	def __init__(
		mass_rocket=mass_rocket,
		start_speed=start_speed,
		time_timer=time_timer,
		fuelFlow=fuelFlow,
		fake=fake):
		mass = mass_rocket
		speed_0 = start_speed
		time = time_timer
		fuel_flow = fuelFlow
		fake = fake

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
			return result

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
			return result

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
			return result

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
			return result

	# Тестирование на меньшое 1 кол-во аргументов
	def test_total_resistance_less_to_1_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.speed_0,
				self.time,
				self.fuel_flow
			)
			result = model._total_resistance()
			return result

	# Тестирование на меньшое 2 кол-во аргументов
	def test_total_resistance_less_to_2_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.time,
				self.fuel_flow
			)
			result = model._total_resistance()
			return result

	# Тестирование на меньшое 3 кол-во аргументов
	def test_total_resistance_less_to_3_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.fuel_flow
			)
			result = model._total_resistance()
			return result

	# Тестирование на меньшое 4 кол-во аргументов
	def test_total_resistance_less_to_4_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time
			)
			result = model._total_resistance()
			return result

	# Тестирование без аргументов аргументов
	def test_total_resistance_without_args(self):
		with pytest.raises(TypeError):
			model = ModelFlight()
			result = model._total_resistance()
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result

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
			return result
