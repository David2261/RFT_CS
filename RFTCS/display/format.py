"""
В этом файле собраны все способы форматирования результатов
"""
from colorama import init
init()
from colorama import Fore

import logging
import logging.config

from RFTCS.setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")


class RocketFormat:
	log_info.info("Запуск класса 'RocketFormat'")

	def __init__(self, num):
		self.num = num

	def rocket_total_speed(self) -> str:
		text = f"Сумма всех скоростей = {str(self.num)} м/с"
		print(Fore.GREEN + text)
		return text

	def _rocket_natural_logarithm(self) -> str:
		text = f"Натуральный логарифм = {str(self.num)}"
		print(Fore.GREEN + text)
		return text

	def _rocket_massa_construction(self) -> str:
		text = f"Сумма всей конструкции ракеты = {str(self.num)} кг"
		print(Fore.GREEN + text)
		return text

	def _rocket_total_oil(self) -> str:
		text = f"Сумма всего топлива = {str(self.num)} кг"
		print(Fore.GREEN + text)
		return text


class FlightFormat:
	log_info.info("Запуск класса 'FlightFormat'")

	def __init__(self, num):
		self.num = num

	def _flight_resistance_force(self) -> str:
		text = f"Сила сопротивления = {str(self.num)} H"
		print(Fore.GREEN + text)
		return text

	def _flight_resistance_force_env(self) -> str:
		text = f"Сила сопротивления среды = {str(self.num)} H"
		print(Fore.GREEN + text)
		return text

	def _flight_distance(self) -> str:
		text = f"Расстояние полета ракеты = {str(self.num)} км"
		print(Fore.GREEN + text)
		return text

	def _flight_mass(self) -> str:
		text = f"Масса ракеты = {str(self.num)} т"
		print(Fore.GREEN + text)
		return text


class LandingFormat:
	log_info.info("Запуск класса 'LandingFormat'")

	def __init__(self, num):
		self.num = num

	def _calculation_rocket_movement(self) -> str:
		text = f"Математическая модель полета ракеты = {self.num}"
		print(Fore.GREEN + text)
		return text

	def _vector_speed(self) -> str:
		text = f"Вектор скорости = {self.num} км/c"
		print(Fore.GREEN + text)
		return text

	def _rocket_flight_y(self) -> str:
		text = f"Расстояние полета ракеты = {self.num}"
		print(Fore.GREEN + text)
		return text

	def _rocket_flight_x(self) -> str:
		text = f"Угол поворота ракеты tg Beta = {self.num}"
		print(Fore.GREEN + text)
		return text


def main_rocket_format(num: float, idea: int) -> str:
	""" Функция для вывода результатов, той или иной функции """
	log_info.info("Запуск функции 'main_rocket_format'")
	num = str(num)  # type: ignore[assignment]
	if idea == 1:
		rf = RocketFormat(num)
		a = rf.rocket_total_speed()
		return a
	elif idea == 2:
		rf = RocketFormat(num)
		return rf._rocket_natural_logarithm()
	elif idea == 3:
		rf = RocketFormat(num)
		return rf._rocket_massa_construction()
	elif idea == 4:
		rf = RocketFormat(num)
		return rf._rocket_total_oil()
	elif idea == 5:
		ff = FlightFormat(num)
		return ff._flight_resistance_force()
	elif idea == 6:
		ff = FlightFormat(num)
		return ff._flight_distance()
	elif idea == 7:
		ff = FlightFormat(num)
		return ff._flight_mass()
	elif idea == 8:
		lf = LandingFormat(num)
		return lf._calculation_rocket_movement()
	elif idea == 9:
		lf = LandingFormat(num)
		return lf._vector_speed()
	elif idea == 10:
		lf = LandingFormat(num)
		return lf._rocket_flight_y()
	elif idea == 11:
		lf = LandingFormat(num)
		return lf._rocket_flight_x()
	else:
		return "Incorrectly selected item in the format file"


if __name__ == '__main__':
	text = main_rocket_format('sdasd', 1)  # type: ignore[arg-type]
