#!/usr/bin/env python3.11
"""
Файл для тестирования расчетов топлива ракеты
"""
from __future__ import annotations
from typing import Any
import numpy as np
import pytest

from RFTCS.rocket_fuel_calculation import TotalOil
from RFTCS.setup.constant import ACCELERATION_FREE_FALL


@pytest.mark.rfc
class TestTotalOil:
	""" Тестирование функций расчета топлива """
	Me = 230
	Mf = 430
	Isp = 4200

	def test_natural_logarithm(self) -> bool:  # type: ignore[return]
		""" Функция нахождения натурального логарифма """
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		check = fuel._natural_logarithm()
		result = np.log(self.Mf / self.Me)
		assert result == check

	def test_natural_logarithm_type(self) -> bool:  # type: ignore[return]
		""" Функция нахождения натурального логарифма """
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._natural_logarithm()
		assert isinstance(result, (int, float))

	def test_natural_logarithm_less(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._natural_logarithm()
		check = result + 1
		assert result < check

	def test_natural_logarithm_more(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._natural_logarithm()
		check = result - 1
		assert result > check

	def test_natural_logarithm_ist_none(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._natural_logarithm()
		assert result is not None

	def test_euler(self) -> bool:  # type: ignore[return]
		""" Функция расчет с помощью Эйлерова числа E """
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		check = fuel._euler()
		G = ACCELERATION_FREE_FALL
		speed = fuel.total_speed()
		result = np.exp(speed / (self.Isp * G))
		assert result == check

	def test_euler_type(self) -> bool:  # type: ignore[return]
		""" Функция нахождения типа с помощью Эйлерова числа E """
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._euler()
		assert isinstance(result, (int, float))

	def test_euler_less(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._euler()
		check = result + 1
		assert result < check

	def test_euler_more(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._euler()
		check = result - 1
		assert result > check

	def test_euler_ist_none(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel._euler()
		assert result is not None

	def test_total_speed(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		check = fuel.total_speed()
		G = ACCELERATION_FREE_FALL
		nl = fuel._natural_logarithm()
		result = self.Isp * G * nl
		assert result == check

	def test_total_speed_type(self) -> bool:  # type: ignore[return]
		""" Функция нахождения суммы всех скоростей """
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_speed()
		assert isinstance(result, (int, float))

	def test_total_speed_less(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_speed()
		check = result + 1
		assert result < check

	def test_total_speed_more(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_speed()
		check = result - 1
		assert result > check

	def test_total_speed_ist_none(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_speed()
		assert result is not None

	def test_total_oil(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		check = fuel.total_oil()
		result = self.Me * (fuel._euler() - 1)
		assert result == check

	def test_total_oil_type(self) -> bool:  # type: ignore[return]
		""" Функция для расчета топлива """
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_oil()
		assert isinstance(result, (int, float))

	def test_total_oil_less(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_oil()
		check = result + 1
		assert result < check

	def test_total_oil_more(self) -> bool:  # type: ignore[return]
		fuel = TotalOil(self.Me, self.Mf, self.Isp)
		result = fuel.total_oil()
		check = result - 1
		assert result > check

	def test_total_oil_ist_none(self) -> bool:  # type: ignore[return]
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
	fake = 'fake'

	def test_natural_logarithm_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.fake, self.Mf, self.Isp)
			result = fuel._natural_logarithm()
			return result

	def test_natural_logarithm_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.fake, self.Isp)
			result = fuel._natural_logarithm()
			return result

	def test_natural_logarithm_less_to_1_args_error(self) -> Any:
		""" Тестирование на 1 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(None, self.Mf, self.Isp)
			result = fuel._natural_logarithm()
			return result

	def test_natural_logarithm_less_to_2_args_error(self) -> Any:
		""" Тестирование на 2 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, None, self.Isp)
			result = fuel._natural_logarithm()
			return result

	def test_natural_logarithm_without_args(self) -> Any:
		""" Тестирование без аргументов """
		with pytest.raises(TypeError):
			fuel = TotalOil(None, self.Me, self.Mf)
			result = fuel._natural_logarithm()
			return result

	def test_natural_logarithm_more_args(self) -> Any:
		""" Тестирование на большее кол-во аргументов """
		with pytest.raises(TypeError):
			fuel = TotalOil(
				self.Me,
				self.Mf,
				self.Isp,
				None)  # type: ignore[call-arg]
			result = fuel._natural_logarithm()
			return result

	def test_euler_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.fake, self.Mf, self.Isp)
			result = fuel._euler()
			return result

	def test_euler_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.fake, self.Isp)
			result = fuel._euler()
			return result

	def test_euler_less_to_1_args_error(self) -> Any:
		""" Тестирование на 1 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(None, self.Mf, self.Isp)
			result = fuel._euler()
			return result

	def test_euler_less_to_2_args_error(self) -> Any:
		""" Тестирование на 2 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, None, self.Isp)
			result = fuel._euler()
			return result

	def test_euler_less_to_3_args_error(self) -> Any:
		""" Тестирование на 3 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Mf, None)
			result = fuel._euler()
			return result

	def test_total_speed_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.fake, self.Mf, self.Isp)
			result = fuel.total_speed()
			return result

	def test_total_speed_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.fake, self.Isp)
			result = fuel.total_speed()
			return result

	def test_total_speed_less_to_1_args_error(self) -> Any:
		""" Тестирование на 1 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(None, self.Mf, self.Isp)
			result = fuel.total_speed()
			return result

	def test_total_speed_less_to_2_args_error(self) -> Any:
		""" Тестирование на 2 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, None, self.Isp)
			result = fuel.total_speed()
			return result

	def test_total_oil_type_1_args_error(self) -> Any:
		""" Тестирование на ошибочный 1 тип параметра функции """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.fake, self.Mf, self.Isp)
			result = fuel.total_oil()
			return result

	def test_total_oil_type_2_args_error(self) -> Any:
		""" Тестирование на ошибочный 2 тип параметра функции """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.fake, self.Isp)
			result = fuel.total_oil()
			return result

	def test_total_oil_less_to_1_args_error(self) -> Any:
		""" Тестирование на 1 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(None, self.Mf, self.Isp)
			result = fuel.total_oil()
			return result

	def test_total_oil_less_to_2_args_error(self) -> Any:
		""" Тестирование на 2 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, None, self.Isp)
			result = fuel.total_oil()
			return result

	def test_total_oil_less_to_3_args_error(self) -> Any:
		""" Тестирование на 3 аргумент """
		with pytest.raises(TypeError):
			fuel = TotalOil(self.Me, self.Mf, None)
			result = fuel.total_oil()
			return result
