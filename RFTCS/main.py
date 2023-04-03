import logging
import logging.config

from exceptions.exception import (
	invalid_entire,
	invalid_type,
	invalid_general,
	invalid_import
)
from setup.logging_conf import LOGGING_CONF

# Логгирование
# logging.config.fileConfig('log.conf')
# logger = logging.getLogger('dev')
# logging.basicConfig(
# 	filename='__logs__/main.log',
# 	encoding='utf-8',
# 	level=logging.NOTSET,
# 	format='%(asctime)s - [%(levelname)s] - %(name)s -
# 	(%(filename)s).%(funcName)s((%lineno)d) - %(message)s')

DEBUG = True

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")


try:
	from display.format import main_rocket_format
	from rocket_flight_simulation import Resistance, ModelFlight
	from rocket_fuel_calculation import TotalOil
	from rocket_flight_trajectory import FlightBallistics
	from display.display_table import (
		display_info,
		fuel_display,
		flight_simulation_display,
		landing_display,
	)

	log_info.info("Импортирование файлов в main.py")
except ImportError as e:
	logger.error(invalid_import(e))
	raise ImportError(invalid_import(e))


# Вывод первой подсказки
def output_info() -> list:
	log_info.info("Запуск функции output_")
	print(
		"Какой формат вывода информации хотите?\n"
		"В виде текста (1) или ввиде таблицы (2): "
	)
	try:
		num = int(input())
	except ValueError as e:
		logger.error(invalid_entire(e))
		raise ValueError(invalid_entire(e))
	display_info()
	try:
		selection = int(input())
	except ValueError as e:
		logger.error(invalid_entire(e))
		raise ValueError(invalid_entire(e))
	return [num, selection]


def fuel_input(stage: int) -> list:
	speed = 0
	Isp_total = 0
	Mass_full_total = 0
	Mass_empty_total = 0
	Mass_fuel_total = 0
	log_info.info("Включение функции 'fuel_input'")

	n = 0
	while n < stage:
		try:
			try:
				Isp = float(input(f"Напишите удельный импульс для {n + 1} ступени: "))
			except ValueError as e:
				logger.error(invalid_entire(e))
				raise ValueError(invalid_entire(e))
			except TypeError as e:
				logger.error(invalid_type(e))
				raise TypeError(invalid_type(e))
			Isp_total += Isp
			try:
				Mass_full = float(
					input(f"Напишите масса полного топлива для {n + 1} ступени: ")
				)
			except ValueError as e:
				logger.error(invalid_entire(e))
				raise ValueError(invalid_entire(e))
			except TypeError as e:
				logger.error(invalid_type(e))
				raise TypeError(invalid_type(e))
			Mass_full_total += Mass_full
			try:
				Mass_empty = float(
					input(f"Напишите масса без топлива для {n + 1} ступени: ")
				)
			except ValueError as e:
				logger.error(invalid_entire(e))
				raise ValueError(invalid_entire(e))
			except TypeError as e:
				logger.error(invalid_type(e))
				raise TypeError(invalid_type(e))
			Mass_empty_total += Mass_empty
			log_info.info(f"Пройден цикл = {n+1}")
		except ValueError as e:
			logger.error(invalid_entire(e))
			raise TypeError(invalid_type(e))
		fuel = TotalOil(Mass_empty, Mass_full_total, Isp)
		Mass_fuel_total += fuel.total_oil()
		print("\n")
		n += 1
		if n == stage:
			break
	fuel = TotalOil(Mass_empty_total, Mass_full_total, Isp_total)
	speed = fuel.total_speed()
	return [speed, Mass_fuel_total]


