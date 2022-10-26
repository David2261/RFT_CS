#!/usr/bin/env python
"""
В данном файле будут производиться расчеты топлива ракеты.
Основные формулы:
	- Сумма всех скоростей [V = l_(sp) * g_(o) * ln(Mf/Me)]
	- Масса конструкции ракеты [Mk = Mp/k]
"""
import os
import sys

path = os.path.join(os.getcwd(), '../')
sys.path.append(path)

import numpy as np
from setup.constant import ACCELERATION_FREE_FALL


class TotalOil:
	""" Расчет общей скорости """
	def __init__(self, m_empty_rocket, mass_rocket, Isp):
		self.Me = m_empty_rocket
		self.Mf = mass_rocket
		self.Isp = Isp

	@classmethod
	# Функция нахождения натурального логарифма
	def _natural_logarithm(cls) -> float:
		num = Mf / Me
		return np.log(num)

	# Функция расчет с помощью Эйлерова числа E
	def _euler(self) -> float:
		G = ACCELERATION_FREE_FALL
		return np.exp(self.total_speed() / (self.Isp * G))

	# Сумма всех скоростей
	def total_speed(self):
		G = ACCELERATION_FREE_FALL
		delta_V = self.Isp * G * self._natural_logarithm()
		return delta_V

	# Функция для расчета топлива
	def total_oil(self) -> float:
		return self.Me * (self._euler() - 1)


if __name__ == "__main__":
	Me = 524
	Mf = 579
	Isp = 4200
	a = TotalOil(Me, Mf, Isp)
	print(a.total_oil())
	# 55.00000000000005
