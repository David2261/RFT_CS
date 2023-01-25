#!/usr/bin/env python3
"""
В данном файле будут производиться расчеты топлива ракеты.
Основные формулы:
	- Сумма всех скоростей [V = l_(sp) * g_(o) * ln(Mf/Me)]
	- Масса конструкции ракеты [Mk = Mp/k]
"""
import sys
import numpy as np
import logging
import logging.config

from exceptions.exception import (
	invalid_import,
	invalid_kbi,
	invalid_type,
	invalid_zero_division,
	invalid_general
)
from setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")

try:
	from setup.constant import ACCELERATION_FREE_FALL

	log_info.info("Включение импортов 'rocket_fuel_calculation.py'")
except ImportError as e:
	logger.error(invalid_import(e))
	raise ImportError(invalid_import(e))


class TotalOil:
	log_info.info("Запуск класса 'TotalOil'")
	""" Расчет общей скорости """

	def __init__(self, m_empty_rocket, mass_rocket, Isp):
		self.Me = m_empty_rocket
		self.Mf = mass_rocket
		self.Isp = Isp

	# Функция нахождения натурального логарифма
	def _natural_logarithm(self) -> float:
		try:
			num = self.Mf / self.Me
			res = np.log(num)
			log_info.info("Запуск функции '_natural_logarithm'")
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except ZeroDivisionError as zde:
			logger.error(invalid_zero_division(zde))
			raise ZeroDivisionError(invalid_zero_division(zde))
		except (IOError, Exception) as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)
		return res

	# Функция расчет с помощью Эйлерова числа E
	def _euler(self) -> float:
		try:
			G = ACCELERATION_FREE_FALL
			speed = self.total_speed()
			res = np.exp(speed / (self.Isp * G))
			log_info.info("Запуск функции '_euler'")
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except ZeroDivisionError as zde:
			logger.error(invalid_zero_division(zde))
			raise ZeroDivisionError(invalid_zero_division(zde))
		except (IOError, Exception) as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)
		return res

	# Сумма всех скоростей
	def total_speed(self):
		try:
			G = ACCELERATION_FREE_FALL
			nl = self._natural_logarithm()
			delta_V = self.Isp * G * nl
			log_info.info("Запуск функции 'total_speed'")
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except (IOError, Exception) as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)
		return delta_V

	# Функция для расчета топлива
	def total_oil(self) -> float:
		try:
			res = self.Me * (self._euler() - 1)
			log_info.info("Запуск функции 'total_oil'")
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except (IOError, Exception) as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)
		return res


if __name__ == "__main__":
	Me = 524
	Mf = 579
	Isp = 4200
	a = TotalOil(Me, Mf, Isp)
	print(a.total_speed())
	print(a.total_oil())
	# 4108.212250250393
	# 55.00000000000005
