from typing import Any
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

fuelFlow = 670

size = 2

fake = 'fake'

engine = 587

weight_empty_rocket = 581

weight_fuel_rocket = 400

quantity = 3

container_pressure = 1400

time_timer = 300

height_begin_place = 120

height_stage_place = 280

stage_rocket = 3

burn_fuel_rocket = 41187.93

burn_step_rocket = 3

burn_size_rocket = 0.45

thrust_force_rocket = 230

gravitation_losses_space = 0.45

start_speed = 280


@pytest.mark.rfs
class TestDistanceNStep:
	""" Тест для distance_N_step """
	fuelFlow = 670
	size = 2

	def test_distance_n_step(self) -> bool:  # type: ignore[return]
		test = distance_N_step(self.fuelFlow, self.size)
		result = INITIAL_DISTANCE - self.size * self.fuelFlow
		assert test == result

	def test_distance_n_step_type(self) -> bool:  # type: ignore[return]
		result = distance_N_step(self.fuelFlow, self.size)
		assert isinstance(result, (int, float))

	def test_distance_n_step_less(self) -> bool:  # type: ignore[return]
		result = distance_N_step(self.fuelFlow, self.size)
		result_more = result + 1
		assert result < result_more

	def test_distance_n_step_more(self) -> bool:  # type: ignore[return]
		result = distance_N_step(self.fuelFlow, self.size)
		result_more = result - 1
		assert result > result_more

	def test_distance_n_step_ist_none(self) -> bool:  # type: ignore[return]
		result = distance_N_step(self.fuelFlow, self.size)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestDistanceNStepError:
	""" Тест исключений для distance_N_step """
	fuelFlow = 670
	size = 2
	fake = 'fake'

	def test_distance_n_step_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			result = distance_N_step(
					self.fake,  # type: ignore[arg-type]
					self.size)
			return result

	def test_distance_n_step_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			result = distance_N_step(
					self.fuelFlow,
					self.fake)  # type: ignore[call-arg, arg-type]
			return result

	def test_distance_n_step_less_args(self) -> Any:
		""" Тестирование на меньшое кол-во аргументов """
		with pytest.raises(TypeError):
			result = distance_N_step(self.fuelFlow)  # type: ignore[call-arg]
			return result

	def test_distance_n_step_without_args(self) -> Any:
		""" Тестирование без аргументов """
		with pytest.raises(TypeError):
			result = distance_N_step()  # type: ignore[call-arg]
			return result

	def test_distance_n_step_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			result = distance_N_step(
				self.fuelFlow,
				self.size,
				self.fake)  # type: ignore[call-arg]
			return result


@pytest.mark.rfs
class TestTgBeta:
	""" Тест для tg_Beta """
	speed = 587

	def test_tg_beta(self) -> bool:  # type: ignore[return]
		check = tg_Beta(self.speed)
		v = (self.speed * BEGIN_RADIUS_ROCKET) / 398_621
		result = v / (2 * np.sqrt(abs(1 - v)))
		assert result == check

	def test_tg_beta_type(self) -> bool:  # type: ignore[return]
		result = tg_Beta(self.speed)
		assert isinstance(result, (int, float))

	def test_tg_beta_less(self) -> bool:  # type: ignore[return]
		result = tg_Beta(self.speed)
		result_more = result + 1
		assert result < result_more

	def test_tg_beta_more(self) -> bool:  # type: ignore[return]
		result = tg_Beta(self.speed)
		result_more = result - 1
		assert result > result_more

	def test_tg_beta_ist_none(self) -> bool:  # type: ignore[return]
		result = tg_Beta(self.speed)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestTgBetaError:
	""" Тест исключений для tg_Beta """
	speed = 587
	fake = 'fake'

	def test_tg_beta_type_args_error(self) -> Any:
		""" Тестирование на ошибочный тип параметра функции """
		with pytest.raises(TypeError):
			result = tg_Beta(self.fake)  # type: ignore[arg-type]
			return result

	def test_tg_beta_less_args(self) -> Any:
		""" Тестирование на меньшое кол-во аргументов """
		with pytest.raises(TypeError):
			result = tg_Beta()  # type: ignore[call-arg]
			return result

	def test_tg_beta_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			result = tg_Beta(self.speed, self.fake)  # type: ignore[call-arg]
			return result


@pytest.mark.rfs
class TestEllipticalRange:
	""" Тест для elliptical_range """
	speed = 587

	def test_elliptical_range(self) -> bool:  # type: ignore[return]
		check = elliptical_range(self.speed)
		R = EARTH_RADIUS
		Tang = tg_Beta(self.speed)
		result = 2 * R * np.arctan(Tang)
		assert result == check

	def test_elliptical_range_type(self) -> bool:  # type: ignore[return]
		result = elliptical_range(self.speed)
		assert isinstance(result, (int, float))

	def test_elliptical_range_less(self) -> bool:  # type: ignore[return]
		result = elliptical_range(self.speed)
		result_more = result + 1
		assert result < result_more

	def test_elliptical_range_more(self) -> bool:  # type: ignore[return]
		result = elliptical_range(self.speed)
		result_more = result - 1
		assert result > result_more

	def test_elliptical_range_ist_none(self) -> bool:  # type: ignore[return]
		result = elliptical_range(self.speed)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestEllipticalRangeError:
	""" Тест исключений для elliptical_range """
	speed = 587
	fake = 'fake'

	def test_elliptical_range_type_args_error(self) -> Any:
		""" Тестирование на ошибочный тип параметра функции """
		with pytest.raises(TypeError):
			result = elliptical_range(self.fake)  # type: ignore[arg-type]
			return result

	def test_elliptical_range_less_args(self) -> Any:
		""" Тестирование на меньшое кол-во аргументов """
		with pytest.raises(TypeError):
			result = elliptical_range()  # type: ignore[call-arg]
			return result

	def test_elliptical_range_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			result = elliptical_range(self.speed, self.fake)  # type: ignore[call-arg]
			return result


