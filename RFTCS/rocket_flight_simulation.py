#!/usr/bin/env python3
"""
В данном файле производиться математическое моделирование полета ракеты.
Основные формулы:
	- Эллептическое расстояние полета ракеты
	- Общее сопротивление
	- Общая скорость
"""
from __future__ import annotations

import numpy as np
# import numpy.typing as npt
import logging
import logging.config
from typing import (
	Any,
	Union
)

from .exceptions.exception import (
	invalid_import,
	invalid_type,
	invalid_zero_division,
	invalid_general,
	invalid_IO
)
from .setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")

try:
	from .setup.constant import (
		ATMOSPHERIC_DENSITY,
		ACCELERATION_FREE_FALL,
		CROSS_SECTION_AREA,
		UNIVERSAL_GAS_CONSTANT,
		EARTH_RADIUS,
	)
	from .setup.settings import (
		INITIAL_DISTANCE,
		AVERAGE_MOLAR_MASS,
		BURNING_TEMPERATURE,
		FPV,
		TVV,
		BEGIN_RADIUS_ROCKET,
	)

	log_info.info("Включение импортов 'rocket_flight_simulation.py'")
except ImportError as e:
	logger.error(invalid_import(e))
	raise ImportError(invalid_import(e))


def distance_N_step(
			fuelFlow: Union[int, float],
			n: Union[int, float]) -> Union[int, float]:
	""" Расстояние от горящей поверхности топлива до стенки камеры сгорания """
	try:
		r0 = INITIAL_DISTANCE
		r_n = r0 - n * fuelFlow
		log_info.info("Запуск функции 'distance_N_step'")
	except TypeError as te:
		logger.error(invalid_type(te))
		raise TypeError(invalid_type(te))
	return float(r_n)


def tg_Beta(spd: Union[int, float]) -> Any:
	""" Угол полета ракеты относительно поверности земли """
	try:
		log_info.info("Запуск функции 'tg_Beta'")
		start = BEGIN_RADIUS_ROCKET
		v = (spd * start) / 398_621
		corn = v / (2 * np.sqrt(abs(1 - v)))
	except TypeError as te:
		logger.error(invalid_type(te))
		raise TypeError(invalid_type(te))
	except ZeroDivisionError as zde:
		logger.error(invalid_zero_division(zde))
		raise ZeroDivisionError(invalid_zero_division(zde))
	return corn


def elliptical_range(speed: Union[int, float]) -> Any:
	""" Эллиптическая дальность полета """
	try:
		log_info.info("Запуск функции 'elliptical_range'")
		R = EARTH_RADIUS
		Tang = tg_Beta(speed)
		L = 2 * R * np.arctan(Tang)
	except TypeError as te:
		logger.error(invalid_type(te))
		raise TypeError(invalid_type(te))
	except IOError as io:
		logger.error(invalid_IO(io))
		raise IOError(invalid_IO(io))
	return L


def mass_rocket(
			m_empty_rocket: Union[int, float],
			m_fuel_rocket: Union[int, float]) -> Union[int, float]:
	""" Масса всей ракеты """
	try:
		log_info.info("Запуск функции 'mass_rocket'")
		res = float(m_empty_rocket + m_fuel_rocket)
	except TypeError as te:
		logger.error(invalid_type(te))
		raise TypeError(invalid_type(te))
	return res


def amount_gas_released(mass: Union[int, float]) -> Union[int, float]:
	""" Количество выделяемого газа за 1 моль """
	try:
		log_info.info("Запуск функции 'amount_gas_released'")
		amm = AVERAGE_MOLAR_MASS
		res = float(mass / amm)
	except TypeError as te:
		logger.error(invalid_type(te))
		raise TypeError(invalid_type(te))
	except ZeroDivisionError as zde:
		logger.error(invalid_zero_division(zde))
		raise ZeroDivisionError(invalid_zero_division(zde))
	return res


