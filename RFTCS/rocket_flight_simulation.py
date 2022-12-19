#!/usr/bin/env python3
"""
В данном файле производиться математическое моделирование полета ракеты.
Основные формулы:
	- Эллептическое расстояние полета ракеты
	- Общее сопротивление
	- Общая скорость
"""
import sys
import numpy as np
import logging
import logging.config

from exceptions.exception import *
from setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")

try:
	from setup.constant import (
		ATMOSPHERIC_PRESSURE,
		ATMOSPHERIC_DENSITY,
		ACCELERATION_FREE_FALL,
		CROSS_SECTION_AREA,
		VOLUME_EMPTY_CC,
		UNIVERSAL_GAS_CONSTANT,
		EARTH_RADIUS
	)
	from setup.settings import (
		INITIAL_DISTANCE,
		FUEL_DENSITY,
		AVERAGE_MOLAR_MASS,
		BURNING_TEMPERATURE,
		FPV,
		TVV,
		BEGIN_RADIUS_ROCKET
	)
	log_info.info("Включение импортов 'rocket_flight_simulation.py'")
except ImportError as e:
	logger.error(invalid_import(e))
	sys.exit(1)


""" Расстояние от горящей поверхности топлива до стенки камеры сгорания. """
def distance_N_step(U: int, n: int) -> float:
	try:
		r0 = INITIAL_DISTANCE
		r_n = r0 - n * U
		log_info.info("Запуск функции 'distance_N_step'")
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return float(r_n)



def tg_Beta(speed: int):
	try:
		log_info.info("Запуск функции 'tg_Beta'")
		R = EARTH_RADIUS
		v = (speed ** 2 * BEGIN_RADIUS_ROCKET) / 398_621
		tg_Beta = v / (2 * np.sqrt(1-v))
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return tg_Beta

""" Эллиптическая дальность полета """
def elliptical_range(speed: int) -> float:
	try:
		log_info.info("Запуск функции 'elliptical_range'")
		R = EARTH_RADIUS
		L = 2 * R * np.arctan(tg_Beta)
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return L


""" Масса всей ракеты """
def mass_rocket(m_empty_rocket: int, m_fuel_rocket: int) -> float:
	try:
		log_info.info("Запуск функции 'mass_rocket'")
		res = float(m_empty_rocket + m_fuel_rocket)
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return res


""" Количество выделяемого газа за 1 моль """
def amount_gas_released(mass: int) -> float:
	try:
		log_info.info("Запуск функции 'amount_gas_released'")
		amm = AVERAGE_MOLAR_MASS
		res = float(mass / amm)
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return res


""" Избыточное давление в камере сгорания на n-шаге """
def overpressure(U) -> float:
	try:
		log_info.info("Запуск функции 'overpressure'")
		amm = AVERAGE_MOLAR_MASS
		ugc = UNIVERSAL_GAS_CONSTANT
		bt = BURNING_TEMPERATURE
		h = amm * ugc * bt
		res =  float(h / U)
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return res


""" Сила выталкивания (тяги) газов через сопло """
def thrust_force(P_n: float):
	try:
		log_info.info("Запуск функции 'thrust_force'")
		csa = CROSS_SECTION_AREA
		res = P_n * csa
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return res


""" Импульс, сообщаемого ракете на n-шаге """
def impuls(P_n, time):
	try:
		log_info.info("Запуск функции 'impuls'")
		tf = thrust_force(P_n)
		res =  float(tf * time)
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return res


""" Высота ракеты над стартовой площадкой """
def height_rocket(h_n, u, t):
	try:
		log_info.info("Запуск функции 'height_rocket'")
		res = float(h_n + u * t)
	except Exception as e:
		logger.error(e)
		sys.exit(1)
	return res


