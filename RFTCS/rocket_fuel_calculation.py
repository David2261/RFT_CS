"""
В данном файле будут производиться расчеты топлива ракеты.
Основные формулы:
	- Сумма всех скоростей [V = l_(sp) * g_(o) * ln(Mf/Me)]
	- Масса конструкции ракеты [Mk = Mp/k]
	- 
"""
from typing import NamedTuple
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from format import RocketFormat


# Константы
# Ускорение свободного падения
GO = 9.81
# Коэффициент массы конструкции для единицы массы топлива
K = 400


# Функция нахождения натурального логарифма
def _natural_logarithm(Mf: float, Me: float) -> float:
	num = Mf / Me
	return np.log(num)

# Сумма всех скоростей
def total_speed(Isp: float, Mf: float, Me: float):
	natural_log = _natural_logarithm(Mf, Me)
	print(RocketFormat._rocket_natural_logarithm(natural_log))

	delta_V = Isp * GO * natural_log
	return delta_V


def _euler(delta_V: float, Isp: float) -> float:
	return np.exp(delta_V/(Isp*GO))


# Функция для расчета топлива
def total_oil(Isp: float, delta_V: float, Me: float) -> float:
	e = _euler(delta_V, Isp)
	Mp = Me * (e - 1)
	return Mp


# Функция расчета массы конструкции ракеты
def massa_construction_rocket(Mp: float) -> float:
	Mk = Mp / K
	return Mk


def main(Isp: float, Mf: float, Me: float) -> float:
	delta_V = total_speed(Isp, Mf, Me)
	print(RocketFormat._rocket_total_speed(delta_V))

	Mp = total_oil(Isp, delta_V, Me)
	Mk = massa_construction_rocket(Mp)
	return Mk


if __name__ == "__main__":
	res = main(420000.0, 5790000.0, 524.0)

	print(RocketFormat._rocket_total_oil(res))
# Для: 4200.0, 579.0, 524.0
# Сумма всех скоростей = 4112.404303566974 км/с
# Сумма массы = 55.0
# Масса топлива ракеты = 0.13750000000000012

# Для: 420000.0, 5790000.0, 524.0
# Масса топлива ракеты = 14473.690000000008
