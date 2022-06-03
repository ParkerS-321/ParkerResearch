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
		conn=sqlite3.connect('sim1.db')
	elif value == '2':
		conn=sqlite3.connect('sim2.db')
	elif value == '3':
		conn = sqlite3.connect('sim3.db')

	db = conn.cursor()


	
	cores_id = request.form.get('cores')
	core_list = cores_id.split(",")
	core_set = set(core_list)

	product_list = request.form.getlist('mycheckbox')



	table_list = list(db.execute('SELECT name from sqlite_master where type="table";'))

	y = {}
	header_list = []
	header_list.append('Core ID')
	
	if value == '1':
		#query = "SELECT blowhair.sim1_img FROM blowhair WHERE blowhair.core IN ({core_list}) UNION SELECT densitytime.sim1_img FROM densitytime WHERE densitytime.core IN ({core_list})"
		query = "SELECT * FROM blowhair WHERE core IN ({co}) ORDER BY core ASC".format(co=','.join(['?'] * len(core_list)))
		db.execute(query, core_list)

	if value == '2':
		
		for tablename in table_list:
			header_list.append(str(tablename[0]))
			y[tablename] = {'core_id':[], 'products':[]}
			if tablename[0] in product_list:
				product = str(tablename[0])
				query = "SELECT {pro}.core,{pro}.sim2_img FROM {pro} WHERE core IN ({co}) ORDER BY core ASC".format(co=','.join(['?'] * len(core_list)), pro=product)
				db.execute(query, core_list)
				rows = db.fetchall()
				for row in rows:
					y[tablename]['products'].append(b64encode(row[1]).decode('utf-8'))
					y[tablename]['core_id'].append(str(row[0]))
	if value == '3':
		db.execute('SELECT blowhair.sim3_img, densitytime.sim3_img FROM blowhair,densitytime WHERE blowhair.core=? AND densitytime.core=?',(core_id, core_id,))

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
				renderText = f'<img src="data:image/png;base64, {res}" width="500" height="500"/>'
			THING[core_id].append(renderText)

	productList = []
	for core_id in THING:
		productList.append(THING[core_id])

	return render_template('table.html',core_set=core_set,productList=productList, header_list=header_list)

if __name__ == "__main__":
	app.run(debug=True)

