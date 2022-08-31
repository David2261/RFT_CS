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



# Функция расчета площади
def _body_area(height: float, width: float) -> float:
	total = height * width
	return total


def resistance_force(height: float, width: float) -> float:
	area = _body_area(height, width)
	dealta_V = total_speed(420000.0, 5790000.0, 524.0)
	F = Cf * (RHO * dealta_V**2) / 2 * area
	return F


if __name__ == "__main__":
	res = resistance_force(100.0, 30.0)
	print(FlightFormat._flight_resistance_force(res))

# Натуральный логарифм = 9.310151165228136
# Сила сопротивления = 4.47619780864866e+22 м/с^2