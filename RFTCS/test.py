from ctypes import *

trajectory = CDLL('./core/bin/Trajectory.so')

speed = 29000
sine = trajectory.api_double_angle_sine()
fr = trajectory.api_flight_range(sine, speed)
# ft = trajectory.api_flight_time(speed)

print(fr)
# print(f'Дальность полета = {fr}\nВремя полета = {ft}')
