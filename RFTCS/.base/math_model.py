#!/usr/bin/env python
""" The Main formulas of mathematical modeling """
import numpy as np

from constant import (
	ATMOSPHERIC_PRESSURE,
	ATMOSPHERIC_DENSITY,
	ACCELERATION_FREE_FALL,
	CROSS_SECTION_AREA,
	VOLUME_EMPTY_CC
)


INITIAL_DISTANCE = 1.34
FUEL_DENSITY = 70.99
AVERAGE_MOLAR_MASS = 0.07
UNIVERSAL_GAS_CONSTANT = 8.314
BURNING_TEMPERATURE = 510


def distance_N_step(U: int, n: int) -> float:
	r0 = INITIAL_DISTANCE
	r_n = r0 - n * U
	return float(r_n)


class CylindricalCavity:
	def _cylindrical_cavity(U: int, n: int) -> float:
		R_0 = INITIAL_DISTANCE
		R_n = R_0 + n * U
		return R_n

	def volume_cylindrical_cavity(U: int, n: int, L: int):
		R_n = CylindricalCavity._cylindrical_cavity(U, n)
		V = np.pi * float((R_n ** 2) * L)
		return V


class Fuel:
	def amount_unspent(U: int):
		P = FUEL_DENSITY
		m = U * P
		return m

	def change_mass(m_1: int, m_2: int) -> float:
		return m_1 - m_2

def mass_rocket(m_empty_rocket: int, m_fuel_rocket: int) -> float:
	return float(m_empty_rocket + m_fuel_rocket)


def amount_gas_released(mass):
	amm = AVERAGE_MOLAR_MASS
	return float(mass / amm)


def overpressure(U) -> float:
	amm = AVERAGE_MOLAR_MASS
	ugc = UNIVERSAL_GAS_CONSTANT
	bt = BURNING_TEMPERATURE
	h = amm * ugc * bt
	return float(h / U)


def thrust_force(P_n: int):
	csa = CROSS_SECTION_AREA
	return float(P_n * csa)


def impuls(P_n, time):
	tf = thrust_force(P_n)
	return float(tf * time)


def height_rocket(h_n, u, t):
	return float(h_n + u * t)


if __name__ == '__main__':
	U = 9.5
	n = 3
	L = 223
	mass = 42500
	print(f"Расстояние от горящей поверхности топлива до стенки = {distance_N_step(U, n)}")
	print(f"Радиус внутренней цилидрической полости = {CylindricalCavity.volume_cylindrical_cavity(U, n, L)}")
	print(f"Объем внутренней цилиндрической полости = {Fuel.amount_unspent(U)}")
	print(f"Количество выделяемого газа за 1 моль = {amount_gas_released(mass)}")
	print(f"Избыточное давление в к.с. на n-шаге = {overpressure(U)}")
	print(f"Сила тяги = {thrust_force(overpressure(U))}")
	print(f"Импульс на n-шаге = {impuls(overpressure(U), n)}")
	print(f"Высота ракеты над стартовой площадкой = {height_rocket(2, U, n)}")

"""
Расстояние от горящей поверхности топлива до стенки = -27.16
Радиус внутренней цилидрической полости = 623810.0587468073
Объем внутренней цилиндрической полости = 674.405
Количество выделяемого газа за 1 моль = 607142.857142857
Избыточное давление в к.с. на n-шаге = 31.24313684210527
Сила тяги = 0.03124313684210527
Импульс на n-шаге = 0.09372941052631581
Высота ракеты над стартовой площадкой = 30.5
"""
