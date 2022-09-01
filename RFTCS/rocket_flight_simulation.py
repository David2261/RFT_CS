"""
Файл для численного моделирования траектории полета ракеты
"""
from rocket_fuel_calculation import total_speed
from format import FlightFormat

# плотность воздуха, кг/м^3
AD = 1
# молярная масса, кг/моль
MM = 0.029
# температура, K
T = 300
# Ускорение свободного падения
GO = 9.81
# Ро - плотность
RHO = 16900
# Коэфициент формы
Cf = 1.2
# Плотность воздуха, кг/м^3
RHO_A = 1.27
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

# Функция расчета сопротивления среды
def resistance_force_env(h: float, w: float, delta_V: float) -> float:
	Mrf = 0.5 * CRFf * RHO_A * (delta_V**2) * frontal_area(w, h)
	return Mrf


# Функция расчета гравитационных потерь
def gravity_losses(gamma: float) -> float:
	Vg = GO * cos(gamma)
	return Vg

# Функция Аэродинамические потери
def aerodynamic_loses(A: float, m: float) -> float:
	Va = A / m
	return Va

# Функция потери скорости на управление
def loss_speed_on_control(F: float, m: float, alpha: float) -> float:
	Vu = (F / m) * (1 - cos(alpha))
	return Vu


if __name__ == "__main__":
	res = resistance_force_env(100.0, 30.0, 2500.0)
	print(FlightFormat._flight_resistance_force_env(res))

# Натуральный логарифм = 9.310151165228136
# Сила сопротивления = 4.47619780864866e+22 м/с^2