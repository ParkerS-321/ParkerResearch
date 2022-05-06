import sqlite3
from sqlite3 import Error
import re
import glob
from collections import defaultdict

def convertToBinary(filename):
	with open(filename, 'rb') as file:
		blobData = file.read()
	return blobData


#Establish data to enter table#

total_files = glob.glob("**", recursive=True)

#BLOW HAIR DATA

hair1_regex = re.compile('(.*)/u501_blowing_hair_c(\d{4}).png')			#SIM 1
densitytime1_regex = re.compile('(.*)/u301_density_6_c(\d{4}).png')

hair1_img = []
hair1_core = []
densitytime1_img = []
densitytime1_core = []



for file in total_files:					
	match = hair1_regex.match(file)
	match1 = densitytime1_regex.match(file)
	if match:
		hair1_img.append(file)
		core=match.group(2)
		hair1_core.append(core)
		found = match
	if match1:
		densitytime1_img.append(file)
		core=match1.group(2)
		densitytime1_core.append(core)
		found=match1


hair_blob1=[]
densitytime_blob1=[]


for file in hair1_img:
	hair_blob1.append(convertToBinary(file))
for file in densitytime1_img:
	densitytime_blob1.append(convertToBinary(file))


blowhair1_final = tuple(zip(hair1_core, hair_blob1))
densitytime1_final = tuple(zip(densitytime1_core, densitytime_blob1))



def create_connection(db_astro_file):
# Create a db connection
	conn = None
	try:
		conn = sqlite3.connect(db_astro_file)
	except Error as e:
		print(e)

	return conn

def create_entry(conn, entry):
	""" Create a new entry in {} table """

	sql = ''' INSERT INTO blowhair (core, sim1_img)
		VALUES (?,?) '''
	cur = conn.cursor()
	
	cur.executemany(sql,entry)
	
	conn.commit()
	
	return cur.lastrowid


def main():
	database = "sim1.db"

	#create a database connection
	conn = create_connection(database)

	entry = blowhair1_final
	create_entry(conn,entry)


if __name__ == '__main__':
	main()

