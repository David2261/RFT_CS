"""
В данном файле будут производиться расчеты топлива ракеты.
Основные формулы:
	- Сумма всех скоростей [V = l_(sp) * g_(o) * ln(Mf/Me)]
	- Масса конструкции ракеты [Mk = Mp/k]
"""
import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt

from format import main_rocket_format


# Константы
# Ускорение свободного падения
GO = 9.81
# Коэффициент массы конструкции для единицы массы топлива
K = 400


# Функция нахождения натурального логарифма
def natural_logarithm(Mf: float, Me: float) -> float:
	num = Mf / Me
	return np.log(num)


# Функция расчет с помощью Эйлерова числа E
def euler(delta_V: float, Isp: float) -> float:
	return np.exp(delta_V / (Isp * GO))


# Сумма всех скоростей
def total_speed(Isp: float, Mf: float, Me: float):
	natural_log = natural_logarithm(Mf, Me)
	delta_V = Isp * GO * natural_log
	return delta_V


# Функция для расчета топлива
def total_oil(Isp: float, delta_V: float, Me: float) -> float:
	e = euler(delta_V, Isp)
	Mp = Me * (e - 1)
	return Mp


# Функция расчета массы конструкции ракеты
def massa_construction_rocket(Mp: float) -> float:
	Mk = Mp / K
	return Mk


def main(Isp: float, delta_V: float, Me: float) -> float:
	# delta_V = total_speed(Isp, Mf, Me)
	# print(main_rocket_format(delta_V, 1))

	Mp = total_oil(Isp, delta_V, Me)
	return round(Mp, 2)


if __name__ == "__main__":
	res = main(4200.0, 2500.0, 524.0)

	print(main_rocket_format(res, 4))

# Масса спутника 524 кг
# Isp = 4200 с
# Скорость = 2500 м/с
# Масса ксенона = ?
# Сумма всего топлива = 32.77897645413678 кг
