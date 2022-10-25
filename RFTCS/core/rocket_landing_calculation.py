"""
Файл для математическое моделирование движения тел
"""
import os
import sys

path = os.path.join(os.getcwd(), '../')
sys.path.append(path)

import numpy as np

from rocket_flight_simulation import resistance_force_env
from rocket_fuel_calculation import total_oil


# Расход топлива
A = 1
# Скорость истечения газов
GFR = 2 / 3
# Ускорение свободного падения
GO = 9.81
# Коэффициент лобового сопротивления
CRFf = 0.14


# Математическая модель движения тел с переменной массой,
# для вертикального взлета
def calculation_rocket_movement(speed: float, resistance: float) -> float:
	m = A * GFR - resistance - speed
	return m


# Горизонтальная составная скорость
def vector_speed(R: float, h: float) -> float:
	h_speed = GO * (R ** 2 / ((R + h) ** 2))
	return h_speed


# Модель для описания полета ракеты
def rocket_flight_description(
							teta: float,
							speed: float,
							mass: float,
							resistance: float,
							vs: float) -> float:
	y = speed * np.sin(teta)
	x = speed * np.cos(teta)
	rocket_speed = (A * GFR - resistance) / mass - (vs * np.sin(teta))
	main_teta = - (vs * (np.cos(teta) / speed))
	return [rocket_speed, main_teta, y, x]


# Масса ракеты
# def rocket_massa():
# 	if m_now <= mk:
# 		m - A * time
# 	else:
# 		m_now = mk
# 	return m_now


def main():
	height = 100.0
	weight = 30.0
	delta_speed = 2500.0
	teta = 87.0
	mass = 524.0
	Isp = 4200.0
	oil_mass = total_oil(Isp, delta_speed, mass)
	# mk = mass - oil_mass

	resistance = resistance_force_env(height, weight, delta_speed)
	crm = calculation_rocket_movement(delta_speed, resistance)
	vs = vector_speed(teta, height)
	rfd = rocket_flight_description(teta, delta_speed, mass, resistance, vs)
	rocket_speed = rfd[0]
	main_teta = rfd[1]
	y = rfd[2]
	x = rfd[3]
	print(
		f"Main rocket speed = {rocket_speed}, simple math model = {crm} \
		teta = {main_teta}, oil mass = {oil_mass} y = {y}, x = {x}")
# Main rocket speed = -447240.143022908,
# teta = -0.0004839147719103341, y = -2054.5445915770565,
# x = 1424.37583566328


if __name__ == "__main__":
	main()
