# Линейный график


*Основным элементом изображения, которое строит pyplot является Фигура (Figure), на нее накладываются один или более графиков, осей, надписей и т.п. Для построения графика используется команда plot(). В самом минимальном варианте можно ее использовать без параметров:*
```python
import matplotlib.pyplot as plt
plt.plot()
```

### Пример
*Пример создания графика, по заданным координатам.*
```python
def line_graph():

	# plt.plot([1, 4, 2, 6, 9, 2]) # Только по Y
	# По осям Y и X
	plt.plot([1, 5, 10, 15, 20], [1, 7, 3, 5, 11])
	plt.show()
```
_График:_ ![Линейный график](/img/line_chart_XY.jpeg)

### Параметры для графика
- наименование осей;
	- xlabel (или ylabel): str
		- Текст подписи.
	- labelpad: численное значение либо None; значение по умолчанию: None
		- Расстояние между областью графика, включающую оси, и меткой.
- наименование самого графика [plt.title()]
- текстовое примечание на поле с графиком [plt.text()]
- легенда - это название линии

### Пример графика с параметрами
```python
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
```

### Работа с линейным графиком
*\*Настройка графиков других видов, будет осуществляться сходным образом.*

