import sqlite3
import datetime

from config import path


class DataBase:
	def __init__(self, table):
		self.table = table

	try:
		sqlConnect = sqlite3.connect(path)
		cursor = sqlConnect.cursor()
	except Exception as e:
		print(f"Bad request...\n{e}")

	def check_table_db(self):
		count_calculations = self.cursor.execute(
			"""SELECT COUNT(*) FROM %s""", self.table)
		if 0 < count_calculations:
			res = True
		else:
			res = False
		return res

	def create_table_db(self):
		if self.table == "ModelFlight":
			self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS %s (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					flow INTEGER,
					mass INTEGER,
					speed_0 INTEGER,
					Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
				);
			""", self.table)
		elif self.table == "FlightBallistics":
			self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS %s (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					flight_range INTEGER,
					flight_time INTEGER,
					Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
				);
			""", self.table)
		elif self.table == "TotalOil":
			self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS %s (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					speed INTEGER,
					oil INTEGER,
					Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
				);
			""", self.table)
		else:
			print("Error")

	def main(self):
		if self.check_table_db():
			...
		else:
			self.create_table_db()
			self.sqlConnect.commit()
			self.cursor.close()

if __name__ == "__main__":
	table = "FlightBallistics"
	data = DataBase(table)
	data.main()

