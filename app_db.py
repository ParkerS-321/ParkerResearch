import sqlite3
from flask import Flask, render_template,request
from sqlite3 import Error
#from flask_sqlalchemy import SQLAlchemy
import base64
from base64 import b64encode

app = Flask(__name__, template_folder='templates')




@app.route('/')
def my_form():
	return render_template('index.html')


@app.route('/table', methods=['POST','GET'])

def getCore():

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
	core_tuple = tuple(core_list)
	
	product_list = request.form.getlist('mycheckbox')
#	product_list = product_list.split(",")
	prod_tuple = tuple(product_list)


	blowhair_tuple = []
	densitytime_tuple = []

	table_list = list(db.execute('SELECT name from sqlite_master where type="table";'))
	y = {}
	
	core_query_list = []

	if value == '1':
		#query = "SELECT blowhair.sim1_img FROM blowhair WHERE blowhair.core IN ({core_list}) UNION SELECT densitytime.sim1_img FROM densitytime WHERE densitytime.core IN ({core_list})"
		query = "SELECT * FROM blowhair WHERE core IN ({co}) ORDER BY core ASC".format(co=','.join(['?'] * len(core_list)))
		db.execute(query, core_list)

	if value == '2':
		for tablename in table_list:
			y[tablename] = []
			if tablename[0] in product_list:
				product = str(tablename[0])
				query = "SELECT {pro}.core,{pro}.sim2_img FROM {pro} WHERE core IN ({co}) ORDER BY core ASC".format(co=','.join(['?'] * len(core_list)), pro=product)
				db.execute(query, core_list)
				rows = db.fetchall()
				for row in rows:
					y[tablename].append(b64encode(row[1]).decode('utf-8'))
					core_query_list.append(row[0])

	if value == '3':
		db.execute('SELECT blowhair.sim3_img, densitytime.sim3_img FROM blowhair,densitytime WHERE blowhair.core=? AND densitytime.core=?',(core_id, core_id,))


	
	
	#for value in y.values():
	#	decode_dt_list.append(b64encode(row[2]).decode('utf-8'))	
	#	user_core_list.append(row[1])	
	#blowhair_tup = tuple(zip(user_core_list,decode_img_list))
	

	list0 = list(y.values())[0]
	list1 = list(y.values())[1]
	
	return render_template('table.html',core_query_list=core_query_list, list0=list0,list1=list1)

if __name__ == "__main__":
	app.run(debug=True)

