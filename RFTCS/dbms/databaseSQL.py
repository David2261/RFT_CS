import sqlite3
import datetime

from config import path


class DataBase:
	def __init__(self, table, arg_1, arg_2, arg_3=None):
		self.table = table
		self.arg_1 = arg_1
		self.arg_2 = arg_2
		self.arg_3 = arg_3

	try:
		sqlConnect = sqlite3.connect(path)
		cursor = sqlConnect.cursor()
	except Exception as e:
		print(f"Bad request...\n{e}")

	def check_table_db(self):
		count_calculations = self.cursor.execute(
			"""SELECT name FROM sqlite_master WHERE type='table' AND name='%s' """ % self.table)
		if count_calculations.fetchone() is not None:
			res = True
		else:
			res = False
		return res

	def create_table_db(self):
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
		else:
			print("Error")
		self.cursor.execute(create_table)

	def insert_db(self):
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
		self.cursor.executemany(query, values)

	def main(self):
		if self.check_table_db():
			self.insert_db()
		else:
			self.create_table_db()
			self.insert_db()
		self.sqlConnect.commit()
		self.cursor.close()

if __name__ == "__main__":
	table = "TotalOil"
	arg_1 = 473
	arg_2 = 14
	arg_3 = 450
	data = DataBase(table, arg_1, arg_2, arg_3)
	data.main()



"""
Для примера (Из консоли):


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