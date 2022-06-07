import glob
import re
import sqlite3
from sqlite3 import Error
import pdb

def convertToBinary(filename):
	with open(filename, 'rb') as file:
		blobData = file.read()
	return blobData

def create_connection(sim_name):
	conn = None
	try:
		conn =  sqlite3.connect(sim_name)
		return conn
	except Error as e:
		print (e)
	return conn

def create_table(conn, create_table_sql):
	""" create a table from the create_table_sql statement"""
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def create_entry(conn, insert_sql, entry):
	""" Create a new entry in {} table """

	cur = conn.cursor()
	
	cur.executemany(insert_sql,entry)
	
	conn.commit()



class Product():
	def __init__(self, name, regexp):
		self.name = name
		self.regexp = regexp
		self.file_list = []
		self.blob_list = []
		self.core_list = []
		self.table_descriptor = """ CREATE TABLE IF NOT EXISTS {} (
						id integer PRIMARY KEY,
						core integer NOT NULL,
						product BLOB
					);""".format(self.name)
		
		self.insert_descriptor = """ INSERT INTO {} (core, product)
						VALUES (?,?) """.format(self.name)	


	def get_files(self, all_files=None):
		if all_files is None:
			all_files = glob.glob("**", recursive=True)
		
		for file in all_files:
			match = re.compile(self.regexp).match(file)
			if match:
				self.file_list.append(file)
				core = match.group(2)
				self.core_list.append(core)	
				found = match
		
		for file in self.file_list:
			self.blob_list.append(convertToBinary(file))
		combined_data = tuple(zip(self.core_list,self.blob_list))
		return combined_data

def readProductList(control_file):
	product_list = []
	with open(control_file) as file:
		for line in file:
			strs = [str(i) for i in line.strip().split(',') if i]
			product_list.append( Product(strs[0], strs[1]) )
	return product_list				

			

if __name__ =='__main__':

	list_of_product_objects = readProductList("control_sim1.txt")
	all_files = glob.glob("**", recursive=True)
	conn = create_connection('simulation1.db')
	for product in list_of_product_objects:
		p = product.get_files(all_files=all_files)
		create_table(conn, product.table_descriptor)
		create_entry(conn, product.insert_descriptor, p)


