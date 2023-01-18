"""
Файл для вывода графика расчетов ракеты
"""
import numpy as np
import matplotlib.pyplot as plt


def func_plot(num: int) -> None:
	# Data
	width = 0.4
	x = list(range(0, 15))
	x_2 = list(range(0, 15))
	x_indexes = np.arange(len(x))
	step = round(num / 15)
	y = []
	y_2 = [
		1200, 1143, 1101,
		987, 1234, 1400,
		1679, 2320, 2780,
		3090, 3407, 3650,
		3899, 4100, 4159]
	y_3 = [
		2320, 1143, 1101,
		1200, 1234, 1400,
		1679, 987, 2780,
		3090, 3407, 3650,
		3899, 4159, 4100]
	for i in range(15):
		if i != 14:
			y.append(i * step)
		else:
			y.append(num)

	# 1 Graphic
	plt.figure()
	plt.subplot(2, 2, 1)

	# Meta data
	plt.title("RFT_CS")
	plt.xlabel('Hours')
	plt.ylabel('Isp')

	plt.plot(x, y, label="Falcon 9", marker="x")
	plt.plot(x_2, y_2, label="Starship", marker="^")
	plt.plot(x, y_3, label="Grasshoper", marker="*")
	plt.legend()

	# 2 Graphic
	plt.subplot(2, 2, 2)
	plt.title("RFT_CS")
	plt.xlabel('Minutes')
	plt.ylabel('Isp')
	# Meta data
	plt.bar(x_indexes - (width / 2), y, label="Falcon 9", width=width)
	plt.bar(x_indexes + (width / 2), y_2, label="Starship", width=width)
	plt.legend()

	# 3 Graphic
	plt.subplot(2, 1, 2)
	plt.title("RFT_CS")
	plt.xlabel('Minutes')
	plt.ylabel('Isp')
	# Meta data
	plt.bar(x_indexes - (width / 2), y, label="Falcon 9", width=width)
	plt.bar(x_indexes + (width / 2), y_2, label="Starship", width=width)
	plt.bar(x_indexes + (width / 2), y_3, label="Starship", width=width)
	plt.legend()
	plt.show()


if __name__ == '__main__':
	func_plot(4200)
