#!/usr/bin/env python3
"""
В данном файле производиться математическое моделирование полета ракеты.
Основные формулы:
	- Эллептическое расстояние полета ракеты
	- Общее сопротивление
	- Общая скорость
"""
import logging
import numpy as np

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
from exceptions import logger


log = logger.get_logger(__name__)


""" Расстояние от горящей поверхности топлива до стенки камеры сгорания. """
def distance_N_step(U: int, n: int) -> float:
	try:
		r0 = INITIAL_DISTANCE
		r_n = r0 - n * U
		return float(r_n)
	except Exception as e:
		log.error("Value error")
		raise ValueError("Некорректные данные!!!")


def tg_Beta(speed: int):
	R = EARTH_RADIUS
	v = (speed ** 2 * BEGIN_RADIUS_ROCKET) / 398_621
	tg_Beta = v / (2 * np.sqrt(1-v))
	return tg_Beta

""" Эллиптическая дальность полета """
def elliptical_range(speed: int) -> float:
	R = EARTH_RADIUS
	L = 2 * R * np.arctan(tg_Beta)
	return L


""" Масса всей ракеты """
def mass_rocket(m_empty_rocket: int, m_fuel_rocket: int) -> float:
	return float(m_empty_rocket + m_fuel_rocket)


""" Количество выделяемого газа за 1 моль """
def amount_gas_released(mass: int) -> float:
	amm = AVERAGE_MOLAR_MASS
	return float(mass / amm)


""" Избыточное давление в камере сгорания на n-шаге """
def overpressure(U) -> float:
	amm = AVERAGE_MOLAR_MASS
	ugc = UNIVERSAL_GAS_CONSTANT
	bt = BURNING_TEMPERATURE
	h = amm * ugc * bt
	return float(h / U)


""" Сила выталкивания (тяги) газов через сопло """
def thrust_force(P_n: float):
	csa = CROSS_SECTION_AREA
	return P_n * csa


""" Импульс, сообщаемого ракете на n-шаге """
def impuls(P_n, time):
	tf = thrust_force(P_n)
	return float(tf * time)


""" Высота ракеты над стартовой площадкой """
def height_rocket(h_n, u, t):
	return float(h_n + u * t)


class CylindricalCavity:
	""" Расчет объема внутренней цилиндрической полости """
	def __init__(self, speed_burning_fuel: int, step: int, Long: int):
		self.U = speed_burning_fuel
		self.n = step
		self.L = Long

	@classmethod
	# Радиус внутренней цилиндрической полости
	def _cylindrical_cavity(cls) -> float:
		R_0 = INITIAL_DISTANCE
		R_n = R_0 + cls.n * cls.U
		return R_n

	# Объем цилиндрической полости
	def volume_cylindrical_cavity(self):
		R_n = self._cylindrical_cavity()
		V = np.pi * float((R_n ** 2) * self.L)
		return V


class Resistance:
	""" Сопротивление """
	def __init__(self, speed: int, tf: int, mass: int):
		self.V = speed
		self.thrust_force = tf
		self.mass = mass

	@classmethod
	# Аэродинамический напор
	def _aerodynamic_pressure(cls):
		AD = ATMOSPHERIC_DENSITY
		return (AD * (cls.V ** 2)) / 2

	""" Аэродинамическое сопротивление """
	def aerodynamic_drag(self):
		Cx = CROSS_SECTION_AREA
		S = Cx
		Q = self._aerodynamic_pressure()
		return Cx * S * Q

	""" Гравитационные потери """
	def gravitation_losses(self):
		G = ACCELERATION_FREE_FALL
		angel = np.sin(FPV)
		return G * angel

	""" Потеря скорости на управление """
	def control_losses(self):
		angel = 1 - np.cos(TVV)
		return (self.thrust_force / self.mass) * angel


class Speed:
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
		G = ACCELERATION_FREE_FALL
		return (cls.thrust_force * cls.gravitation_losses - cls.mass * G)

	# Ускорение ракеты
	def rocket_acceleration(self):
		F = self._resultant_force()
		return F / self.mass

	def rocket_speed(self):
		a = self.rocket_acceleration()
		return self.speed_0 + a * self.time

class ModelFlight:
	""" Моделирование полета """
	def __init__(self, fuel_flow: float, mass: float, speed_0: float, time: int):
		self.mass = mass
		self.speed_0 = speed_0
		self.time = time
		self.tf = thrust_force(fuel_flow)

	# Общее сопротивление
	@classmethod
	def _total_resistance(cls):
		speed = cls._total_speed()
		resistance = Resistance(speed, cls.tf, cls.mass)

	# Общая скорость
	@classmethod
	def _total_speed(cls):
		resistance = Resistance(cls.speed_0, cls.tf, cls.mass)
		gl = resistance.gravitation_losses()
		speed = Speed(cls.tf, gl, cls.mass, cls.time, cls.speed_0)

	# Общее расстояние
	@classmethod
	def _total_distance(cls) -> float:
		speed = cls._total_speed()
		elliptical_range(speed)
		return elliptical_range

	def model_stack(self) -> list:
		resistance = self._total_resistance
		speed = self._total_speed
		distance = self._total_distance
		Beta = tg_Beta(speed)
		return [resistance, speed, distance, Beta]
