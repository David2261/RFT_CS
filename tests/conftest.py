import pytest


@pytest.fixture(autouse=True)
def simulation_data():
	return [
		{
			id: 1,
			"flow": 15,
			"mass": 69,
			"speed_0": 360,
			"time": 4,
			"resistance": 6.434864717732359,
			"speed": 320.9329980000043,
			"distance": 11679.656463692852
		}
	]


