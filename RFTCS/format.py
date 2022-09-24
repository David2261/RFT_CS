"""
В этом файле собраны все способы форматирования результатов
"""
from colorama import init

init()

from colorama import Fore, Back, Style


class RocketFormat:
	def _rocket_total_speed(num: float) -> None:
		print(Fore.GREEN + f"Сумма всех скоростей = {str(num)} м/с")

	def _rocket_natural_logarithm(num: float) -> None:
		print(Fore.GREEN + f"Натуральный логарифм = {str(num)}")

	def _rocket_massa_construction(num: float) -> None:
		print(Fore.GREEN + f"Сумма всей конструкции ракеты = {str(num)} кг")

	def _rocket_total_oil(num: float) -> None:
		print(Fore.GREEN + f"Сумма всего топлива = {str(num)} кг")


class FlightFormat:
	def _flight_resistance_force(num: float) -> None:
		print(Fore.GREEN + f"Сила сопротивления = {str(num)} H")

	def _flight_resistance_force_env(num: float) -> None:
		print(Fore.GREEN + f"Сила сопротивления среды = {str(num)} H")

	def _flight_distance(num: float) -> None:
		print(Fore.GREEN + f"Расстояние полета ракеты = {str(num)} км")

	def _flight_mass(num: float) -> None:
		print(Fore.GREEN + f"Масса ракеты = {str(num)} т")


class LandingFormat:
	def _calculation_rocket_movement(num: float) -> None:
		print(Fore.GREEN + f"Математическая модель полета ракеты = {num}")

	def _vector_speed(num: float) -> None:
		print(Fore.GREEN + f"Вектор скорости = {num} км/c")

	def _rocket_flight_y(num: float) -> None:
		print(Fore.GREEN + f"Координата ракеты y = {num}")

	def _rocket_flight_x(num: float) -> None:
		print(Fore.GREEN + f"Координата ракеты x = {num}")


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
	elif idea == 8:
		return LandingFormat._calculation_rocket_movement(num)
	elif idea == 9:
		return LandingFormat._vector_speed(num)
	elif idea == 10:
		return LandingFormat._rocket_flight_y(num)
	elif idea == 11:
		return LandingFormat._rocket_flight_x(num)
