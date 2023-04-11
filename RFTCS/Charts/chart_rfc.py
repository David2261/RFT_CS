"""
Файл для вывода графика расчетов ракеты
"""
# import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def fuel_charts(y, func) -> None:
	# Data
	X = np.linspace(0, np.pi * 4, 1000)
	Y = func(X)
	fig = plt.figure(figsize=(12, 8))
	ax_1 = fig.add_subplot(2, 1, 1)

	ax_1.plot(X, Y)
	ax_1.set(title="RFT_CS")
	plt.show()


if __name__ == "__main__":
	fuel_charts(4200, lambda x: x**2 + x)
