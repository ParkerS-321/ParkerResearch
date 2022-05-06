import sqlite3
from sqlite3 import Error

def create_connection(db_astro_file):
	""" create a database connection to a SQLite3 database """
	conn = None
	try:
		conn = sqlite3.connect(db_astro_file)
		print(sqlite3.version)
	except Error as e:
		print(e)
	finally:
		if conn:
			conn.close()

if __name__ == '__main__':
	create_connection("sim3.db")
