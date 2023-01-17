# Численное моделирование топлива ракеты

## Описание
*Численное моделирование топлива ракеты. Производяться расчеты связанные с кольчеством топлива на разных стадиях топлива.*

## Импорты
Импортируется библиотеки numpy и matplotlib, и typing.
Из файла format импортируется функция main_rocket_format, для более удобного вывода результа в консоль.

## Классы
- TotalOil (Класс для расчета топлива) - принимает 3 параметра (масса пустой и полной ракеты, и Isp, с типом float).
Включает функции:
	- \_natural_logarithm - (Скрытая функция получение натурального логарифма) - принимает 2 параметра (массу полной и пустой ракеты, с типом float).
	- \_euler - (Скрытая функция расчет с помощью Эйлерова числа E) - принимает 1 параметр (общая скорость, с типом float).
	- total_speed - (Функция сумма всех скоростей) - принимает 2 параметра (натуральный логарифм и Isp, с типом float).
	- total_oil - (Функция для расчета топлива) - принимает 2 параметра (масса пустой ракеты и число эйлера, с типом float).

## Пример
```python
def total_speed(self):
	try:
		G = ACCELERATION_FREE_FALL
		nl = self._natural_logarithm()
		delta_V = self.Isp * G * nl
		log_info.info("Запуск функции 'total_speed'")
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return delta_V
```

## Пример логирования
```bash
2022-12-20 19:34:30 - format.py - root - Запуск класса 'RocketFormat'
2022-12-20 19:34:30 - format.py - root - Запуск класса 'FlightFormat'
2022-12-20 19:34:30 - format.py - root - Запуск класса 'LandingFormat'
2022-12-20 19:34:32 - rocket_flight_simulation.py - root - Включение импортов 'rocket_flight_simulation.py'
2022-12-20 19:34:32 - rocket_flight_simulation.py - root - Запуск класса 'CylindricalCavity'
2022-12-20 19:34:32 - rocket_flight_simulation.py - root - Запуск класса 'Resistance'
2022-12-20 19:34:32 - rocket_flight_simulation.py - root - Запуск класса 'Speed'
2022-12-20 19:34:32 - rocket_flight_simulation.py - root - Запуск класса 'ModelFlight'
2022-12-20 19:34:32 - rocket_fuel_calculation.py - root - Включение импортов 'rocket_fuel_calculation.py'
2022-12-20 19:34:32 - rocket_fuel_calculation.py - root - Запуск класса 'TotalOil'
2022-12-20 19:34:32 - rocket_flight_trajectory.py - root - Запуск класса 'FlightBallistics'
2022-12-20 19:34:32 - main.py - root - Импортирование файлов в main.py
2022-12-20 19:34:32 - main.py - root - Начало функции main
2022-12-20 19:34:33 - main.py - root - Запуск функции output_
2022-12-20 19:34:46 - main.py - root - Включение function_output
2022-12-20 19:34:46 - main.py - root - Включение функции 'fuel_input'
2022-12-20 19:34:58 - main.py - root - Пройден цикл = 1
2022-12-20 19:34:58 - rocket_fuel_calculation.py - root - Запуск функции '_natural_logarithm'
2022-12-20 19:34:58 - rocket_fuel_calculation.py - root - Запуск функции 'total_speed'
2022-12-20 19:34:58 - rocket_fuel_calculation.py - root - Запуск функции '_euler'
2022-12-20 19:34:58 - rocket_fuel_calculation.py - root - Запуск функции 'total_oil'
2022-12-20 19:34:58 - rocket_fuel_calculation.py - root - Запуск функции '_natural_logarithm'
2022-12-20 19:34:58 - rocket_fuel_calculation.py - root - Запуск функции 'total_speed'
2022-12-20 19:34:58 - format.py - root - Запуск функции 'main_rocket_format'
2022-12-20 19:34:58 - format.py - root - Запуск функции 'main_rocket_format'
```