def overpressure(U: Union[int, float]) -> Union[int, float]:
	""" Избыточное давление в камере сгорания на n-шаге """
	try:
		log_info.info("Запуск функции 'overpressure'")
		amm = AVERAGE_MOLAR_MASS
		ugc = UNIVERSAL_GAS_CONSTANT
		bt = BURNING_TEMPERATURE
		h = amm * ugc * bt
		res = float(h / U)
	except TypeError as te:
		logger.error(invalid_type(te))
		raise TypeError(invalid_type(te))
	except ZeroDivisionError as zde:
		logger.error(invalid_zero_division(zde))
		raise ZeroDivisionError(invalid_zero_division(zde))
	return res


def thrust_force(P_n: Union[int, float]) -> Union[int, float]:
	""" Сила выталкивания (тяги) газов через сопло """
	try:
		log_info.info("Запуск функции 'thrust_force'")
		res = float(P_n) * float(CROSS_SECTION_AREA)
	except TypeError as te:
		logger.error(invalid_type(te))
		raise TypeError(invalid_type(te))
	return res


def impuls(
			P_n: Union[int, float],
			time: Union[int, float]) -> Union[int, float]:
	""" Импульс, сообщаемого ракете на n-шаге """
	try:
		log_info.info("Запуск функции 'impuls'")
		tf = thrust_force(P_n)
		res = tf * float(time)
	except TypeError as te:
		logger.error(invalid_type(te))
		raise TypeError(invalid_type(te))
	return res


def height_rocket(
			h_n: Union[int, float],
			u: Union[int, float],
			t: Union[int, float]) -> Union[int, float]:
	""" Высота ракеты над стартовой площадкой """
	try:
		log_info.info("Запуск функции 'height_rocket'")
		res = float(h_n) + float(u) * float(t)
	except TypeError as te:
		logger.error(invalid_type(te))
		raise TypeError(invalid_type(te))
	return res


class CylindricalCavity:
	"""Расчет объема внутренней цилиндрической полости"""

	log_info.info("Запуск класса 'CylindricalCavity'")

	def __init__(
				self,
				speed_burning_fuel: Union[float, int],
				step: int,
				Long: float) -> None:
		self.U = speed_burning_fuel
		self.n = step
		self.L = Long

	@staticmethod
	def _cylindrical_cavity(n: int, U: Union[float, int]) -> float:
		""" Радиус внутренней цилиндрической полости, м """
		try:
			log_info.info("Запуск функции '_cylindrical_cavity'")
			R_0 = INITIAL_DISTANCE
			R_n = R_0 + n * U
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		return float(R_n)

	def volume_cylindrical_cavity(self):
		""" Объем цилиндрической полости, м^3 """
		try:
			log_info.info("Запуск функции 'volume_cylindrical_cavity'")
			R_n = self._cylindrical_cavity(self.n, self.U)
			V = np.pi * float((pow(R_n, 2)) * self.L)
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		return V


class Resistance:
	log_info.info("Запуск класса 'Resistance'")
	""" Сопротивление """

	def __init__(self, speed: float, tf: float, mass: float) -> None:
		self.V = speed
		self.thrust_force = tf
		self.mass = mass

	def _aerodynamic_pressure(self):
		""" Аэродинамический напор, км/ч """
		try:
			log_info.info("Запуск функции '_aerodynamic_pressure'")
			AD = ATMOSPHERIC_DENSITY
			speed = self.V
			res = (AD * (pow(speed, 2))) / 2
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except ZeroDivisionError as zde:
			logger.error(invalid_zero_division(zde))
			raise ZeroDivisionError(invalid_zero_division(zde))
		return res

	def aerodynamic_drag(self):
		""" Аэродинамическое сопротивление, км/ч """
		try:
			log_info.info("Запуск функции 'aerodynamic_drag'")
			Cx = CROSS_SECTION_AREA
			S = Cx
			Q = self._aerodynamic_pressure()
			res = Cx * S * Q
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		return res

	def gravitation_losses(self):
		""" Гравитационные потери, км/ч """
		try:
			log_info.info("Запуск функции 'gravitation_losses'")
			G = ACCELERATION_FREE_FALL
			angel = np.sin(FPV)
			res = G * angel
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		return res

	def control_losses(self):
		""" Потеря скорости на управление, км/ч """
		try:
			log_info.info("Запуск функции 'control_losses'")
			angel = 1 - np.cos(TVV)
			res = (self.thrust_force / self.mass) * angel
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except ZeroDivisionError as zde:
			logger.error(invalid_zero_division(zde))
			raise ZeroDivisionError(invalid_zero_division(zde))
		return res