class CylindricalCavity:
	""" Расчет объема внутренней цилиндрической полости """
	log_info.info("Запуск класса 'CylindricalCavity'")
	def __init__(self, speed_burning_fuel: int, step: int, Long: int):
		self.U = speed_burning_fuel
		self.n = step
		self.L = Long

	@classmethod
	# Радиус внутренней цилиндрической полости
	def _cylindrical_cavity(cls) -> float:
		try:
			log_info.info("Запуск функции '_cylindrical_cavity'")
			R_0 = INITIAL_DISTANCE
			R_n = R_0 + cls.n * cls.U
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return R_n

	# Объем цилиндрической полости
	def volume_cylindrical_cavity(self):
		try:
			log_info.info("Запуск функции 'volume_cylindrical_cavity'")
			R_n = self._cylindrical_cavity()
			V = np.pi * float((R_n ** 2) * self.L)
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return V


class Resistance:
	log_info.info("Запуск класса 'Resistance'")
	""" Сопротивление """
	def __init__(self, speed: int, tf: int, mass: int):
		self.V = speed
		self.thrust_force = tf
		self.mass = mass

	@classmethod
	# Аэродинамический напор
	def _aerodynamic_pressure(cls):
		try:
			log_info.info("Запуск функции '_aerodynamic_pressure'")
			AD = ATMOSPHERIC_DENSITY
			res = (AD * (cls.V ** 2)) / 2
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res

	""" Аэродинамическое сопротивление """
	def aerodynamic_drag(self):
		try:
			log_info.info("Запуск функции 'aerodynamic_drag'")
			Cx = CROSS_SECTION_AREA
			S = Cx
			Q = self._aerodynamic_pressure()
			res = Cx * S * Q
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res

	""" Гравитационные потери """
	def gravitation_losses(self):
		try:
			log_info.info("Запуск функции 'gravitation_losses'")
			G = ACCELERATION_FREE_FALL
			angel = np.sin(FPV)
			res = G * angel
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res

	""" Потеря скорости на управление """
	def control_losses(self):
		try:
			log_info.info("Запуск функции 'control_losses'")
			angel = 1 - np.cos(TVV)
			res = (self.thrust_force / self.mass) * angel
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res


class Speed:
	log_info.info("Запуск класса 'Speed'")
	""" Скорость """
	def __init__(self, tf, gl, m, time, speed_0):
		self.thrust_force = tf
		self.gravitation_losses = gl
		self.mass = m
		self.time = time
		self.speed_0 = speed_0

	@classmethod
	# Равнодействующая сила
	def _resultant_force(cls):
		try:
			log_info.info("Запуск функции '_resultant_force'")
			G = ACCELERATION_FREE_FALL
			res = cls.thrust_force * cls.gravitation_losses - cls.mass * G
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res

	# Ускорение ракеты
	def rocket_acceleration(self):
		try:
			log_info.info("Запуск функции 'rocket_acceleration'")
			F = self._resultant_force()
			res = F / self.mass
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res

	def rocket_speed(self):
		try:
			log_info.info("Запуск функции 'rocket_speed'")
			a = self.rocket_acceleration()
			res = self.speed_0 + a * self.time
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res

class ModelFlight:
	log_info.info("Запуск класса 'ModelFlight'")
	""" Моделирование полета """
	def __init__(self, fuel_flow: float, mass: float, speed_0: float, time: int):
		self.mass = mass
		self.speed_0 = speed_0
		self.time = time
		self.tf = thrust_force(fuel_flow)

	# Общее сопротивление
	@classmethod
	def _total_resistance(cls):
		try:
			log_info.info("Запуск функции '_total_resistance'")
			speed = cls._total_speed()
			resistance = Resistance(speed, cls.tf, cls.mass)
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return resistance

	# Общая скорость
	@classmethod
	def _total_speed(cls):
		try:
			log_info.info("Запуск функции '_total_speed'")
			resistance = Resistance(cls.speed_0, cls.tf, cls.mass)
			gl = resistance.gravitation_losses()
			speed = Speed(cls.tf, gl, cls.mass, cls.time, cls.speed_0)
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return speed

	# Общее расстояние
	@classmethod
	def _total_distance(cls) -> float:
		try:
			log_info.info("Запуск функции '_total_distance'")
			speed = cls._total_speed()
			res = elliptical_range(speed)
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return res

	def model_stack(self) -> list:
		try:
			log_info.info("Запуск функции 'model_stack'")
			resistance = self._total_resistance
			speed = self._total_speed
			distance = self._total_distance
			Beta = tg_Beta(speed)
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		return [resistance, speed, distance, Beta]
