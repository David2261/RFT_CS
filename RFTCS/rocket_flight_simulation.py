"""
Файл для численного моделирования траектории полета ракеты
"""
import numpy as np

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
Cf = 1.2
# Плотность воздуха, кг/м^3
RHO_A = 1.2754
# Коэффициент лобового сопротивления
CRFf = 0.14


# Функция расчета площади
def _body_area(height: float, width: float) -> float:
	total = height * width
	return total


# Функция расчета силы сопротивления
def resistance_force(height: float, width: float) -> float:
	area = _body_area(height, width)
	dealta_V = total_speed(420000.0, 5790000.0, 524.0)
	F = Cf * (RHO * dealta_V**2) / 2 * area
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


# Функция расчета гравитационных потерь
def gravity_losses(gamma: float) -> float:
	Vg = GO * np.cos(gamma)
	return Vg


# Функция Аэродинамические потери
def aerodynamic_losses(A: float, m: float) -> float:
	Va = A / m
	return Va


# Функция потери скорости на управление
def loss_speed_on_control(F: float, m: float, alpha: float) -> float:
	Vu = (F / m) * (1 - np.cos(alpha))
	return Vu


if __name__ == "__main__":
	res = resistance_force_env(100.0, 30.0, 2500.0)
	print(FlightFormat._flight_resistance_force_env(res))

# Натуральный логарифм = 9.310151165228136
# Сила сопротивления = 4.47619780864866e+22 м/с^2
