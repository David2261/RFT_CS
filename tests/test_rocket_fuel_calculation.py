"""
Файл для тестирования расчетов топлива ракеты
"""
import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import numpy as np
import pytest

from rocket_fuel_calculation import TotalOil
from setup.constant import ACCELERATION_FREE_FALL


@pytest.mark.rfc
class TestTotalOil:
	""" Тестирование функций расчета топлива """
	Me = 524
	Mf = 579
	Isp = 4200

	# Функция нахождения натурального логарифма
	def _natural_logarithm_check(self) -> float:
		num = self.Mf / self.Me
		return np.log(num)

	# Функция расчет с помощью Эйлерова числа E
	def _euler(self) -> float:
		G = ACCELERATION_FREE_FALL
		A = TotalOil(self.Me, self.Mf, self.Isp)
		num = A.total_speed()
		return np.exp(num / (self.Isp * G))

	# Тестирвание вычисления функции
	def test_total_speed(self):
		G = ACCELERATION_FREE_FALL
		nl = self._natural_logarithm_check()
		answer = self.Isp * G * nl
		res = TotalOil(self.Me, self.Mf, self.Isp)
		result = res.total_speed()
		assert result == answer

	# Тестирование типа вывода функции
	def test_total_speed_type(self):
		res = TotalOil(self.Me, self.Mf, self.Isp)
		result = res.total_speed()
		assert isinstance(result, (int, float))

	# Тестирование на логическую операцию функции
	def test_total_speed_less(self):
		G = ACCELERATION_FREE_FALL
		nl = self._natural_logarithm_check()
		answer = self.Isp * G * nl
		res = TotalOil(self.Me, self.Mf, self.Isp)
		result = res.total_speed()
		assert result < (answer + 1)

	# Тестирвание вычисления функции
	def test_total_oil(self):
		answer = self.Me * (self._euler() - 1)
		res = TotalOil(self.Me, self.Mf, self.Isp)
		result = res.total_oil()
		assert result == answer

	# Тестирование типа вывода функции
	def test_total_oil_type(self):
		res = TotalOil(self.Me, self.Mf, self.Isp)
		result = res.total_oil()
		assert isinstance(result, (int, float))

	# Тестирование на логическую операцию функции
	def test_total_oil_less(self):
		answer = self.Me * (self._euler() - 1)
		res = TotalOil(self.Me, self.Mf, self.Isp)
		result = res.total_oil()
		assert result < (answer + 1)


@pytest.mark.rfc
@pytest.mark.exception
class TestTotalOilError:
	""" Тестирование исключений функций расчета топлива """
	Me = "false"
	Mf = 579
	Isp = 4200

	# Тестирование на ошибочный тип параметра функции
	def test_total_speed_type_error(self):
		with pytest.raises(TypeError):
			res = TotalOil(self.Me, self.Mf, self.Isp)
			res.total_speed()

	# Тестирование на меньшое кол-во аргументов
	def test_total_speed_less_args(self):
		with pytest.raises(TypeError):
			res = TotalOil(self.Mf, self.Isp)
			res.total_speed()

	# Тестирование на большее кол-во аргументов
	def test_total_speed_more_args(self):
		with pytest.raises(TypeError):
			res = TotalOil(self.Me, self.Mf, self.Isp, 2314)
			res.total_speed()

	# Тестирование на ошибочный тип параметра функции
	def test_total_oil_type_error(self):
		with pytest.raises(TypeError):
			res = TotalOil(self.Me, self.Mf, self.Isp)
			res.total_oil()

	# Тестирование на меньшое кол-во аргументов
	def test_total_oil_less_args(self):
		with pytest.raises(TypeError):
			res = TotalOil(self.Mf, self.Isp)
			res.total_oil()

	# Тестирование на большее кол-во аргументов
	def test_total_oil_more_args(self):
		with pytest.raises(TypeError):
			res = TotalOil(self.Me, self.Mf, self.Isp, 2314)
			res.total_oil()
