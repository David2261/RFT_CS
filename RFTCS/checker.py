import timeit


code_to_test = """
from rocket_flight_simulation import ModelFlight

flow = 15
mass = 69
speed_0 = 360
time = 4
m = ModelFlight(flow, mass, speed_0, time)
stack = m.model_stack()
for i in range(3):
	stack[i]

from rocket_flight_trajectory import FlightBallistics

speed = 36500
b = FlightBallistics(speed)
b.flight_range()
b.flight_time()

from rocket_fuel_calculation import TotalOil

Me = 524
Mf = 579
Isp = 4200
a = TotalOil(Me, Mf, Isp)
a.total_speed()
a.total_oil()
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)