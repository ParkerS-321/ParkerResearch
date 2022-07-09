import sqlite3
from flask import Flask, render_template,request,session
from sqlite3 import Error
import base64
from base64 import b64encode
import pdb
import itertools
import re

app = Flask(__name__, template_folder='templates')
app.secret_key ='\xd9\rx\xd2\xe8\xec\r\xcc\xac\xf2}\x8eF\x9csY'
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/sim', methods=['POST','GET'])
def sim():
	session["value"] = request.form.get('sim')
	if session["value"] == '1':
		conn = sqlite3.connect('simulation1.db')
		simText = f'Simulation 1'
	elif session["value"] == '2':
		conn = sqlite3.connect('simulation2.db')
		simText = f'Simulation 2'
	elif session["value"] == '3':
		conn = sqlite3.connect('simulation3.db')
		simText = f'Simulation 3'	
	
	db = conn.cursor()
	
	db_table_list = list(db.execute('SELECT name from sqlite_master where type="table";'))
	db_table_list_first = []
	for i in db_table_list:
		db_table_list_first.append(i[0])
	
	core_dict = {}
	for table in db_table_list_first:
		core_dict[table] = {'core_id':[]}
		name = str(table)
		query = "SELECT {name}.core FROM {name}".format(name=name)
		db.execute(query)
		rows = db.fetchall()
		for row in rows:
			core_dict[table]['core_id'].append(str(row[0]))

	list_dict = [list(d.values()) for d in core_dict.values()]
	merged1 = list(itertools.chain(*list_dict))
	merged2 = list(itertools.chain(*merged1))

	core_list=[]
	for i in merged2:
		if i not in core_list:
              		core_list.append(i)
	core_list.sort()					#THOUGHT THIS WOULD SORT Core table but jinja batch messes it up

	return render_template('sim.html',simText=simText, core_list=core_list)


@app.route('/table', methods=['POST','GET'])

def makeApp():
	
	value = session.get("value",None)
	if value == '1':
		conn=sqlite3.connect('simulation1.db')
	elif value == '2':
		conn=sqlite3.connect('simulation2.db')				#Connects to desired DB based on user input
	elif value == '3':
		conn = sqlite3.connect('simulation3.db')

	db = conn.cursor()
	
	cores_id = request.form.getlist('core_check')
#	core_list = cores_id.split(",")
	core_set = set(cores_id)

	product_list = request.form.getlist('mycheckbox')



	table_list = list(db.execute('SELECT name from sqlite_master where type="table";'))			#Grabs a tuple of tables within the desired DB of the form (table, )
	table_list_first_ele = []
	for i in table_list:
		table_list_first_ele.append(i[0])								#Just grabs the table name from the tuple

	y = {}
	header_list = []
	header_list.append('Core ID')
	
	for tablename in product_list:
		y[tablename] = {'core_id':[], 'products':[]}							#Makes dictionary for core_id and the associated products
		header_list.append(str(tablename))
		if tablename in table_list_first_ele:
			product = str(tablename)
			query = "SELECT {pro}.core,{pro}.product FROM {pro} WHERE core IN ({co}) ORDER BY core ASC".format(co=','.join(['?'] * len(cores_id)), pro=product)		
			db.execute(query, cores_id)
			rows = db.fetchall()
			product_type = list(db.execute("SELECT typeof(product) from %s LIMIT 1;"%tablename))[0][0]
			for row in rows:
				if product_type == 'blob':
					y[tablename]['products'].append(b64encode(row[1]).decode('utf-8'))
				else:
					y[tablename]['products'].append(row[1])
				y[tablename]['core_id'].append(str(row[0]))

	THING = {}
	for core_id in core_set:
		THING[core_id] = []
		THING[core_id].append(core_id)
		for tablename in y:
			if core_id not in y[tablename]['core_id']:							
				renderText = 'X'
			else:
				index = y[tablename]['core_id'].index(core_id)						#Renders either 'X' if the product does not exist for the desired core
				res = y[tablename]['products'][index]
				product_type = list(db.execute("SELECT typeof(product) from %s LIMIT 1;"%tablename))[0][0]
				if product_type == 'blob':
					renderText = f'<img src="data:image/png;base64, {res}" width="300" height="300"/>' 
				else:	
					renderText = res
		
			THING[core_id].append(renderText)

	productList = []
	for core_id in THING:
		productList.append(THING[core_id])

	return render_template('table.html',core_set=core_set,productList=productList, header_list=header_list)

if __name__ == "__main__":
	app.run(debug=True)

