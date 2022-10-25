"""
В этом файле собраны все способы форматирования результатов
"""
from typing import NamedTuple, Union
from colorama import init

init()

from colorama import Fore, Back, Style


def checker(number):
	if isinstance(number, (float, int)):
		return number
	else: 
		ValueError()



class RocketFormat:
	@checker
	def _rocket_total_speed(num) -> str:
		text = f"Сумма всех скоростей = {str(num)} м/с"
		print(Fore.GREEN + text)
		return text

	@checker
	def _rocket_natural_logarithm(num: Union[int, float]) -> str:
		text = f"Натуральный логарифм = {str(num)}"
		print(Fore.GREEN + text)
		return text

	@checker
	def _rocket_massa_construction(num: Union[int, float]) -> str:
		text = f"Сумма всей конструкции ракеты = {str(num)} кг"
		print(Fore.GREEN + text)
		return text

	@checker
	def _rocket_total_oil(num: Union[int, float]) -> str:
		text = f"Сумма всего топлива = {str(num)} кг"
		print(Fore.GREEN + text)
		return text


class FlightFormat:
	@checker
	def _flight_resistance_force(num: float) -> str:
		text = f"Сила сопротивления = {str(num)} H"
		print(Fore.GREEN + text)
		return text

	@checker
	def _flight_resistance_force_env(num: float) -> str:
		text = f"Сила сопротивления среды = {str(num)} H"
		print(Fore.GREEN + text)
		return text

	@checker
	def _flight_distance(num: float) -> str:
		text = f"Расстояние полета ракеты = {str(num)} км"
		print(Fore.GREEN + text)
		return text

	@checker
	def _flight_mass(num: float) -> str:
		text = f"Масса ракеты = {str(num)} т"
		print(Fore.GREEN + text)
		return text


class LandingFormat:
	@checker
	def _calculation_rocket_movement(num: float) -> str:
		text = f"Математическая модель полета ракеты = {num}"
		print(Fore.GREEN + text)
		return text

	@checker
	def _vector_speed(num: float) -> str:
		text = f"Вектор скорости = {num} км/c"
		print(Fore.GREEN + text)
		return text

	@checker
	def _rocket_flight_y(num: float) -> str:
		text = f"Координата ракеты y = {num}"
		print(Fore.GREEN + text)
		return text

	@checker
	def _rocket_flight_x(num: float) -> str:
		text = f"Координата ракеты x = {num}"
		print(Fore.GREEN + text)
		return text


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


if __name__ == '__main__':
	main_rocket_format('sdasd', 1)