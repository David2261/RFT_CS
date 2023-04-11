#!/usr/bin/env python3
import sqlite3
import datetime

import logging
import logging.config

from setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")

try:
	from exceptions.exception import (
		invalid_entire,
		invalid_type,
		invalid_general,
		invalid_import
	)
except Exception as ex:
	logger.error(f"Ошибка с импортированием функкций исключений... {ex}")

# Bad request!!!
try:
	from config import path
	log_info.info("Импортирование файлов в databaseSQL.py")
except ImportError:
	from .config import path
except Exception as ex:
	logger.error(invalid_import(ex))
	raise invalid_import(ex)


class DataBaseSQL:
	""" Создание и добавление данных в БД """
	def __init__(self, table, arg_1, arg_2, arg_3=None):
		self.table = table
		self.arg_1 = arg_1
		self.arg_2 = arg_2
		self.arg_3 = arg_3

	try:
		sqlConnect = sqlite3.connect(path)
		cursor = sqlConnect.cursor()
		log_info.info("Подключение к БД SQL")
	except FileNotFoundError:
		logger.error(invalid_file(ex))
		raise FileNotFoundError(invalid_file(ex))
	except Exception as e:
		logger.error(invalid_general(ex))
		raise invalid_general(ex)

	def check_db_table(self):
		try:
			count_calculations = self.cursor.execute(
				"""SELECT name FROM sqlite_master
				WHERE type='table' AND name='%s';""" % self.table)
			res = True if count_calculations.fetchone() \
				is not None else False
			log_info.info("Проверка данных в БД SQL")
		except Exception as ex:
			logger.error(invalid_general(ex))
			raise invalid_general(ex)
		return res

	def create_db_table(self):
		try:
			if self.table == "ModelFlight":
				create_table = """
					CREATE TABLE IF NOT EXISTS ModelFlight (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					flow INTEGER,
					mass INTEGER,
					speed_0 INTEGER,
					Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);
				"""
			elif self.table == "FlightBallistics":
				create_table = """
					CREATE TABLE IF NOT EXISTS FlightBallistics (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					flight_range INTEGER,
					flight_time INTEGER,
					Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);
				"""
			elif self.table == "TotalOil":
				create_table = """
					CREATE TABLE IF NOT EXISTS TotalOil (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					speed INTEGER,
					oil INTEGER,
					Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);
				"""
			log_info.info("Создание таблиц в БД SQL")
		except Exception as ex:
			logger.error(invalid_general(ex))
			raise invalid_general(ex)
		self.cursor.execute(create_table)

	def insert_db(self):
		try:
			if self.table == "ModelFlight":
				query = """
				INSERT INTO ModelFlight
				(flow, mass, speed_0)
				VALUES (?, ?, ? );
				"""
				values = [(self.arg_1, self.arg_2, self.arg_3)]
			elif self.table == "FlightBallistics":
				query = """
				INSERT INTO FlightBallistics
				(flight_time, flight_range)
				VALUES (?, ? );
				"""
				values = [(self.arg_1, self.arg_2)]
			elif self.table == "TotalOil":
				query = """
				INSERT INTO TotalOil
				(speed, oil)
				VALUES (?, ? );
				"""
				values = [(self.arg_1, self.arg_2)]
			log_info.info("Ввод данных в БД SQL")
		except Exception as ex:
			logger.error(invalid_general(ex))
			raise invalid_general(ex)
		self.cursor.executemany(query, values)

	def record_data(self):
		try:
			if self.check_db_table():
				self.insert_db()
			else:
				self.create_db_table()
				self.insert_db()
		log_info.info("Основная функция записи данных в БД SQL")
		except Exception as ex:
			logger.error(invalid_general(ex))
			raise invalid_general(ex)
		self.sqlConnect.commit()
		self.cursor.close()


