import os
import sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

import pytest
import numpy as np

from main import (
	output_info,
	fuel_input,
	flight_model_input,
	function_output
)




class TestFlightModel:
	"""Тест для ввода моделирование полета"""
	stage = 1
	height = 120
	width = 15
	speed = 450
	etf = 2080
	mass = 550
	gamma = 1.2
	fad = 0.04
	time = 650

	def test_flight_model_input(self):
		res = flight_model_input(
			self.stage)
		assert res



