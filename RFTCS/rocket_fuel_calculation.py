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

# Константы
GO = 9.81
K = 400


def _format_func(num: int) -> str:
	return f"Сумма всех скоростей = {str(num)} км/с"

# Функция нахождения натурального логарифма
def _natural_logarithm(Mf: int, Me: int) -> float:
	num = Mf / Me
	yield log(num)

# Сумма всех скоростей
def total_speed(Isp: int, Mf: int, Me: int):
	natural_log = _natural_logarithm(Mf, Me)
	print(type(natural_log))
	delta_V = Isp * GO * natural_log
	return type(delta_V)



if __name__ == "__main__":
	res = total_speed(280, 579, 524)
	print(res)
