"""
В этом файле я буду пробовать разные графики, тренды и интересные функции matplotlib.
Никаких зависимостей с основным проектом нет!
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


data_line = (
	[1, 2, 3, 4],
	[1, 4, 2, 3],
	[1, 5, 3, 4],
	[1, 3, 2, 5]
)

# Axis - Эти объекты задают масштаб и пределы,
# 	а также генерируют отметки (метки на оси) и метки
# 	(строки, обозначающие отметки).
# Axes - это прикрепление к графику,
# 	который содержит область для построения данных и
# 	обычно включает в себя два (или три в случае 3D)


def line_graph():
	# Простой способ сделать фигуру с осями - использовать
	# 	pyplot.subplots
	fig, ax = plt.subplots()
	ax.plot(data_line[0], data_line[1], data_line[2], data_line[3])
	plt.show()


# Функции построения графиков
def matrix_graph():
	b = np.matrix([[1, 2], [3, 4]])
	b_asarray = np.asarray(b)

	np.random.seed(19680801)  # seed the random number generator.

	data = {'a': np.arange(50),
	        'c': np.random.randint(0, 50, 50),
	        'd': np.random.randn(50)}
	data['b'] = data['a'] + 10 * np.random.randn(50)
	data['d'] = np.abs(data['d']) * 100

	fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
	ax.scatter('a', 'b', c='c', s='d', data=data)
	ax.set_xlabel('entry a')
	ax.set_ylabel('entry b')
	plt.show()


def simple_plot_graph():
	x = np.linspace(0, 2, 100)  # Некоторые данные

	fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
	ax.plot(x, x, label='linear')  # Нанесите некоторые данные на оси.
	ax.plot(x, x**2, label='quadratic')
	ax.plot(x, x**3, label='cubic')
	ax.set_xlabel('x label')  # x-label
	ax.set_ylabel('y label')  # y-label
	ax.set_title("Simple Plot")  # title
	ax.legend()

	plt.show()

if __name__ == "__main__":
	simple_plot_graph()
