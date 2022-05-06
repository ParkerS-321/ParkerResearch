import sqlite3
from sqlite3 import Error

def create_connection(db_astro_file):
	conn = None
	try:
		conn = sqlite3.connect(db_astro_file)
		return conn
	except Error as e:
		print(e)
	return conn

def create_table(conn, create_table_sql):
	""" create a table from the create_table_sql statement"""
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def main():
	database = "sim1.db"

	sql_create_blowhair_table = """ CREATE TABLE IF NOT EXISTS blowhair (
						id integer PRIMARY KEY,
						core integer NOT NULL,
						sim1_img BLOB
					); """

	sql_create_densitytime_table = """ CREATE TABLE IF NOT EXISTS densitytime (
						id integer PRIMARY KEY,
						core integer NOT NULL,
						sim1_img BLOB
					); """


	conn = create_connection(database)

	if conn is not None:
		create_table(conn, sql_create_densitytime_table)
		create_table(conn, sql_create_blowhair_table)
	else:
		print("Error! Cannot create the db connection.")

if __name__ == '__main__':
	main()
