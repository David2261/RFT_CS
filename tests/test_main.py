"""
Главный файл, где собранны все импорты.
"""
import os, sys

path = os.path.join(os.getcwd(), '../RFTCS/')
sys.path.append(path)

from test_format import TestRocketFormat, TestFlightFormat

TestRocketFormat()
TestFlightFormat()
