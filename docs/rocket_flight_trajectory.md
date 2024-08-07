<p><a target="_blank" href="https://app.eraser.io/workspace/yFmi3ZY9GVWMUBRs9jCx" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# Расчет траектории полета ракеты
## Описание
_Определяет траекторию полёта ракеты._

## Импорты
- Импортируется библиотеки numpy и typing.
- Из файла _rocket_flight_simulation_ импортируется функция resistance_force_env, для расчета лобового сопротивления
- Из файла _rocket_fuel_calculation_ импортируется функция total_oil, для получения общего количества топлива в ракете
## Константы
- Ускорение свободного падения
    - 9.81
- Угол вектора тяги над горизонтом, градусов
    - 15
## Классы
- FlightBallistics (Класс для расчета траектории полета _внутри Земли_) - принимает 1 параметр (скорость, с типом float).
Включает функции:
    - _double_angle_sine (Скрытая функция расчета синуса двойного угла) - принимает 1 параметр и 1 константу (скорость ракеты и угол вектора тяги над горизонтом, с типом float), выводит число типа float.
    - flight_range (Функция дальности полета) - принимает 2 параметра и 2 константы (ускорение свободного полета, угол вектора тяги над горизонтом, синус двойного угла и скорость, с типом float), выводит число типа float.
    - flight_time (Функция время полета ракеты) - принимает 1 параметр и 2 константы (ускороние свободного полета, угол двойного угла и скорость, всё с типом float), выводит число типа float.




<!--- Eraser file: https://app.eraser.io/workspace/yFmi3ZY9GVWMUBRs9jCx --->