@pytest.mark.rfs
class TestMassRocket:
	""" Тест для mass_rocket """
	emptyRocket = 581
	fuelWidth = 400

	def test_mass_rocket(self) -> bool:  # type: ignore[return]
		check = mass_rocket(self.emptyRocket, self.fuelWidth)
		result = float(self.emptyRocket + self.fuelWidth)
		assert result == check

	def test_mass_rocket_type(self) -> bool:  # type: ignore[return]
		result = mass_rocket(self.emptyRocket, self.fuelWidth)
		assert isinstance(result, (int, float))

	def test_mass_rocket_less(self) -> bool:  # type: ignore[return]
		result = mass_rocket(self.emptyRocket, self.fuelWidth)
		result_more = result + 1
		assert result < result_more

	def test_mass_rocket_more(self) -> bool:  # type: ignore[return]
		result = mass_rocket(self.emptyRocket, self.fuelWidth)
		result_more = result - 1
		assert result > result_more

	def test_mass_rocket_ist_none(self) -> bool:  # type: ignore[return]
		result = mass_rocket(self.emptyRocket, self.fuelWidth)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestMassRocketError:
	""" Тест исключений для mass_rocket """
	emptyRocket = 581
	fuelWidth = 400
	fake = 'fake'

	def test_mass_rocket_1_type_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			result = mass_rocket(self.emptyRocket, self.fake)  # type: ignore[arg-type]
			return result

	def test_mass_rocket_2_type_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			result = mass_rocket(self.fake, self.fuelWidth)  # type: ignore[arg-type]
			return result

	def test_mass_rocket_less_args(self) -> Any:
		""" Тестирование на меньшое кол-во аргументов """
		with pytest.raises(TypeError):
			result = mass_rocket()  # type: ignore[call-arg]
			return result

	def test_mass_rocket_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			result = mass_rocket(
					self.emptyRocket,
					self.fuelWidth,
					self.fake)  # type: ignore[call-arg]
			return result


@pytest.mark.rfs
class TestAmountGasReleased:
	""" Тест для amount_gas_released """
	mass = 581

	def test_amount_gas_released(self) -> bool:  # type: ignore[return]
		check = amount_gas_released(self.mass)
		result = float(self.mass / AVERAGE_MOLAR_MASS)
		assert result == check

	def test_amount_gas_released_type(self) -> bool:  # type: ignore[return]
		result = amount_gas_released(self.mass)
		assert isinstance(result, (int, float))

	def test_amount_gas_released_less(self) -> bool:  # type: ignore[return]
		result = amount_gas_released(self.mass)
		result_more = result + 1
		assert result < result_more

	def test_amount_gas_released_more(self) -> bool:  # type: ignore[return]
		result = amount_gas_released(self.mass)
		result_more = result - 1
		assert result > result_more

	def test_amount_gas_released_ist_none(self) -> bool:  # type: ignore[return]
		result = amount_gas_released(self.mass)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestAmountGasReleasedError:
	""" Тест исключений для amount_gas_released """
	mass = 581
	fake = 'fake'

	def test_amount_gas_released_type_args_error(self) -> Any:
		""" Тестирование на ошибочный тип параметра функции """
		with pytest.raises(TypeError):
			result = amount_gas_released(self.fake)  # type: ignore[arg-type]
			return result

	def test_amount_gas_released_less_args(self) -> Any:
		""" Тестирование на меньшое кол-во аргументов """
		with pytest.raises(TypeError):
			result = amount_gas_released()  # type: ignore[call-arg]
			return result

	def test_amount_gas_released_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			result = amount_gas_released(
					self.mass,
					self.fake)  # type: ignore[call-arg]
			return result


@pytest.mark.rfs
class TestOverpressure:
	""" Тест для overpressure """
	step = 3

	def test_overpressure(self) -> bool:  # type: ignore[return]
		check = overpressure(self.step)
		h = AVERAGE_MOLAR_MASS * UNIVERSAL_GAS_CONSTANT * BURNING_TEMPERATURE
		result = float(h / self.step)
		assert result == check

	def test_overpressure_type(self) -> bool:  # type: ignore[return]
		result = overpressure(self.step)
		assert isinstance(result, (int, float))

	def test_overpressure_less(self) -> bool:  # type: ignore[return]
		result = overpressure(self.step)
		result_more = result + 1
		assert result < result_more

	def test_overpressure_more(self) -> bool:  # type: ignore[return]
		result = overpressure(self.step)
		result_more = result - 1
		assert result > result_more

	def test_overpressure_ist_none(self) -> bool:  # type: ignore[return]
		result = overpressure(self.step)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestOverpressureError:
	""" Тест исключений для overpressure """
	step = 3
	fake = 'fake'

	def test_overpressure_type_args_error(self) -> Any:
		""" Тестирование на ошибочный тип параметра функции """
		with pytest.raises(TypeError):
			result = overpressure(self.fake)  # type: ignore[arg-type]
			return result

	def test_overpressure_less_args(self) -> Any:
		""" Тестирование на меньшое кол-во аргументов """
		with pytest.raises(TypeError):
			result = overpressure()  # type: ignore[call-arg]
			return result

	def test_overpressure_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			result = overpressure(self.step, self.fake)  # type: ignore[call-arg]
			return result


