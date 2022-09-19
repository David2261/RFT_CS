from prettytable import PrettyTable


pt = PrettyTable()


def display_info():
	pt.field_names = ["Fuel", "Landing", "Flight"]
	pt.add_row([1, 2, 3])
	print(pt)


def fuel_display(stack: list) -> None:
	pt.clear()
	pt.field_names = ["Speed total", "Total oil"]
	pt.add_row([stack[0], stack[1]])
	print(pt)


def flight_simulation_display(stack: list) -> None:
	pt.clear()
	pt.field_names = ["Amount of losses", "Distance", "Mass"]
	pt.add_row(stack)
	print(pt)


def landing_display(stack: list) -> None:
	pt.clear()
	pt.field_names = ["Mathematic model", "x", "y"]
	pt.add_row(stack)
	print(pt)

if __name__ == "__main__":
	display_info()
	num = int(input("Write your choice: "))
	data_fuel = [52258.61, 32.78]
	data_flight = [24.47, 2500, 56.2]
	data_landing = [56.2, 657, 3282]
	if num == 1:
		fuel_display(data_fuel)
	elif num == 2:
		landing_display(data_landing)
	elif num == 3:
		flight_simulation_display(data_flight)
	else:
		print("Bad request!")




"""
+-------------+-----------+
| Speed total | Total oil |
+-------------+-----------+
|   52258.61  |   32.78   |
+-------------+-----------+
"""