class Speed:
	log_info.info("Запуск класса 'Speed'")
	""" Скорость """

	def __init__(
				self,
				tf: Union[int, float],
				gl: Union[int, float],
				m: Union[int, float],
				time: Union[int, float],
				speed_0: Union[int, float]) -> None:
		self.thrust_force = tf
		self.gravitation_losses = gl
		self.mass = m
		self.time = time
		self.speed_0 = speed_0

	def _resultant_force(self):
		""" Равнодействующая сила """
		try:
			log_info.info("Запуск функции '_resultant_force'")
			G = ACCELERATION_FREE_FALL
			res = thrust_force(self.speed_0) * self.gravitation_losses - self.mass * G
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		return res

	def rocket_acceleration(self):
		""" Ускорение ракеты """
		try:
			log_info.info("Запуск функции 'rocket_acceleration'")
			F = self._resultant_force()
			res = F / self.mass
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		except ZeroDivisionError as zde:
			logger.error(invalid_zero_division(zde))
			raise ZeroDivisionError(invalid_zero_division(zde))
		return res

	def rocket_speed(self):
		""" Скорость ракеты, км/ч """
		try:
			log_info.info("Запуск функции 'rocket_speed'")
			a = self.rocket_acceleration()
			res = self.speed_0 + a * self.time
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		return res


class ModelFlight:
	log_info.info("Запуск класса 'ModelFlight'")
	""" Моделирование полета """

	def __init__(
				self,
				fuel_flow: float,
				mass: float,
				speed_0: float,
				time: float) -> None:
		self.mass = mass
		self.speed_0 = speed_0
		self.time = time
		self.fuel_flow = fuel_flow

	def _total_resistance(self):
		""" Общее сопротивление, км/ч """
		try:
			log_info.info("Запуск функции '_total_resistance'")
			speed = self._total_speed()
			tf = thrust_force(self.fuel_flow)
			resistance = Resistance(speed, tf, self.mass)
			cont = resistance.control_losses()
			gl = resistance.gravitation_losses()
			ad = resistance.aerodynamic_drag()
			res = cont + gl + ad
		except TypeError as te:
			logger.error(invalid_type(te))
			raise TypeError(invalid_type(te))
		return res

	def _total_speed(self):
		""" Общая скорость, км/ч """
		try:
			log_info.info("Запуск функции '_total_speed'")
			tf = thrust_force(self.fuel_flow)
			resistance = Resistance(self.speed_0, tf, self.mass)
			gl = resistance.gravitation_losses()
			spd = Speed(tf, gl, self.mass, self.time, self.speed_0)
			speed = spd.rocket_speed()
		except Exception as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)
		return speed

	def _total_distance(self) -> float:
		""" Общее расстояние, км """
		try:
			log_info.info("Запуск функции '_total_distance'")
			speed = self._total_speed()
			res = elliptical_range(speed)
		except Exception as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)  # type: ignore[misc]
		return float(res)

	def model_stack(self) -> list:
		try:
			log_info.info("Запуск функции 'model_stack'")
			resistance = self._total_resistance()
			speed = self._total_speed()
			distance = self._total_distance()
			Beta = tg_Beta(speed)
		except Exception as e:
			logger.error(invalid_general(e))
			raise invalid_general(e)  # type: ignore[misc]
		return [resistance, speed, distance, Beta]


if __name__ == "__main__":
	flow = 15
	mass = 69
	speed_0 = 360
	time = 4
	m = ModelFlight(flow, mass, speed_0, time)
	stack = m.model_stack()
	for i in range(3):
		print(stack[i])
# 6.434864717732359
# 320.9329980000043
# 11679.656463692852
