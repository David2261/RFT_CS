import os
import sys

path = os.path.join(os.getcwd(), '../../RFTCS/')
sys.path.append(path)

import pytest
import numpy as np

from rocket_flight_simulation import (
	_body_area,
	resistance_force,
	frontal_area,
	environmental_resistance,
	resistance_force_env,
	gravity_losses,
	aerodynamic_losses,
	loss_speed_on_control
)
from rocket_fuel_calculation import total_speed


def data_rfs():
	height = 120.0
	width = 30.0
	speed = 2500.0
	array = (height, width, speed)
	return array


@pytest.mark.skip()
class TestMixinRFS:
	data = data_rfs()
	height = data[0]
	width = data[1]

	def test_isinstance(function, self):
		result = function(self.height, self.width)
		assert isinstance(result, (int, float))
	
	def test_type_error(function, height, width):
		with pytest.raises(TypeError):
			function('(17,', width)

	def test_more_args_error(function, height, width):
		with pytest.raises(TypeError):
			function(height, width, 23.1)

	def test_less_args_error(function, height, width):
		with pytest.raises(TypeError):
			function(height)

 


