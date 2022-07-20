import glob
import os
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

def append_value(dict_obj, key, value):
	if key in dict_obj:
		if not isinstance(dict_obj[key], list):
			dict_obj[key] = [dict_obj[key]]
		dict_obj[key].append(value)
	else:
		dict_obj[key] = value


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
	def __init__(self, name, regexp, sim_name):
		self.name = name
		self.regexp = regexp
		self.sim_name = sim_name
		self.ftype_list = []
		self.file_list = []
		self.blob_list = []
		self.core_list = []

		file_type = self.regexp.split(".")[-1]
		if file_type == 'h5':
			self.run = self.get_scalars()
		else:
			self.run = self.get_files()


		self.table_descriptor = """ CREATE TABLE IF NOT EXISTS {} (
						id integer PRIMARY KEY,
						core integer NOT NULL,
						product BLOB,
						ftype text
					);""".format(self.name)
		
		self.scalar_descriptor = """ CREATE TABLE IF NOT EXISTS {} (
						id integer PRIMARY KEY,
						core integer NOT NULL,
						product integer,
						ftype text
					);""".format(self.name)
								

		self.insert_descriptor = """ INSERT INTO {} (core, product, ftype)
						VALUES (?,?,?) """.format(self.name)
		
		self.scalar_insert_descriptor = """ INSERT INTO {} (core, product, ftype)
							VALUES (?,?,?) """.format(self.name)	
		
			
	def create_connection(self):
		conn = None
		try:
			conn =  sqlite3.connect(self.sim_name)
			return conn
		except Error as e:
			print (e)
		return conn


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
			ext = os.path.splitext(file)
			self.ftype_list.append(ext[1])
		combined_data = tuple(zip(self.core_list,self.blob_list,self.ftype_list))

		return combined_data


	def get_scalars(self, all_files=None):
		if all_files is None:
			all_files = glob.glob("**", recursive=True)		
		for file in all_files:
			match = re.compile(self.regexp).match(file)
			if match:
				if 'nparticles' in file:
					ext = os.path.splitext(file)
					f_ext = ext[1]
					Fptr = h5py.File(file, 'r')
					Core_ids = Fptr['core_ids'][()]
					N_particles = Fptr['n_particles'][()]
					other_THING = dict(zip(Core_ids, N_particles))
					for key in other_THING:
						append_value(other_THING, key, f_ext)
					keys_values = other_THING.items()
					other_combined = []
					for x, (y, z) in keys_values:
						other_combined.append((str(x), str(y), str(z)))
					found=match
				if 'neighborhood' in file:
					ext = os.path.splitext(file)
					f_ext = ext[1]
					Fptr = h5py.File(file, 'r')
					Core_ids = Fptr['core_ids'][()]
					Neighborhood = Fptr['neighborhood'][()]
					other_THING = dict(zip(Core_ids, Neighborhood))
					for key in other_THING:
						append_value(other_THING, key, f_ext)
					keys_values = other_THING.items()
					other_combined = []
					for x, (y, z) in keys_values:
						other_combined.append((str(x), str(y), str(z)))
					found=match
				if 'mountain_top' in file:
					ext = os.path.splitext(file)
					f_ext = ext[1]
					fptr = h5py.File(file, 'r')
					THING_TO_FILL = {}
					for group in fptr:
						peak_id = fptr[group]['peak_id'][()]
						THING_TO_FILL[peak_id] = fptr[group]['peak_density'][()]
					for key in THING_TO_FILL:
						append_value(THING_TO_FILL, key, f_ext)
					keys_values = THING_TO_FILL.items()
					other_combined = []
					for x, (y, z) in keys_values:
						other_combined.append((str(x), str(y), str(z)))
		return other_combined
	

def readProductList(control_file):
	product_list = []
	with open(control_file) as file:
		for line in file:
			strs = [str(i) for i in line.strip().split(',') if i]
			product_list.append( Product(strs[0], strs[1], strs[2]) )
	return product_list				

			

if __name__ =='__main__':

	list_of_product_objects = readProductList("control_sim3.txt")
	all_files = glob.glob("**", recursive=True)
	for product in list_of_product_objects:
		conn = product.create_connection()
		p = product.run
		print(p)
		pdb.set_trace()
		if p[0][2] == '.h5':
			create_table(conn, product.scalar_descriptor)	
			create_entry(conn, product.scalar_insert_descriptor, p)
		else:
			create_table(conn, product.table_descriptor)
			create_entry(conn, product.insert_descriptor, p)
