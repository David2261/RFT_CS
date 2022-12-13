#!/usr/bin/env python
""" The Main formulas of mathematical modeling """
import logging
import numpy as np

from setup.constant import (
	ATMOSPHERIC_PRESSURE,
	ATMOSPHERIC_DENSITY,
	ACCELERATION_FREE_FALL,
	CROSS_SECTION_AREA,
	VOLUME_EMPTY_CC,
	UNIVERSAL_GAS_CONSTANT
)
from setup.settings import (
	INITIAL_DISTANCE,
	FUEL_DENSITY,
	AVERAGE_MOLAR_MASS,
	BURNING_TEMPERATURE,
	FPV,
	TVV
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



""" Масса всей ракеты """
def mass_rocket(m_empty_rocket: int, m_fuel_rocket: int) -> float:
	return float(m_empty_rocket + m_fuel_rocket)


""" Количество выделяемого газа за 1 моль """
def amount_gas_released(mass):
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
def thrust_force(P_n: int):
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
		R_n = R_0 + n * U
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
		return (AD * (V ** 2)) / 2

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
	def __init__(self, tf, gr, m, time, speed_0):
		self.thrust_force = tf
		self.gravitation_losses = gr
		self.mass = m
		self.time = time
		self.speed_0 = speed_0

	@classmethod
	# Равнодействующая сила
	def _resultant_force(cls):
		G = ACCELERATION_FREE_FALL
		return (self.thrust_force * self.gravitation_losses - self.mass * G)

	def rocket_acceleration(self):
		F = _resultant_force()
		return F / self.mass

	def rocket_speed(self):
		a = rocket_acceleration()
		return speed_0 + a * self.time