def flight_model_input(stage: int) -> list:
	n = 0
	sum_resistance = 0
	total_speed = 0
	total_time = 0
	total_resistance = 0
	log_info.info("Включение flight_model_input")

	while n < stage:
		try:
			speed = float(input("Напишите скорость ракеты: "))
			fuel_flow = float(input("Напишите расход ступени: "))
			mass = float(input("Напишите массу ракеты: "))
			time = float(input("Время работы двигателя: "))
		except ValueError as e:
			logger.error(invalid_entire(e))
			raise ValueError(invalid_entire(e))
		except TypeError as e:
			logger.error(invalid_type(e))
			raise TypeError(invalid_type(e))
		resistance = Resistance(speed, fuel_flow, mass)

		# res_env = resistance.resistance_force() - Этого нет (т.е. функция была удалена)
		gl = resistance.gravitation_losses()
		al = resistance.aerodynamic_drag()
		lsc = resistance.control_losses()
		sum_resistance = gl + al + lsc

		total_resistance += sum_resistance
		total_speed += speed
		total_time += time
		log_info.info(f"Пройден цикл = {n + 1}")
		n += 1
	distance = total_speed * time - total_resistance
	return [total_resistance, distance, mass]


def landing_model_input(stage: int) -> list:
	n = 0
	mm = 0
	log_info.info("Включение landing_model_input")
	try:
		time = float(input("Время полета ракеты: "))
		speed_0 = float(input("Напишите начальную скорость ракеты: "))
	except ValueError as e:
		logger.error(invalid_entire(e))
		raise ValueError(invalid_entire(e))
	except TypeError as e:
		logger.error(invalid_type(e))
		raise TypeError(invalid_type(e))
	while n < stage:
		try:
			mass = float(input(f"Напишите массу ступени ({stage}): "))
			fuel_flow = float(input("Напишите расход ступени: "))
		except ValueError as e:
			logger.error(invalid_entire(e))
			raise ValueError(invalid_entire(e))
		except TypeError as e:
			logger.error(invalid_type(e))
			raise TypeError(invalid_type(e))
		model = ModelFlight(fuel_flow, mass, speed_0, time)
		model_stack = model.model_stack()
		ballistic = FlightBallistics(model_stack[1])
		mm += ballistic.flight_range()
		log_info.info(f"Пройден цикл = {n + 1}")
		n += 1
	return [mm, model_stack[2], model_stack[3]]


def function_output(enter: list, stage: int) -> None:
	# 1 - строка, 2 - таблица
	display = enter[0]
	# 1 - топливо, 2 - Полет, 3 - Моделирование полета
	function = enter[1]
	log_info.info("Включение function_output")
	if function == 1:
		if display == 1:
			fuel_data = fuel_input(stage)
			main_rocket_format(round(fuel_data[0], 2), 1)
			main_rocket_format(round(fuel_data[1], 2), 4)
		elif display == 2:
			fuel_data = fuel_input(stage)
			stack = [round(fuel_data[0], 2), round(fuel_data[1], 2)]
			fuel_display(stack)
		else:
			invalid_entire(f"Не тот вывод информации {display}")
	elif function == 2:
		if display == 1:
			land_data = landing_model_input(stage)
			main_rocket_format(round(land_data[0], 2), 8)
			main_rocket_format(round(land_data[1], 2), 10)
			main_rocket_format(round(land_data[2], 2), 11)
		elif display == 2:
			land_data = landing_model_input(stage)
			stack = [
				round(land_data[0], 2),
				round(land_data[1], 2),
				round(land_data[2], 2),
			]
			landing_display(stack)
		else:
			invalid_entire(f"Не тот вывод информации {display}")
	elif function == 3:
		if display == 1:
			flight_data = flight_model_input(stage)
			main_rocket_format(round(flight_data[0], 2), 5)
			main_rocket_format(round(flight_data[1], 2), 6)
			main_rocket_format(round(flight_data[2], 2), 7)
		elif display == 2:
			flight_data = flight_model_input(stage)
			stack = [
				round(flight_data[0], 2),
				round(flight_data[1], 2),
				round(flight_data[2], 2),
			]
			flight_simulation_display(stack)
		else:
			invalid_entire(f"Не тот вывод информации {display}")


def main() -> None:
	log_info.info("Начало функции main")
	stage = input("Напишите количество ступеней: ")
	try:
		stage = int(stage)
		screen = output_info()
		function_output(screen, stage)
	except Exception as e:
		logger.error(invalid_general(e))
		raise Exception(invalid_general(e))


if __name__ == "__main__":
	main()
