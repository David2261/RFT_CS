import os
import sys
import logging
import logging.config

path = os.path.join(os.getcwd(), '../')
sys.path.append(path)


from display.format import main_rocket_format
from rocket_flight_simulation import (
	Resistance,
	Speed,
	ModelFlight
)
from rocket_fuel_calculation import TotalOil
from rocket_flight_trajectory import FlightBallistics
from display.display_table import (
	display_info,
	fuel_display,
	flight_simulation_display,
	landing_display
)
from exceptions.exception import invalid_entire


# Логгирование
logging.config.fileConfig('log.conf')

logger = logging.getLogger('dev')




# Вывод первой подсказки
def output_info() -> list:
	print(
		"Какой формат вывода информации хотите?\n"
		"В виде текста (1) или ввиде таблицы (2): ")
	num = int(input())
	display_info()
	selection = int(input())
	return [num, selection]


def fuel_input(stage: int) -> list:
	speed = 0
	Isp_total = 0
	Mass_full_total = 0
	Mass_empty_total = 0
	Mass_fuel_total = 0

	n = 0
	while (n < stage):
		Isp = float(input(
			f"Напишите удельный импульс для {n + 1} ступени: "))
		Isp_total += Isp
		Mass_full = float(input(
			f"Напишите масса полного топлива для {n + 1} ступени: "))
		Mass_full_total += Mass_full
		Mass_empty = float(input(
			f"Напишите масса без топлива для {n + 1} ступени: "))
		Mass_empty_total += Mass_empty
		Mass_fuel_total += total_oil(
			Isp,
			total_speed(Isp_total, Mass_full_total, Mass_empty_total),
			Mass_empty)
		print("\n")
		n += 1
		if n == stage:
			break
	speed += total_speed(Isp_total, Mass_full_total, Mass_empty_total)
	return [speed, Mass_fuel_total]


def flight_model_input(stage: int) -> list:
	n = 0
	sum_resistance = 0
	total_speed = 0
	total_time = 0
	total_resistance = 0

	while (n < stage):
		speed = float(input("Напишите скорость ракеты: "))
		fuel_flow = float(input("Напишите расход ступени: "))
		mass = float(input("Напишите массу ракеты: "))
		time = float(input("Время работы двигателя: "))
		resistance = Resistance(speed, fuel_flow, mass)

		res_env = resistance.resistance_force()
		gl = resistance.gravity_losses()
		al = resistance.aerodynamic_losses()
		lsc = resistance.loss_speed_on_control()
		sum_resistance = gl + al + lsc + res_env

		total_resistance += sum_resistance
		total_speed += speed
		total_time += time
		n += 1
	distance = total_speed * time - total_resistance
	return [total_resistance, distance, mass]


def landing_model_input(stage: int) -> list:
	n = 0
	mm = 0
	stage = float(input("Напишите количество ступеней: "))
	time = float(input("Время полета раакеты: "))
	speed_0 = float(input("Напишите начальную скорость ракеты: "))
	while (n < stage):
		mass = float(input(f"Напишите массу ступени ({stage}): "))
		fuel_flow = float(input("Напишите расход ступени: "))
		model = ModelFlight(fuel_flow, mass, speed_0, time)
		model_stack = model.model_stack()
		ballistic = FlightBallistics(model_stack[1])

		mm += ballistic.flight_range()
	return [mm, model_stack[2], model_stack[3]]


def function_output(enter: list, stage: int) -> None:
	# 1 - строка, 2 - таблица
	display = enter[0]
	# 1 - топливо, 2 - Полет, 3 - Моделирование полета
	function = enter[1]
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
				round(land_data[2], 2)
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
				round(flight_data[2], 2)
			]
			flight_simulation_display(stack)
		else:
			invalid_entire(f"Не тот вывод информации {display}")


def main() -> None:
	stage = input("Напишите количество ступеней: ")
	try:
		stage = int(stage)
		screen = output_info()
		function_output(screen, stage)
	except ValueError:
		logger.error(f"Вы ввели некоректные данные: {stage}")


if __name__ == "__main__":
	main()
