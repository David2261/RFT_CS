from format import *
from rocket_flight_simulation import *
from rocket_fuel_calculation import *
from rocket_landing_calculation import *
from display_table import *

def output():
	display_info()
	print("Какой формат вывода информации хотите\n\
		В виде текста (1) или ввиде таблицы (2):")
	num = int(input( ))
	return num


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

def main() -> None:
	num = output()
	if num == 1:
		fuel_data = fuel_input()
		print(main_rocket_format(round(fuel_data[0], 2), 1))
		print(main_rocket_format(round(fuel_data[1], 2), 4))
	elif num == 2:
		fuel_data = fuel_input()
		stack = [round(fuel_data[0], 2), round(fuel_data[1], 2)]
		fuel_display(stack)
	else:
		...



if __name__ == "__main__":
	main()





