import matplotlib as mlt
import matplotlib.pyplot as plt
import numpy as np



def price_to_value():

	# plt.plot([1, 4, 2, 6, 9, 2]) # Только по Y
	# По осям Y и X
	x = [1, 5, 10, 15, 20]
	y = [1, 7, 3, 5, 11]
	plt.plot(x, y, label='Steel cost')
	plt.xlabel(
		'Price',
		fontweight='book',
		fontstyle='italic',
		color='blue',
		fontsize='medium')
	plt.ylabel(
		'Value',
		fontweight='book',
		fontstyle='oblique',
		color='green',
		fontsize='medium'
	)
	plt.title('Inflatian', size='20')
	plt.legend()
	plt.grid(True)
	plt.text(16.3, 5.1, 'The big deal!')
	plt.show()


def sell_cars():
	x = [1, 3, 6, 8, 10, 20]
	y1 = [1, 2, 5, 9, 12, 26]
	plt.plot(x, y1, '--r', label='Renault')
	y2 = [i*1.2 + 1 for i in y1]
	plt.plot(x, y2, '-', label='Porsche')
	y3 = [i*1.2 + 1 for i in y2]
	plt.plot(x, y3, '-.', label='Mercedes')
	y4 = [i*1.2 + 1 for i in y3]
	plt.plot(x, y4, 'ro', label='Volkswagen')
	y5 = [i*1.2 + 1 for i in y4]
	plt.plot(x, y5, ':', label='Audi')

	plt.title('Sells', size=20)
	plt.legend()
	plt.show()






if __name__ == "__main__":
	sell_cars()




