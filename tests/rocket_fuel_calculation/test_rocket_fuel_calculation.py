"""
Файл для тестирования расчетов топлива ракеты
"""
import numpy as np
import pytest

from RFTCS.rocket_fuel_calculation import TotalOil
from RFTCS.setup.constant import ACCELERATION_FREE_FALL
from .data import *


@pytest.mark.rfc
class TestTotalOil:
	""" Тестирование функций расчета топлива """
	Me = 230
	Mf = 430
	Isp = 4200

	# Функция нахождения натурального логарифма
	def test_natural_logarithm(self) -> float:
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		check = fuel._natural_logarithm()
		result = np.log(self.Mf / self.Me)
		assert result == check

	# Функция нахождения натурального логарифма
	def test_natural_logarithm_type(self) -> float:
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._natural_logarithm()
		assert isinstance(result, (int, float))

	def test_natural_logarithm_less(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._natural_logarithm()
		check = result + 1
		assert result < check

	def test_natural_logarithm_more(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._natural_logarithm()
		check = result - 1
		assert result > check

	def test_natural_logarithm_ist_none(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._natural_logarithm()
		assert result is not None

	# Функция расчет с помощью Эйлерова числа E
	def test_euler(self) -> float:
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		check = fuel._euler()
		G = ACCELERATION_FREE_FALL
		speed = fuel.total_speed()
		result = np.exp(speed / (self.Isp * G))
		assert result == check

	# Функция нахождения натурального логарифма
	def test_euler_type(self) -> float:
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._euler()
		assert isinstance(result, (int, float))

	def test_euler_less(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._euler()
		check = result + 1
		assert result < check

	def test_euler_more(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._euler()
		check = result - 1
		assert result > check

	def test_euler_ist_none(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._euler()
		assert result is not None

	def test_total_speed(self) -> float:
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		check = fuel.total_speed()
		G = ACCELERATION_FREE_FALL
		nl = fuel._natural_logarithm()
		result = self.Isp * G * nl
		assert result == check

	# Функция нахождения натурального логарифма
	def test_total_speed_type(self) -> float:
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_speed()
		assert isinstance(result, (int, float))

	def test_total_speed_less(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_speed()
		check = result + 1
		assert result < check

	def test_total_speed_more(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_speed()
		check = result - 1
		assert result > check

	def test_total_speed_ist_none(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_speed()
		assert result is not None

	def test_total_oil(self) -> float:
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		check = fuel.total_oil()
		result = self.Me * (fuel._euler() - 1)
		assert result == check

	# Функция нахождения натурального логарифма
	def test_total_oil_type(self) -> float:
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_oil()
		assert isinstance(result, (int, float))

	def test_total_oil_less(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_oil()
		check = result + 1
		assert result < check

	def test_total_oil_more(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_oil()
		check = result - 1
		assert result > check

	def test_total_oil_ist_none(self):
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_oil()
		assert result is not None


@pytest.mark.rfc
@pytest.mark.exception
class TestTotalOilError:
	""" Тестирование исключений функций расчета топлива """
	Me = 230
	Mf = 430
	Isp = 4200
	fake = 'ake'

	# Тестирование на ошибочный 1 тип параметра функции
	def test_natural_logarithm_type_1_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.fake, self.Mf, self.Isp)
			result = fuel._natural_logarithm()
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_natural_logarithm_type_2_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.fake, self.Isp)
			result = fuel._natural_logarithm()
			return result

	# Тестирование на 1 аргумент
	def test_natural_logarithm_less_to_1_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Mf, self.Isp)
			result = fuel._natural_logarithm()
			return result

	# Тестирование на 2 аргумент
	def test_natural_logarithm_less_to_2_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Isp)
			result = fuel._natural_logarithm()
			return result

	# Тестирование без аргументов
	def test_natural_logarithm_without_args(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Mf)
			result = fuel._natural_logarithm()
			return result

	# Тестирование на большее кол-во аргументов
	def test_natural_logarithm_more_args(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Mf, self.Isp, self.fake)
			result = fuel._natural_logarithm()
			return result

	# Тестирование на ошибочный 1 тип параметра функции
	def test_euler_type_1_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.fake, self.Mf, self.Isp)
			result = fuel._euler()
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_euler_type_2_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.fake, self.Isp)
			result = fuel._euler()
			return result

	# Тестирование на 1 аргумент
	def test_euler_less_to_1_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Mf, self.Isp)
			result = fuel._euler()
			return result

	# Тестирование на 2 аргумент
	def test_euler_less_to_2_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Isp)
			result = fuel._euler()
			return result

	# Тестирование на 3 аргумент
	def test_euler_less_to_3_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Mf)
			result = fuel._euler()
			return result

	# Тестирование на ошибочный 1 тип параметра функции
	def test_total_speed_type_1_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.fake, self.Mf, self.Isp)
			result = fuel.total_speed()
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_total_speed_type_2_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.fake, self.Isp)
			result = fuel.total_speed()
			return result

	# Тестирование на 1 аргумент
	def test_total_speed_less_to_1_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Mf, self.Isp)
			result = fuel.total_speed()
			return result

	# Тестирование на 2 аргумент
	def test_total_speed_less_to_2_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Isp)
			result = fuel.total_speed()
			return result

	# Тестирование на ошибочный 1 тип параметра функции
	def test_total_oil_type_1_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.fake, self.Mf, self.Isp)
			result = fuel.total_oil()
			return result

	# Тестирование на ошибочный 2 тип параметра функции
	def test_total_oil_type_2_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.fake, self.Isp)
			result = fuel.total_oil()
			return result

	# Тестирование на 1 аргумент
	def test_total_oil_less_to_1_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Mf, self.Isp)
			result = fuel.total_oil()
			return result

	# Тестирование на 2 аргумент
	def test_total_oil_less_to_2_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Isp)
			result = fuel.total_oil()
			return result

	# Тестирование на 3 аргумент
	def test_total_oil_less_to_3_args_error(self):
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Mf)
			result = fuel.total_oil()
			return result
