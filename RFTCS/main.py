from format import *
from rocket_flight_simulation import *
from rocket_fuel_calculation import *
from rocket_landing_calculation import *



def main():
	speed = 0
	Isp_total = 0
	Mass_full_total = 0
	Mass_empty_total = 0

	stage = int(input("Напишите количество ступеней: "))
	n = 0
	while (n <= stage):
		Isp = input(
			f"Напишите удельный импульс для {n + 1} ступени: ")
		Isp_total += float(Isp)
		Mass_full = input(
			f"Напишите масса полного топлива для {n + 1} ступени: ")
		Mass_full_total += float(Mass_full)
		Mass_empty = input(
			f"Напишите масса без топлива для {n + 1} ступени: ")
		Mass_empty_total += float(Mass_empty)
		
		print("\n")
		n += 1
		if n == stage:
			break
	speed += total_speed(Isp_total, Mass_full_total, Mass_empty_total)

	return main_rocket_format(round(speed, 2), 1)


if __name__ == "__main__":
	print(main())





