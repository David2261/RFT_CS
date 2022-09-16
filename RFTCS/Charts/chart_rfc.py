"""
Файл для вывода графика расчетов ракеты
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def fuel_charts(stage: int, y: list) -> None:
	x = list()
	for i in range(stage + 1):
		x.append(i)
	plt.plot(x, y, label='Скорость')
	plt.xlabel(
		'Ступень',
		fontweight='book',
		fontstyle='italic',
		color='blue',
		fontsize='medium')
	plt.ylabel(
		'Скорость',
		fontweight='book',
		fontstyle='oblique',
		color='green',
		fontsize='medium'
	)
	plt.title('Изменение скорости ракеты', size='20')
	plt.legend()
	plt.grid(True)
	plt.show()


if __name__ == "__main__":
	y_list = [0, 6461.95, 8489.82, 6764.82]
	fuel_charts(3, y_list)


