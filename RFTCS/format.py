"""
В этом файле собраны все способы форматирования результатов
"""


class RocketFormat:
	def _rocket_total_speed(num: float) -> str:
		return f"Сумма всех скоростей = {str(num)} м/с"

	def _rocket_natural_logarithm(num: float) -> str:
		return f"Натуральный логарифм = {str(num)}"

	def _rocket_massa_construction(num: float) -> str:
		return f"Сумма всей конструкции ракеты = {str(num)} кг"

	def _rocket_total_oil(num: float) -> str:
		return f"Сумма всего топлива = {str(num)} кг"


class FlightFormat:
	def _flight_resistance_force(num: float) -> str:
		return f"Сила сопротивления = {str(num)} H"

	def _flight_resistance_force_env(num: float) -> str:
		return f"Сила сопротивления среды = {str(num)} H"

	def _flight_distance(num: float) -> str:
		return f"Расстояние полета ракеты = {str(num)} км"

	def _flight_mass(num: float) -> str:
		return f"Масса ракеты = {str(num)} т"


# Функция для вывода результатов, той или иной функции
def main_rocket_format(num: float, idea: int) -> str:
	if idea == 1:
		return RocketFormat._rocket_total_speed(num)
	elif idea == 2:
		return RocketFormat._rocket_natural_logarithm(num)
	elif idea == 3:
		return RocketFormat._rocket_massa_construction(num)
	elif idea == 4:
		return RocketFormat._rocket_total_oil(num)
	elif idea == 5:
		return FlightFormat._flight_resistance_force(num)
	elif idea == 6:
		return FlightFormat._flight_distance(num)
	elif idea == 7:
		return FlightFormat._flight_mass(num)