class ReadSQL:
	""" Чтение данных из БД """
	def __init__(self, table, size=None, item=None):
		self.table = table
		self.size = size
		self.item = item

	try:
		sqlConnect = sqlite3.connect(path)
		cursor = sqlConnect.cursor()
	except Exception as e:
		print(f"Bad request...\n{e}")

	def read_all_data(self):
		if self.table == "TotalOil":
			query = """SELECT * FROM TotalOil;"""
		elif self.table == "FlightBallistics":
			query = """SELECT * FROM FlightBallistics;"""
		elif self.table == "ModelFlight":
			query = """SELECT * FROM ModelFlight;"""
		res = self.cursor.execute(query)
		print(res.fetchall())
		self.cursor.close()

	def read_item_data(self):
		if self.table == "TotalOil":
			query = """SELECT * FROM TotalOil WHERE id = ?;"""
		elif self.table == "FlightBallistics":
			query = """SELECT * FROM FlightBallistics WHERE id = ?;"""
		elif self.table == "ModelFlight":
			query = """SELECT * FROM ModelFlight WHERE id = ?;"""
		res = self.cursor.execute(query, (self.item, ))
		print(res.fetchone())
		self.cursor.close()

	def read_many_data(self):
		if self.table == "TotalOil":
			query = """SELECT * FROM TotalOil;"""
		elif self.table == "FlightBallistics":
			query = """SELECT * FROM FlightBallistics;"""
		elif self.table == "ModelFlight":
			query = """SELECT * FROM ModelFlight;"""
		res = self.cursor.execute(query)
		print(res.fetchmany(self.size))
		self.cursor.close()


class PopSQL:
	""" Удаление данных из БД """
	def __init__(self, table, size=None, item=None):
		self.table = table
		self.item = item

	try:
		sqlConnect = sqlite3.connect(path)
		cursor = sqlConnect.cursor()
	except Exception as e:
		print(f"Bad request...\n{e}")

	def pop_data(self):
		try:
			if self.table == "TotalOil":
				query = """DELETE FROM TotalOil WHERE id = ?;"""
			elif self.table == "FlightBallistics":
				query = """DELETE FROM FlightBallistics WHERE id = ?;"""
			elif self.table == "ModelFlight":
				query = """DELETE FROM ModelFlight WHERE id = ?;"""
			self.cursor.execute(query, (self.item, ))
		except Exception as ex:
			print(f"Не получилось удалить запись...\n{ex}")
		self.cursor.close()

	def pop_last_data(self):
		try:
			if self.table == "TotalOil":
				query = """DELETE FROM TotalOil
					WHERE id = (SELECT MAX(id) FROM TotalOil);"""
			elif self.table == "FlightBallistics":
				query = """DELETE FROM FlightBallistics
					WHERE id = (SELECT MAX(id) FROM FlightBallistics);"""
			elif self.table == "ModelFlight":
				query = """DELETE FROM ModelFlight
					WHERE id = (SELECT MAX(id) FROM ModelFlight);"""
			self.cursor.execute(query)
		except Exception as ex:
			print(f"Не получилось удалить запись...\n{ex}")
		self.cursor.close()



if __name__ == "__main__":
	table = "ModelFlight"
	size = 2
	item = 2
	data = ReadSQL(table, size, item)
	data.read_many_data()


"""
Для примера (Из консоли - get all datas):


Напишите количество ступеней: 2
Какой формат вывода информации хотите?
В виде текста (1) или ввиде таблицы (2): 
2
+------+---------+--------+
| Fuel | Landing | Flight |
+------+---------+--------+
|  1   |    2    |   3    |
+------+---------+--------+
3
Напишите скорость ракеты: 450
Напишите расход ступени: 12
Напишите массу ракеты: 45
Время работы двигателя: 60
Напишите скорость ракеты: 23
Напишите расход ступени: 2
Напишите массу ракеты: 15
Время работы двигателя: 11.5
+------------------+----------+------+
| Amount of losses | Distance | Mass |
+------------------+----------+------+
|      12.93       | 5426.57  | 15.0 |
+------------------+----------+------+

SELECT COUNT(*) FROM sqlite_master; 4
SELECT COUNT(*) FROM ModelFlight; 1
SELECT COUNT(*) FROM TotalOil; 2
"""


"""
Для примера (Из консоли - get item data):

(1, 13.034366290892303, 7686.965633709107, 49, '2023-04-05 22:01:12')
(2, 12.930333693036495, 5426.569666306964, 15, '2023-04-05 22:05:21')

"""


"""
Для примера (Из консоли - get many datas):

[
(1, 13.034366290892303, 7686.965633709107, 49, '2023-04-05 22:01:12'),
(2, 12.930333693036495, 5426.569666306964, 15, '2023-04-05 22:05:21')
]

"""