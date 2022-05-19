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
	
#	products = request.form.get('products')
#	product_list = products.split(",")
#	prod_tuple = tuple(product_list)


	if value == '1':
		#query = "SELECT blowhair.sim1_img FROM blowhair WHERE blowhair.core IN ({core_list}) UNION SELECT densitytime.sim1_img FROM densitytime WHERE densitytime.core IN ({core_list})"
		query = "SELECT * FROM blowhair WHERE core IN ({co}) ORDER BY core ASC".format(co=','.join(['?'] * len(core_list)))
		db.execute(query, core_list)

	if value == '2':
		query = "SELECT * FROM blowhair WHERE core IN ({co}) ORDER BY core ASC".format(co=','.join(['?'] * len(core_list)))
		db.execute(query, core_list)
		#db.execute('SELECT blowhair.sim2_img, densitytime.sim2_img FROM blowhair,densitytime WHERE blowhair.core=? AND densitytime.core=?',(core_id, core_id,))

	if value == '3':
		db.execute('SELECT blowhair.sim3_img, densitytime.sim3_img FROM blowhair,densitytime WHERE blowhair.core=? AND densitytime.core=?',(core_id, core_id,))

	rows=db.fetchall()

	img_list = []
	decode_img_list = []
	user_core_list = []
	#n = 2
	#img_list.append([x[n] for x in rows])
	
	for row in rows:
		decode_img_list.append(b64encode(row[2]).decode('utf-8'))	
		user_core_list.append(row[1])	
	blowhair_tup = tuple(zip(user_core_list,decode_img_list))
	
	return render_template('table.html',core_list=core_list, blowhair_tup=blowhair_tup)

if __name__ == "__main__":
	app.run(debug=True)

