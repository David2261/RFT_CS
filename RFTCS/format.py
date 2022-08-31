"""
В этом файле собраны все способы форматирования результатов
"""


class RocketFormat:
	def _rocket_total_speed(num: float) -> str:
		return f"Сумма всех скоростей = {str(num)} м/с"

	def _rocket_natural_logarithm(num: float) -> str:
		return f"Натуральный логарифм = {str(num)}"

	def _rocket_massa_construction(num: float) -> str:
		return f"Сумма всей конструкции ракеты = {str(num)} кг"

	def _rocket_total_oil(num: float) -> str:
		return f"Сумма всего топлива = {str(num)} кг"


class FlightFormat:
	def _flight_resistance_force(num: float) -> str:
		return f"Сила сопротивления = {num} м/с^2"

