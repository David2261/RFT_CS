from format import *
from rocket_flight_simulation import *
from rocket_fuel_calculation import *
from rocket_landing_calculation import *
from display_table import *


def output_info() -> list:
	print("Какой формат вывода информации хотите?\n" + \
		"В виде текста (1) или ввиде таблицы (2):")
	num = int(input( ))
	display_info()
	selection = int(input( ))
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
	height = float(input("Напишите высоту ракеты: "))
	width = float(input("Напишите ширину ракеты: "))

	while (n < stage):
		speed = float(input("Напишите скорость ракеты: "))
		etf = float(input("Напишите силу тяги двигателя: "))
		mass = float(input("Напишите массу ракеты: "))
		gamma = float(input(
			"Напишите угол между вектором силы тяги и местным вектором: "))
		fad = float(input(
			"Сила лобового аэродинамического сопротивления: "))
		time = float(input("Время работы двигателя: "))

		res_env = resistance_force(speed, 0.04)
		gl = gravity_losses(etf, gamma, time)
		al = aerodynamic_losses(fad, mass, time)
		lsc = loss_speed_on_control(etf, mass, gamma, time)
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
	x = 0
	y = 0
	while (n < stage):
		speed = float(input("Напишите скорость ракеты: "))
		resistance = float(input("Напишите общее сопротивление: "))
		teta = float(input(
			"Напишите угол между вектором силы тяги и местным вектором: "))
		mm += calculation_rocket_movement(speed, resistance)
		stack = rocket_flight_description(teta, speed, 1, resistance, 1)
		y += stack[0]
		x += stack[1]
		n += 1
	return [mm, x, y]


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
			...
	elif function == 2:
		if display == 1:
			land_data = landing_model_input(stage)
			main_rocket_format(round(land_data[0], 2), 8)
			main_rocket_format(round(land_data[1], 2), 10)
			main_rocket_format(round(land_data[2], 2), 11)
		elif display == 2:
			land_data = landing_model_input(stage)
			stack = [round(land_data[0], 2), round(land_data[1], 2), round(land_data[2], 2)]
			landing_display(stack)
		else:
			...
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
			...

def main() -> None:
	stage = int(input("Напишите количество ступеней: "))
	screen = output_info()
	function_output(screen, stage)


if __name__ == "__main__":
	main()

