import pytest


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
