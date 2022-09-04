"""
Главный файл, где собранны все импорты.
"""
import os, sys
from pathlib import *

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)
import unittest

from rocket_flight_simulation import *
from rocket_fuel_calculation import *