@pytest.mark.rfs
class TestThrustForse:
	""" Тест для thrust_force """
	pressure = 1400

	def test_thrust_force(self) -> bool:  # type: ignore[return]
		check = thrust_force(self.pressure)
		result = self.pressure * CROSS_SECTION_AREA
		assert result == check

	def test_thrust_force_type(self) -> bool:  # type: ignore[return]
		result = thrust_force(self.pressure)
		assert isinstance(result, (int, float))

	def test_thrust_force_less(self) -> bool:  # type: ignore[return]
		result = thrust_force(self.pressure)
		result_more = result + 1
		assert result < result_more

	def test_thrust_force_more(self) -> bool:  # type: ignore[return]
		result = thrust_force(self.pressure)
		result_more = result - 1
		assert result > result_more

	def test_thrust_force_ist_none(self) -> bool:  # type: ignore[return]
		result = thrust_force(self.pressure)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestThrustForseError:
	""" Тест исключений для thrust_force """
	pressure = 1400
	fake = 'fake'

	def test_thrust_force_type_args_error(self) -> Any:
		""" Тестирование на ошибочный тип параметра функции """
		with pytest.raises(ValueError):
			result = thrust_force(self.fake)  # type: ignore[arg-type]
			return result

	def test_thrust_force_less_args(self) -> Any:
		""" Тестирование на меньшое кол-во аргументов """
		with pytest.raises(TypeError):
			result = thrust_force()  # type: ignore[call-arg]
			return result

	def test_thrust_force_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			result = thrust_force(self.pressure, self.fake)  # type: ignore[call-arg]
			return result


@pytest.mark.rfs
class TestImpuls:
	""" Тест для impuls """
	pressure = 1400
	time = 300

	def test_impuls(self) -> bool:  # type: ignore[return]
		check = impuls(self.pressure, self.time)
		tf = thrust_force(self.pressure)
		result = float(tf * self.time)
		assert result == check

	def test_impuls_type(self) -> bool:  # type: ignore[return]
		result = impuls(self.pressure, self.time)
		assert isinstance(result, (int, float))

	def test_impuls_less(self) -> bool:  # type: ignore[return]
		result = impuls(self.pressure, self.time)
		result_more = result + 1
		assert result < result_more

	def test_impuls_more(self) -> bool:  # type: ignore[return]
		result = impuls(self.pressure, self.time)
		result_more = result - 1
		assert result > result_more

	def test_impuls_ist_none(self) -> bool:  # type: ignore[return]
		result = impuls(self.pressure, self.time)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestImpulsError:
	""" Тест исключений для impuls """
	pressure = 1400
	time = 300
	fake = 'fake'

	def test_impuls_type_to_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(ValueError):
			result = impuls(self.fake, self.time)  # type: ignore[arg-type]
			return result

	def test_impuls_type_to_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(ValueError):
			result = impuls(self.pressure, self.fake)  # type: ignore[arg-type]
			return result

	def test_impuls_less_to_1_args(self) -> Any:
		""" Тестирование на меньшое кол-во аргументов """
		with pytest.raises(TypeError):
			result = impuls(self.pressure)  # type: ignore[call-arg]
			return result

	def test_impuls_less_to_2_args(self) -> Any:
		""" Тестирование на меньшое кол-во аргументов """
		with pytest.raises(TypeError):
			result = impuls(self.time)  # type: ignore[call-arg]
			return result

	def test_impuls_without_args(self) -> Any:
		""" Тестирование без аргументов аргументов """
		with pytest.raises(TypeError):
			result = impuls()  # type: ignore[call-arg]
			return result

	def test_impuls_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			result = impuls(
					self.pressure,
					self.time,
					self.fake)  # type: ignore[call-arg]
			return result


