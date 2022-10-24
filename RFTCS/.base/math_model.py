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


def distance_N_step(U: int, n: int) -> float:
	r0 = INITIAL_DISTANCE
	r_n = r0 - n * U
	return float(r_n)


class CylindricalCavity:
	@classmethod
	def _cylindrical_cavity(U: int, n: int) -> float:
		R_0 = INITIAL_DISTANCE
		R_n = R_0 + n * U
		return R_n

	def volume_cylindrical_cavity(U: int, n: int, L: int) -> float:
		R_n = _cylindrical_cavity(U, n)
		V = mp.pi() * (R_n ** 2) * L
		return float(V)


class Fuel:
	def amount_unspent(U: int):
		P = FUEL_DENSITY
		m = U * P
		return m

	def change_mass(m_1: int, m_2: int) -> float:
		return m_1 - m_2







