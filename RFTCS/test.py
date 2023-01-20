from ctypes import *

trajectory = CDLL('./core/bin/Trajectory.so')

speed = 29000
sine = trajectory.double_angle_sine()
fr = trajectory.flight_range(sine, speed)
ft = trajectory.flight_time(speed)

print(f'Дальность полета = {fr}\nВремя полета = {ft}')
