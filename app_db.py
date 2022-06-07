import sqlite3
from flask import Flask, render_template,request
from sqlite3 import Error
#from flask_sqlalchemy import SQLAlchemy
import base64
from base64 import b64encode
import pdb

app = Flask(__name__, template_folder='templates')


@app.route('/')
def my_form():
	return render_template('index.html')


@app.route('/table', methods=['POST','GET'])



def makeApp():

	value = request.form.get('sim')
	if value == '1':
		conn=sqlite3.connect('simulation1.db')
	elif value == '2':
		conn=sqlite3.connect('simulation2.db')
	elif value == '3':
		conn = sqlite3.connect('simulation3.db')

	db = conn.cursor()


	
	cores_id = request.form.get('cores')
	core_list = cores_id.split(",")
	core_set = set(core_list)

	product_list = request.form.getlist('mycheckbox')



	table_list = list(db.execute('SELECT name from sqlite_master where type="table";'))
	table_list_first_ele = []
	for i in table_list:
		table_list_first_ele.append(i[0])

	y = {}
	header_list = []
	header_list.append('Core ID')
	
	for tablename in product_list:
		y[tablename] = {'core_id':[], 'products':[]}
		header_list.append(str(tablename))
		if tablename in table_list_first_ele:
			product = str(tablename)
			query = "SELECT {pro}.core,{pro}.product FROM {pro} WHERE core IN ({co}) ORDER BY core ASC".format(co=','.join(['?'] * len(core_list)), pro=product)
			db.execute(query, core_list)
			rows = db.fetchall()
			for row in rows:
				y[tablename]['products'].append(b64encode(row[1]).decode('utf-8'))
				y[tablename]['core_id'].append(str(row[0]))

	THING = {}
	for core_id in core_set:
		THING[core_id] = []
		THING[core_id].append(core_id)
		for tablename in y:
			if core_id not in y[tablename]['core_id']:
				renderText = 'X'
			else:
				index = y[tablename]['core_id'].index(core_id)
				res = y[tablename]['products'][index]
				renderText = f'<img src="data:image/png;base64, {res}" width="300" height="300"/>'
			THING[core_id].append(renderText)

	productList = []
	for core_id in THING:
		productList.append(THING[core_id])

	return render_template('table.html',core_set=core_set,productList=productList, header_list=header_list)

if __name__ == "__main__":
	app.run(debug=True)