@pytest.mark.rfs
class TestHeightRocket:
	""" Тест для height_rocket """
	heightStart = 120
	heightStage = 280
	stage = 3

	def test_height_rocket(self) -> bool:  # type: ignore[return]
		check = height_rocket(
				self.heightStart,
				self.heightStage,
				self.stage)
		result = float(self.heightStart + self.heightStage * self.stage)
		assert result == check

	def test_height_rocket_type(self) -> bool:  # type: ignore[return]
		result = height_rocket(
				self.heightStart,
				self.heightStage,
				self.stage)
		assert isinstance(result, (int, float))

	def test_height_rocket_less(self) -> bool:  # type: ignore[return]
		result = height_rocket(
				self.heightStart,
				self.heightStage,
				self.stage)
		result_more = result + 1
		assert result < result_more

	def test_height_rocket_more(self) -> bool:  # type: ignore[return]
		result = height_rocket(
				self.heightStart,
				self.heightStage,
				self.stage)
		result_more = result - 1
		assert result > result_more

	def test_height_rocket_ist_none(self) -> bool:  # type: ignore[return]
		result = height_rocket(
				self.heightStart,
				self.heightStage,
				self.stage)
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestHeightRocketError:
	""" Тест исключений для height_rocket """
	heightStart = 120
	heightStage = 280
	stage = 3
	fake = 'fake'

	def test_height_rocket_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(ValueError):
			result = height_rocket(
					self.fake,  # type: ignore[arg-type]
					self.heightStage,
					self.stage)
			return result

	def test_height_rocket_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(ValueError):
			result = height_rocket(
					self.heightStart,
					self.fake,  # type: ignore[arg-type]
					self.stage)
			return result

	def test_height_rocket_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(ValueError):
			result = height_rocket(
					self.heightStart,
					self.heightStage,
					self.fake)  # type: ignore[arg-type]
			return result

	def test_height_rocket_less_to_1_args(self) -> Any:
		""" Тестирование на меньшое 1 кол-во аргументов """
		with pytest.raises(TypeError):
			result = height_rocket(
					self.heightStage,
					self.stage)  # type: ignore[call-arg]
			return result

	def test_height_rocket_less_to_2_args(self) -> Any:
		""" Тестирование на меньшое 2 кол-во аргументов """
		with pytest.raises(TypeError):
			result = height_rocket(
					self.heightStart,
					self.stage)  # type: ignore[call-arg]
			return result

	def test_height_rocket_less_to_3_args(self) -> Any:
		""" Тестирование на меньшое 3 кол-во аргументов """
		with pytest.raises(TypeError):
			result = height_rocket(
					self.heightStart,
					self.heightStage)  # type: ignore[call-arg]
			return result

	def test_height_rocket_without_args(self) -> Any:
		""" Тестирование без аргументов аргументов """
		with pytest.raises(TypeError):
			result = height_rocket()  # type: ignore[call-arg]
			return result

	def test_height_rocket_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			result = height_rocket(
					self.heightStart,
					self.heightStage,
					self.stage,
					self.fake)  # type: ignore[call-arg]
			return result


@pytest.mark.rfs
class TestCylindricalCavity:
	"""Тест CylindricalCavity"""
	burnFuel = 41187.93
	step = 3
	size = 0.45

	def test_volume_cylindrical_cavity(self) -> bool:  # type: ignore[return]
		""" Тестирвание вычисления функции """
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		check = CC.volume_cylindrical_cavity()
		R_0 = INITIAL_DISTANCE
		R_n = R_0 + self.step * self.burnFuel
		result = np.pi * float((pow(R_n, 2)) * self.size)
		assert result == check

	def test_volume_cylindrical_cavity_type(  # type: ignore[return]
				self) -> bool:
		""" Тестирование типа вывода функции """
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		result = CC.volume_cylindrical_cavity()
		assert isinstance(result, (float, int))

	def test_volume_cylindrical_cavity_less(  # type: ignore[return]
				self) -> bool:
		""" Тестирование на логическую операцию функции """
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		result = CC.volume_cylindrical_cavity()
		check = result + 1
		assert result < check

	def test_volume_cylindrical_cavity_more(  # type: ignore[return]
				self) -> bool:
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		result = CC.volume_cylindrical_cavity()
		check = result - 1
		assert result > check

	def test_volume_cylindrical_cavity_ist_none(  # type: ignore[return]
				self) -> bool:
		CC = CylindricalCavity(self.burnFuel, self.step, self.size)
		result = CC.volume_cylindrical_cavity()
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestCylindricalCavityError:
	"""Тест CylindricalCavity с ошибкой"""
	burnFuel = 41187.93
	step = 3
	size = 0.45
	fake = 'fake'

	def test_volume_cylindrical_cavity_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			CC = CylindricalCavity(
					self.fake,  # type: ignore[arg-type]
					self.step,
					self.size)
			result = CC.volume_cylindrical_cavity()
			return result

	def test_volume_cylindrical_cavity_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			CC = CylindricalCavity(
					self.burnFuel,
					self.fake,  # type: ignore[arg-type]
					self.size)
			result = CC.volume_cylindrical_cavity()
			return result

	def test_volume_cylindrical_cavity_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(TypeError):
			CC = CylindricalCavity(
					self.burnFuel,
					self.step,
					self.fake)  # type: ignore[call-arg, arg-type]
			result = CC.volume_cylindrical_cavity()
			return result

	def test_volume_cylindrical_cavity_less_to_1_args(self) -> Any:
		""" Тестирование на меньшое 1 кол-во аргументов """
		with pytest.raises(TypeError):
			CC = CylindricalCavity(
					self.step,
					self.size)  # type: ignore[call-arg, arg-type]
			result = CC.volume_cylindrical_cavity()
			return result

	def test_volume_cylindrical_cavity_less_to_2_args(self) -> Any:
		""" Тестирование на меньшое 2 кол-во аргументов """
		with pytest.raises(TypeError):
			CC = CylindricalCavity(
					self.burnFuel,
					self.size)  # type: ignore[call-arg, arg-type]
			result = CC.volume_cylindrical_cavity()
			return result

	def test_volume_cylindrical_cavity_less_to_3_args(self) -> Any:
		""" Тестирование на меньшое 3 кол-во аргументов """
		with pytest.raises(TypeError):
			CC = CylindricalCavity(
					self.burnFuel,
					self.step)  # type: ignore[call-arg]
			result = CC.volume_cylindrical_cavity()
			return result

	def test_volume_cylindrical_cavity_without_args(self) -> Any:
		""" Тестирование без аргументов аргументов """
		with pytest.raises(TypeError):
			CC = CylindricalCavity()  # type: ignore[call-arg]
			result = CC.volume_cylindrical_cavity()
			return result

	def test_volume_cylindrical_cavity_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			CC = CylindricalCavity(
					self.burnFuel,
					self.step,
					self.size,
					self.fake)  # type: ignore[call-arg]
			result = CC.volume_cylindrical_cavity()
			return result


