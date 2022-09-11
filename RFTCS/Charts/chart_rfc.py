"""
Файл для вывода графика расчетов ракеты
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



def charts() -> None:
	# evenly sampled time at 200ms intervals
	t = np.arange(0., 5., 0.2)

	# red dashes, blue squares and green triangles
	plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
	plt.show()


if __name__ == "__main__":
	charts()


