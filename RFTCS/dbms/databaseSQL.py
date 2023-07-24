#!/usr/bin/env python3
import sqlite3
# import datetime

import logging
import logging.config

from RFTCS.setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")

try:
	from RFTCS.exceptions.exception import (
		invalid_general,
		invalid_import,
		invalid_file
	)
except Exception as ex:
	logger.error(f"Ошибка с импортированием функкций исключений... {ex}")

# Bad request!!!
try:
	from .config import path
	log_info.info("Импортирование файлов в databaseSQL.py")
except ImportError as ex:
	logger.error(invalid_import(ex))
	raise ex


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
		log_info.info("Подключение DataBaseSQL к БД SQL")
	except FileNotFoundError as ex:
		logger.error(invalid_file(ex))
		raise FileNotFoundError(invalid_file(ex))
	except Exception as ex:
		logger.error(invalid_general(ex))
		raise ex

	def check_db_table(self):
		try:
			count_calculations = self.cursor.execute(
				"""SELECT name FROM sqlite_master
				WHERE type='table' AND name='%s';""" % self.table)
			res = True if count_calculations.fetchone() \
				is not None else False
			log_info.info(f"Проверка данных в {self.table} БД SQL")
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
			log_info.info(f"Создание таблиц в БД SQL - {self.table}")
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
		log_info.info("Подключение ReadSQL к БД SQL")
	except FileNotFoundError as ex:
		logger.error(invalid_file(ex))
		raise FileNotFoundError(invalid_file(ex))
	except Exception as ex:
		logger.error(invalid_general(ex))
		raise ex

	def read_all_data(self):
		try:
			if self.table == "TotalOil":
				query = """SELECT * FROM TotalOil;"""
			elif self.table == "FlightBallistics":
				query = """SELECT * FROM FlightBallistics;"""
			elif self.table == "ModelFlight":
				query = """SELECT * FROM ModelFlight;"""
			res = self.cursor.execute(query)
			print(res.fetchall())
			log_info.info(f"Чтение данных из {self.table} в БД SQL")
		except Exception as ex:
			logger.error(invalid_general(ex))
			raise invalid_general(ex)
		self.cursor.close()

	def read_item_data(self):
		try:
			if self.table == "TotalOil":
				query = """SELECT * FROM TotalOil WHERE id = ?;"""
			elif self.table == "FlightBallistics":
				query = """SELECT * FROM FlightBallistics WHERE id = ?;"""
			elif self.table == "ModelFlight":
				query = """SELECT * FROM ModelFlight WHERE id = ?;"""
			res = self.cursor.execute(query, (self.item, ))
			print(res.fetchone())
			log_info.info(f"Чтение одной записи из {self.table} в БД SQL")
		except Exception as ex:
			logger.error(invalid_general(ex))
			raise invalid_general(ex)
		self.cursor.close()

	def read_many_data(self):
		try:
			if self.table == "TotalOil":
				query = """SELECT * FROM TotalOil;"""
			elif self.table == "FlightBallistics":
				query = """SELECT * FROM FlightBallistics;"""
			elif self.table == "ModelFlight":
				query = """SELECT * FROM ModelFlight;"""
			res = self.cursor.execute(query)
			print(res.fetchmany(self.size))
			log_info.info(f"Чтение нескольких записей \
				из {self.table} в БД SQL")
		except Exception as ex:
			logger.error(invalid_general(ex))
			raise invalid_general(ex)
		self.cursor.close()


class PopSQL:
	""" Удаление данных из БД """
	def __init__(self, table, item=None):
		self.table = table
		self.item = item

	try:
		sqlConnect = sqlite3.connect(path)
		cursor = sqlConnect.cursor()
		log_info.info("Подключение PopSQL к БД SQL")
	except FileNotFoundError as ex:
		logger.error(invalid_file(ex))
		raise FileNotFoundError(invalid_file(ex))
	except Exception as ex:
		logger.error(invalid_general(ex))
		raise ex

	def pop_data(self):
		try:
			if self.table == "TotalOil":
				query = """DELETE FROM TotalOil WHERE id = ?;"""
			elif self.table == "FlightBallistics":
				query = """DELETE FROM FlightBallistics WHERE id = ?;"""
			elif self.table == "ModelFlight":
				query = """DELETE FROM ModelFlight WHERE id = ?;"""
			self.cursor.execute(query, (self.item, ))
			log_info.info(f"Удаление одной записи из {self.table} в БД SQL")
		except Exception as ex:
			logger.error(invalid_general(ex))
			raise invalid_general(ex)
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
			log_info.info(f"Удаление последней записи\
				из {self.table} в БД SQL")
		except Exception as ex:
			logger.error(invalid_general(ex))
			raise invalid_general(ex)
		self.cursor.close()