@pytest.mark.rfs
class TestResistance:
	""" Тест для Resistance """
	speed = 587
	thrust_force = 230
	mass = 700

	def test_aerodynamic_pressure(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist._aerodynamic_pressure()
		result = (ATMOSPHERIC_DENSITY * (pow(self.speed, 2))) / 2
		assert result == check

	def test_aerodynamic_pressure_type(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist._aerodynamic_pressure()
		assert isinstance(result, (int, float))

	def test_aerodynamic_pressure_less(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist._aerodynamic_pressure()
		result_more = result + 1
		assert result < result_more

	def test_aerodynamic_pressure_more(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist._aerodynamic_pressure()
		result_more = result - 1
		assert result > result_more

	def test_aerodynamic_pressure_ist_none(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist._aerodynamic_pressure()
		assert result is not None

	def test_aerodynamic_drag(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist.aerodynamic_drag()
		Cx = CROSS_SECTION_AREA
		S = Cx
		Q = resist._aerodynamic_pressure()
		result = Cx * S * Q
		assert result == check

	def test_aerodynamic_drag_type(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.aerodynamic_drag()
		assert isinstance(result, (int, float))

	def test_aerodynamic_drag_less(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.aerodynamic_drag()
		result_more = result + 1
		assert result < result_more

	def test_aerodynamic_drag_more(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.aerodynamic_drag()
		result_more = result - 1
		assert result > result_more

	def test_aerodynamic_drag_ist_none(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.aerodynamic_drag()
		assert result is not None

	def test_gravitation_losses(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist.gravitation_losses()
		G = ACCELERATION_FREE_FALL
		angel = np.sin(FPV)
		result = G * angel
		assert result == check

	def test_gravitation_losses_type(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.gravitation_losses()
		assert isinstance(result, (int, float))

	def test_gravitation_losses_less(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.gravitation_losses()
		result_more = result + 1
		assert result < result_more

	def test_gravitation_losses_more(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.gravitation_losses()
		result_more = result - 1
		assert result > result_more

	def test_gravitation_losses_ist_none(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.gravitation_losses()
		assert result is not None

	def test_control_losses(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		check = resist.control_losses()
		angel = 1 - np.cos(TVV)
		result = (self.thrust_force / self.mass) * angel
		assert result == check

	def test_control_losses_type(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.control_losses()
		assert isinstance(result, (int, float))

	def test_control_losses_less(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.control_losses()
		result_more = result + 1
		assert result < result_more

	def test_control_losses_more(self) -> bool:  # type: ignore[return]
		resist = Resistance(self.speed, self.thrust_force, self.mass)
		result = resist.control_losses()
		result_more = result - 1
		assert result > result_more

	def test_control_losses_ist_none(self) -> bool:  # type: ignore[return]
		resist = Resistance(
				self.speed,
				self.thrust_force,
				self.mass)
		result = resist.control_losses()
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestResistanceError:
	""" Тест исключений для Resistance """
	speed = 587
	thrust_force = 230
	mass = 700
	fake = 'fake'

	def test_aerodynamic_pressure_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			resist = Resistance(
					self.fake,  # type: ignore[arg-type]
					self.thrust_force,
					self.mass)
			result = resist._aerodynamic_pressure()
			return result

	def test_aerodynamic_pressure_less_to_1_args(self) -> Any:
		""" Тестирование на меньшое 1 кол-во аргументов """
		with pytest.raises(TypeError):
			resist = Resistance(  # type: ignore[call-arg]
					self.thrust_force,
					self.mass)
			result = resist._aerodynamic_pressure()
			return result

	def test_aerodynamic_pressure_less_to_2_args(self) -> Any:
		""" Тестирование на меньшое 2 кол-во аргументов """
		with pytest.raises(TypeError):
			resist = Resistance(  # type: ignore[call-arg]
					self.speed,
					self.mass)
			result = resist._aerodynamic_pressure()
			return result

	def test_aerodynamic_pressure_less_to_3_args(self) -> Any:
		""" Тестирование на меньшое 3 кол-во аргументов """
		with pytest.raises(TypeError):
			resist = Resistance(
					self.speed,
					self.thrust_force)  # type: ignore[call-arg]
			result = resist._aerodynamic_pressure()
			return result

	def test_aerodynamic_pressure_without_args(self) -> Any:
		""" Тестирование без аргументов аргументов """
		with pytest.raises(TypeError):
			resist = Resistance()  # type: ignore[call-arg]
			result = resist._aerodynamic_pressure()
			return result

	def test_aerodynamic_pressure_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			resist = Resistance(  # type: ignore[call-arg]
					self.speed,
					self.thrust_force,
					self.mass,
					self.fake)
			result = resist._aerodynamic_pressure()
			return result

	def test_aerodynamic_drag_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			resist = Resistance(
					self.fake,  # type: ignore[arg-type]
					self.thrust_force,
					self.mass)
			result = resist.aerodynamic_drag()
			return result

	def test_control_losses_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			resist = Resistance(
					self.speed,
					self.fake,  # type: ignore[arg-type]
					self.mass)
			result = resist.control_losses()
			return result

	def test_control_losses_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(TypeError):
			resist = Resistance(
					self.speed,
					self.thrust_force,
					self.fake)  # type: ignore[arg-type]
			result = resist.control_losses()
			return result


@pytest.mark.rfs
class TestSpeed:
	"""Тест Speed"""
	thrust_force = 230
	gravitation_losses = 0.45
	mass = 700
	time = 300,
	speed_0 = 280

	def test_resultant_force(self) -> bool:  # type: ignore[return]
		""" Тестирвание вычисления функции """
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		check = speed._resultant_force()
		G = ACCELERATION_FREE_FALL
		result = thrust_force(self.speed_0) \
			* self.gravitation_losses - self.mass * G
		assert result == check

	def test_resultant_force_type(self) -> bool:  # type: ignore[return]
		""" Тестирование типа вывода функции """
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		result = speed._resultant_force()
		assert isinstance(result, (float, int))

	def test_resultant_force_less(self) -> bool:  # type: ignore[return]
		""" Тестирование на логическую операцию функции """
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		result = speed._resultant_force()
		check = result + 1
		assert result < check

	def test_resultant_force_more(self) -> bool:  # type: ignore[return]
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		result = speed._resultant_force()
		check = result - 1
		assert result > check

	def test_resultant_force_ist_none(self) -> bool:  # type: ignore[return]
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		result = speed._resultant_force()
		assert result is not None

	# Тестирвание вычисления функции
	def test_rocket_acceleration(self) -> bool:  # type: ignore[return]
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		check = speed.rocket_acceleration()
		F = speed._resultant_force()
		result = F / self.mass
		assert result == check

	# Тестирование типа вывода функции
	def test_rocket_acceleration_type(self) -> bool:  # type: ignore[return]
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		result = speed.rocket_acceleration()
		assert isinstance(result, (float, int))

	# Тестирование на логическую операцию функции
	def test_rocket_acceleration_less(self) -> bool:  # type: ignore[return]
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		result = speed.rocket_acceleration()
		check = result + 1
		assert result < check

	def test_rocket_acceleration_more(self) -> bool:  # type: ignore[return]
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		result = speed.rocket_acceleration()
		check = result - 1
		assert result > check

	def test_rocket_acceleration_ist_none(self) -> bool:  # type: ignore[return]
		speed = Speed(
				self.thrust_force,
				self.gravitation_losses,
				self.mass,
				self.time,
				self.speed_0)
		result = speed.rocket_acceleration()
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestSpeedError:
	"""Тест Speed с ошибкой"""
	thrust_force = 230
	gravitation_losses = 0.45
	mass = 700
	time = 300,
	speed_0 = 280
	fake = 'fake'

	def test_resultant_force_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			speed = Speed(  # type: ignore[call-arg]
					self.thrust_force,
					self.fake,
					self.mass,
					self.time,
					self.speed_0)
			result = speed._resultant_force()
			return result

	def test_resultant_force_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(TypeError):
			speed = Speed(
					self.thrust_force,
					self.gravitation_losses,
					self.fake,
					self.time,
					self.speed_0)
			result = speed._resultant_force()
			return result

	def test_resultant_force_type_5_args_error(self) -> Any:
		""" Тестирование на ошибочный 5 тип параметра функции """
		with pytest.raises(ValueError):
			speed = Speed(
					self.thrust_force,
					self.gravitation_losses,
					self.mass,
					self.time,
					self.fake)
			result = speed._resultant_force()
			return result

	def test_resultant_force_less_to_1_args(self) -> Any:
		""" Тестирование на меньшое 1 кол-во аргументов """
		with pytest.raises(TypeError):
			speed = Speed(  # type: ignore[call-arg]
					self.gravitation_losses,
					self.mass,
					self.time,
					self.speed_0)
			result = speed._resultant_force()
			return result

	def test_resultant_force_less_to_2_args(self) -> Any:
		""" Тестирование на меньшое 2 кол-во аргументов """
		with pytest.raises(TypeError):
			speed = Speed(  # type: ignore[call-arg]
					self.thrust_force,
					self.mass,
					self.time,
					self.speed_0)
			result = speed._resultant_force()
			return result

	def test_resultant_force_less_to_3_args(self) -> Any:
		""" Тестирование на меньшое 3 кол-во аргументов """
		with pytest.raises(TypeError):
			speed = Speed(  # type: ignore[call-arg]
					self.thrust_force,
					self.gravitation_losses,
					self.time,
					self.speed_0)
			result = speed._resultant_force()
			return result

	def test_resultant_force_less_to_4_args(self) -> Any:
		""" Тестирование на меньшое 4 кол-во аргументов """
		with pytest.raises(TypeError):
			speed = Speed(  # type: ignore[call-arg]
					self.thrust_force,
					self.gravitation_losses,
					self.mass,
					self.speed_0)
			result = speed._resultant_force()
			return result

	def test_resultant_force_less_to_5_args(self) -> Any:
		""" Тестирование на меньшое 5 кол-во аргументов """
		with pytest.raises(TypeError):
			speed = Speed(  # type: ignore[call-arg]
					self.thrust_force,
					self.gravitation_losses,
					self.mass,
					self.time)
			result = speed._resultant_force()
			return result

	def test_resultant_force_without_args(self) -> Any:
		""" Тестирование без аргументов аргументов """
		with pytest.raises(TypeError):
			speed = Speed()  # type: ignore[call-arg]
			result = speed._resultant_force()
			return result

	def test_resultant_force_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			speed = Speed(  # type: ignore[call-arg]
					self.thrust_force,
					self.gravitation_losses,
					self.mass,
					self.time,
					self.speed_0,
					self.fake)
			result = speed._resultant_force()
			return result

	def test_rocket_acceleration_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			speed = Speed(
					self.thrust_force,
					self.fake,
					self.mass,
					self.time,
					self.speed_0)
			result = speed.rocket_acceleration()
			return result

	def test_rocket_acceleration_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(TypeError):
			speed = Speed(
					self.thrust_force,
					self.gravitation_losses,
					self.fake,
					self.time,
					self.speed_0)
			result = speed.rocket_acceleration()
			return result

	def test_rocket_acceleration_type_5_args_error(self) -> Any:
		""" Тестирование на ошибочный 5 тип параметра функции """
		with pytest.raises(ValueError):
			speed = Speed(
					self.thrust_force,
					self.gravitation_losses,
					self.mass,
					self.time,
					self.fake)
			result = speed.rocket_acceleration()
			return result

	def test_rocket_speed_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			speed = Speed(
					self.thrust_force,
					self.fake,
					self.mass,
					self.time,
					self.speed_0)
			result = speed.rocket_speed()
			return result

	def test_rocket_speed_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(TypeError):
			speed = Speed(
					self.thrust_force,
					self.gravitation_losses,
					self.fake,
					self.time,
					self.speed_0)
			result = speed.rocket_speed()
			return result

	def test_rocket_speed_type_4_args_error(self) -> Any:
		""" Тестирование на ошибочный 4 тип параметра функции """
		with pytest.raises(TypeError):
			speed = Speed(
					self.thrust_force,
					self.gravitation_losses,
					self.mass,
					self.fake,
					self.speed_0)
			result = speed.rocket_speed()
			return result

	def test_rocket_speed_type_5_args_error(self) -> Any:
		""" Тестирование на ошибочный 5 тип параметра функции """
		with pytest.raises(ValueError):
			speed = Speed(
					self.thrust_force,
					self.gravitation_losses,
					self.mass,
					self.time,
					self.fake)
			result = speed.rocket_speed()
			return result


@pytest.mark.rfs
class TestModelFlight:
	"""Тест ModelFlight"""
	mass = 700
	speed_0 = 280
	time = 300
	fuel_flow = 670

	def test_total_resistance(self) -> bool:  # type: ignore[return]
		""" Тестирвание вычисления функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		check = round(model._total_resistance())
		speed = model._total_speed()
		resistance = Resistance(speed, int(thrust_force(self.fuel_flow)), self.mass)
		cont = resistance.control_losses()
		gl = resistance.gravitation_losses()
		ad = resistance.aerodynamic_drag()
		result = round(cont + gl + ad)
		assert result == check

	def test_total_resistance_type(self) -> bool:  # type: ignore[return]
		""" Тестирование типа вывода функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_resistance()
		assert isinstance(result, (float, int))

	def test_total_resistance_less(self) -> bool:  # type: ignore[return]
		""" Тестирование на логическую операцию функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_resistance()
		check = result + 1
		assert result < check

	def test_total_resistance_more(self) -> bool:  # type: ignore[return]
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_resistance()
		check = result - 1
		assert result > check

	def test_total_resistance_ist_none(self) -> bool:  # type: ignore[return]
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_resistance()
		assert result is not None

	def test_total_speed_type(self) -> bool:  # type: ignore[return]
		""" Тестирование типа вывода функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_speed()
		assert isinstance(result, (float, int))

	def test_total_speed_less(self) -> bool:  # type: ignore[return]
		""" Тестирование на логическую операцию функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_speed()
		check = result + 1
		assert result < check

	def test_total_speed_more(self) -> bool:  # type: ignore[return]
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_speed()
		check = result - 1
		assert result > check

	def test_total_speed_ist_none(self) -> bool:  # type: ignore[return]
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_speed()
		assert result is not None

	def test_total_distance(self) -> bool:  # type: ignore[return]
		""" Тестирвание вычисления функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		check = model._total_distance()
		speed = model._total_speed()
		result = elliptical_range(speed)
		assert result == check

	def test_total_distance_type(self) -> bool:  # type: ignore[return]
		""" Тестирование типа вывода функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_distance()
		assert isinstance(result, (float, int))

	def test_total_distance_less(self) -> bool:  # type: ignore[return]
		""" Тестирование на логическую операцию функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_distance()
		check = result + 1
		assert result < check

	def test_total_distance_more(self) -> bool:  # type: ignore[return]
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_distance()
		check = result - 1
		assert result > check

	def test_total_distance_ist_none(self) -> bool:  # type: ignore[return]
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model._total_distance()
		assert result is not None

	def test_model_stack(self) -> bool:  # type: ignore[return]
		""" Тестирвание вычисления функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		check = model.model_stack()
		resistance = model._total_resistance()
		speed = model._total_speed()
		distance = model._total_distance()
		Beta = tg_Beta(speed)
		result = [resistance, speed, distance, Beta]
		assert result == check

	def test_model_stack_type(self) -> bool:  # type: ignore[return]
		""" Тестирование типа вывода функции """
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model.model_stack()
		assert isinstance(result, (float, int, list))

	def test_model_stack_ist_none(self) -> bool:  # type: ignore[return]
		model = ModelFlight(
				self.mass,
				self.speed_0,
				self.time,
				self.fuel_flow)
		result = model.model_stack()
		assert result is not None


@pytest.mark.rfs
@pytest.mark.exception
class TestModelFlightError:
	"""Тест ModelFlight с ошибкой"""
	mass = 700
	speed_0 = 280
	time = 300
	fuel_flow = 670
	fake = 'fake'

	def test_total_resistance_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.fake,  # type: ignore[arg-type]
					self.speed_0,
					self.time,
					self.fuel_flow)
			result = model._total_resistance()
			return result

	def test_total_resistance_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.fake,  # type: ignore[arg-type]
					self.time,
					self.fuel_flow)
			result = model._total_resistance()
			return result

	def test_total_resistance_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.speed_0,
					self.fake,  # type: ignore[arg-type]
					self.fuel_flow)
			result = model._total_resistance()
			return result

	def test_total_resistance_type_4_args_error(self) -> Any:
		""" Тестирование на ошибочный 4 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.speed_0,
					self.time,
					self.fake)  # type: ignore[arg-type]
			result = model._total_resistance()
			return result

	def test_total_resistance_less_to_1_args(self) -> Any:
		""" Тестирование на меньшое 1 кол-во аргументов """
		with pytest.raises(TypeError):
			model = ModelFlight(  # type: ignore[call-arg]
					self.speed_0,
					self.time,
					self.fuel_flow)
			result = model._total_resistance()
			return result

	def test_total_resistance_less_to_2_args(self) -> Any:
		""" Тестирование на меньшое 2 кол-во аргументов """
		with pytest.raises(TypeError):
			model = ModelFlight(  # type: ignore[call-arg]
					self.mass,
					self.time,
					self.fuel_flow)
			result = model._total_resistance()
			return result

	def test_total_resistance_less_to_3_args(self) -> Any:
		""" Тестирование на меньшое 3 кол-во аргументов """
		with pytest.raises(TypeError):
			model = ModelFlight(  # type: ignore[call-arg]
					self.mass,
					self.speed_0,
					self.fuel_flow)
			result = model._total_resistance()
			return result

	def test_total_resistance_less_to_4_args(self) -> Any:
		""" Тестирование на меньшое 4 кол-во аргументов """
		with pytest.raises(TypeError):
			model = ModelFlight(  # type: ignore[call-arg]
					self.mass,
					self.speed_0,
					self.time)
			result = model._total_resistance()
			return result

	def test_total_resistance_without_args(self) -> Any:
		""" Тестирование без аргументов аргументов """
		with pytest.raises(TypeError):
			model = ModelFlight()  # type: ignore[call-arg]
			result = model._total_resistance()
			return result

	def test_total_resistance_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			model = ModelFlight(  # type: ignore[call-arg]
					self.mass,
					self.speed_0,
					self.time,
					self.fuel_flow,
					self.fake)  # type: ignore[arg-type]
			result = model._total_resistance()
			return result

	def test_total_speed_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.fake,  # type: ignore[arg-type]
					self.speed_0,
					self.time,
					self.fuel_flow)
			result = model._total_speed()
			return result

	def test_total_speed_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.fake,  # type: ignore[arg-type]
					self.time,
					self.fuel_flow)
			result = model._total_speed()
			return result

	def test_total_speed_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.speed_0,
					self.fake,  # type: ignore[arg-type]
					self.fuel_flow)
			result = model._total_speed()
			return result

	def test_total_speed_type_4_args_error(self) -> Any:
		""" Тестирование на ошибочный 4 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.speed_0,
					self.time,
					self.fake)  # type: ignore[arg-type]
			result = model._total_speed()
			return result

	def test_total_distance_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.fake,  # type: ignore[arg-type]
					self.speed_0,
					self.time,
					self.fuel_flow)
			result = model._total_distance()
			return result

	def test_total_distance_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.fake,  # type: ignore[arg-type]
					self.time,
					self.fuel_flow)
			result = model._total_distance()
			return result

	def test_total_distance_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.speed_0,
					self.fake,  # type: ignore[arg-type]
					self.fuel_flow)
			result = model._total_distance()
			return result

	def test_total_distance_type_4_args_error(self) -> Any:
		""" Тестирование на ошибочный 4 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.speed_0,
					self.time,
					self.fake)  # type: ignore[arg-type]
			result = model._total_distance()
			return result

	def test_model_stack_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.fake,  # type: ignore[arg-type]
					self.speed_0,
					self.time,
					self.fuel_flow)
			result = model.model_stack()
			return result

	def test_model_stack_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.fake,  # type: ignore[arg-type]
					self.time,
					self.fuel_flow)
			result = model.model_stack()
			return result

	def test_model_stack_type_3_args_error(self) -> Any:
		""" Тестирование на ошибочный 3 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.speed_0,
					self.fake,  # type: ignore[arg-type]
					self.fuel_flow)
			result = model.model_stack()
			return result

	def test_model_stack_type_4_args_error(self) -> Any:
		""" Тестирование на ошибочный 4 тип параметра функции """
		with pytest.raises(TypeError):
			model = ModelFlight(
					self.mass,
					self.speed_0,
					self.time,
					self.fake)  # type: ignore[arg-type]
			result = model.model_stack()
			return result
