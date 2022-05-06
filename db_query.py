import sqlite3
from sqlite3 import Error

def create_connection(db_astro_file):
	""" create a db connection """
	conn = None

	try:
		conn = sqlite3.connect(db_astro_file)
	except Error as e:
		print(e)

	return conn


def select_all(conn):
	""" query all rows in the blow hair table """

	cur = conn.cursor()
	cur.execute("SELECT * FROM blowhair")

	rows = cur.fetchall()

	for row in rows:
		print(row)


core_id = input("Enter Core: ")

def user_query(conn, core_id):
	cur = conn.cursor()
	cur.execute("SELECT * FROM blowhair,densitytime WHERE blowhair.core=? AND densitytime.core=?", (core_id, core_id,))
	rows = cur.fetchall()
	for row in rows:
		print(row)

def main():

	database = "astro.db"

	conn = create_connection(database)
	with conn:
		print("Query all entries")
#		select_all(conn)

		print("Query by core: ")
		user_query(conn, core_id)

if __name__ == '__main__':
	main()
