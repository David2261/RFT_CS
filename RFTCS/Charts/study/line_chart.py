import matplotlib as mlt
import matplotlib.pyplot as plt
import numpy as np



def line_graph():

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



if __name__ == "__main__":
	line_graph()




