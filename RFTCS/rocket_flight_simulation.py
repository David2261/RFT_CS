"""
Файл для численного моделирования траектории полета ракеты
"""
import numpy as np
from scipy import integrate

from rocket_fuel_calculation import total_speed
from format import FlightFormat

# молярная масса, кг/моль
MM = 0.029
# Температура, K
T = 300
# Ускорение свободного падения
GO = 9.81
# Ро - плотность
RHO = 16900
# Коэфициент формы
Cf = 0.2
# Плотность воздуха, кг/м^3
RHO_A = 1.2754
# Коэффициент лобового сопротивления
CRFf = 0.14


# Функция расчета площади
def _body_area(height: float, width: float) -> float:
	total = height * width
	return total


# Функция расчета силы сопротивления
def resistance_force(speed: float, area: float) -> float:
	#area = _body_area(height, width)
	dealta_V = speed
	F = Cf * area * dealta_V**2 * RHO_A / 2
	return F


# Функция расчета лобовой площади
def frontal_area(w: float, h: float) -> float:
	return CRFf * w * h


# k - Сопротивление среды
def environmental_resistance(rocket_form: float) -> float:
	er = 0.5 * RHO_A * CRFf * rocket_form
	return er


# Функция расчета сопротивления среды
def resistance_force_env(h: float, w: float, speed: float) -> float:
	Mrf = environmental_resistance(frontal_area(w, h)) * (speed ** 2)
	return Mrf


# Дополнение к функции расчета гравитационных потерь
def addition_gl(time: float, gamma: float, F) -> float:
	Vg = F * np.cos(gamma)
	return Vg


# Функция расчета гравитационных потерь
def gravity_losses(F: float, gamma: float, time: float) -> float:
	res = integrate.quad(addition_gl, 0, time, args=(gamma, F))
	return res[1]


# Дополнение к функции Аэродинамические потери
def addition_al(time, A: float, m: float) -> float:
	Va = (A * time) / (m * time)
	return Va


# Функция Аэродинамические потери
def aerodynamic_losses(A: float, m: float, time: float) -> float:
	res = integrate.quad(addition_al, 0, time, args=(A, m))
	return res[0]


# Дополнение к функции потери скорости на управление
def addition_lsc(
		time,
		F: float,
		mass: float,
		Alpha: float) -> float:
	Vu = ((F * time) / (mass * time)) * \
		(1 - np.cos(Alpha * time))
	return Vu


# Функция потери скорости на управление
def loss_speed_on_control(
		F: float,
		mass: float,
		Alpha: float,
		time: float) -> float:
	res = integrate.quad(
		addition_lsc,
		0,
		time,
		args=(F, mass, Alpha))
	return res[0]


if __name__ == "__main__":
	res = gravity_losses(2080.0, 1.2, 900)
	print(FlightFormat._flight_resistance_force(res))

# Натуральный логарифм = 9.310151165228136
# Сила сопротивления = 4.47619780864866e+22 м/с^2
