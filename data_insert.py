import glob
import re
import sqlite3
from sqlite3 import Error
import h5py
import pdb
import fnmatch

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
		
		self.scalar_descriptor = """ CREATE TABLE IF NOT EXISTS {} (
						id integer PRIMARY KEY,
						core integer NOT NULL,
						product integer
					);""".format(self.name)
								

		self.insert_descriptor = """ INSERT INTO {} (core, product)
						VALUES (?,?) """.format(self.name)	
		
		self.scalar_insert_descriptor = """ INSERT INTO {} (core, product)
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


	def get_nparticle_scalars(self, all_files=None):
		if all_files is None:
			all_files = glob.glob("**", recursive=True)
		
		for file in all_files:
			match = re.compile(self.regexp).match(file)
			if match:
				Fptr = h5py.File(file, 'r')
				Core_ids = Fptr['core_ids'][()]
				N_particles = Fptr['n_particles'][()]
				other_THING = dict(zip(Core_ids, N_particles))
				keys_values = other_THING.items()
				str_THING = {str(key): str(value) for key, value in keys_values}
				other_combined = [(k,v) for k,v in str_THING.items()]
				found=match

		return other_combined
	
	def get_neighborhood_scalars(self, all_files=None):
		if all_files is None:
			all_files = glob.glob("**", recursive=True)

		for file in all_files:
			match = re.compile(self.regexp).match(file)
			if match:
				Fptr = h5py.File(file, 'r')
				Core_ids = Fptr['core_ids'][()]
				Neighborhood = Fptr['neighborhood'][()]
				other_THING = dict(zip(Core_ids, Neighborhood))
				keys_values = other_THING.items()
				str_THING = {str(key): str(value) for key, value in keys_values}

				other_combined = [(k,v) for k,v in str_THING.items()]
				found=match	
		return other_combined
		


	def get_mountaintop_scalars(self, all_files=None):
		if all_files is None:
			all_files = glob.glob("**", recursive=True)
		
		for file in all_files:
			match = re.compile(self.regexp).match(file)
			if match:
				fptr = h5py.File(file, 'r')
				THING_TO_FILL = {}
				for group in fptr:
					peak_id = fptr[group]['peak_id'][()]
					THING_TO_FILL[peak_id] = fptr[group]['peak_density'][()]
				keys_values = THING_TO_FILL.items()
				str_THING = {str(key): str(value) for key, value in keys_values}
				mt_combined = [(k,v) for k,v in str_THING.items()]
		
		return mt_combined
		

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
	conn = create_connection('simulation3.db')
	for product in list_of_product_objects:
		p = product.get_scalars(all_files=all_files)
		create_table(conn, product.scalar_descriptor)
		create_entry(conn, product.scalar_insert_descriptor, p)


