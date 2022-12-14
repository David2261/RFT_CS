import matplotlib.pyplot as plt
import numpy as np


def sin_wave():
	fig = plt.figure()
	fig.subplots_adjust(top=0.8)
	ax1 = fig.add_subplot(211)
	ax1.set_ylabel('Вольт')
	ax1.set_title('Синусоидная')

	t = np.arange(0.0, 1.0, 0.01)
	s = np.sin(2*np.pi*t)
	line, = ax1.plot(t, s, color='red', lw=2)

	# Фиксация случайного состояния для воспроизводимости
	np.random.seed(19680801)

	ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
	n, bins, patches = ax2.hist(
		np.random.randn(1000),
		50,
		facecolor='yellow',
		edgecolor='blue'
	)
	ax2.set_xlabel('Время')

	plt.show()


def cos_wave():
	fig = plt.figure()
	fig.subplots_adjust(top=0.8)
	ax1 = fig.add_subplot(211)
	ax1.set_title('Косинусоидная')

	time = np.arange(0.0, 1.0, 0.01)
	c = np.cos(2 * np.pi * time)
	line = ax1.plot(time, c, color='blue', lw=2)

	np.random.seed(19680801)
	ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
	n, bins, patches = ax2.hist(
		np.random.randn(1000),
		50,
		facecolor='orange',
		edgecolor='blue'
	)
	ax2.set_xlabel('Время')
	plt.show()



if __name__ == '__main__':
	sin_wave()
	cos_wave()
