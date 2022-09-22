from format import *
from rocket_flight_simulation import *
from rocket_fuel_calculation import *
from rocket_landing_calculation import *
from display_table import *


def output_info() -> list:
	print("Какой формат вывода информации хотите\n\
		В виде текста (1) или ввиде таблицы (2):")
	num = int(input( ))
	display_info()
	selection = int(input( ))
	return [num, selection]



def fuel_input() -> list:
	speed = 0
	Isp_total = 0
	Mass_full_total = 0
	Mass_empty_total = 0
	Mass_fuel_total = 0

	stage = int(input("Напишите количество ступеней: "))
	n = 0
	while (n <= stage):
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


def flight_model_input() -> list:
	height = float(input("Напишите высоту ракеты: "))
	width = float(input("Напишите ширину ракеты: "))
	speed = float(input("Напишите скорость ракеты: "))
	etf = float(input("Напишите силу тяги двигателя: "))
	mass = float(input("Напишите массу ракеты: "))
	gamma = float(input("Напишите угол между вектором силы тяги и \
		местным вектором: "))
	fad = float(input("Сила лобового аэродинамического сопротивления: "))

	res_env = resistance_force_env(height, width, speed)
	gl = gravity_losses(gamma)
	al = aerodynamic_losses(fad, mass)
	lsc = loss_speed_on_control(etf, mass, gamma)

	total_resistance = gl + al + lsc + res_env
	distance = 1.2
	return [total_resistance, distance, mass]


def function_output(enter: list) -> None:
	# 1 - строка, 2 - таблица
	display = enter[0]
	# 1 - топливо, 2 - Полет, 3 - Моделирование полета
	function = enter[1]
	if function == 1:
		if display == 1:
			fuel_data = fuel_input()
			print(main_rocket_format(round(fuel_data[0], 2), 1))
			print(main_rocket_format(round(fuel_data[1], 2), 4))
		elif display == 2:
			fuel_data = fuel_input()
			stack = [round(fuel_data[0], 2), round(fuel_data[1], 2)]
			fuel_display(stack)
		else:
			...
	elif function == 2:
		...
	elif function == 3:
		if display == 1:
			flight_data = flight_model_input()
			print(main_rocket_format(round(flight_data[0], 2), 5))
			print(main_rocket_format(round(flight_data[1], 2), 6))
			print(main_rocket_format(round(flight_data[2], 2), 7))
		elif display == 2:
			flight_data = flight_model_input()
			stack = [
				round(flight_data[0], 2),
				round(flight_data[1], 2),
				round(flight_data[2], 2)
			]
			flight_simulation_display(stack)
		else:
			...

def main() -> None:
	screen = output_info()
	function_output(screen)


if __name__ == "__main__":
	main()





