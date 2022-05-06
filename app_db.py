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
	core_id = request.form.get('core')
	db.execute('SELECT blowhair.sim1_img, densitytime.sim1_img FROM blowhair,densitytime WHERE blowhair.core=? AND densitytime.core=?',(core_id, core_id,))
	rows=db.fetchall()
	
	blob_blowhair_img=[]	
	blob_densitytime_img=[]
	for row in rows:
		blob_blowhair_img = b64encode(row[0]).decode('utf-8')
		blob_densitytime_img = b64encode(row[1]).decode('utf-8')
	
	return render_template('table.html',core_id=core_id, rows=rows, blob_blowhair_img=blob_blowhair_img, blob_densitytime_img=blob_densitytime_img)

if __name__ == "__main__":
	app.run(debug=True)
