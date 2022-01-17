import glob
import re
import os
import jinja2
import pandas as pd
from IPython.display import Image,HTML
import numpy as np
from flask import Flask,request,render_template,session,redirect,send_from_directory



list_files=glob.glob("**", recursive=True)                      # create list of all files

new_list=[]

for file in list_files:
        #head,tail = os.path.split(file)
        #new_list.append(tail)
        new_list.append(file)
#print(new_list)

#-------------------------------------------------------------- u301 table-----------------------------------------------#

regex = re.compile('(.*)/u301_density_6_c(\d{4}).png')

u301_image_list=[]
u301_core_list = []

for file in new_list:
        match = regex.match(file)
        if match:
                u301_image_list.append(file)                    #match the files with the correct regex exp
                found = match
                #print(file)

for file in u301_image_list:                                    #extract the core number 'c...' from the matched files
        match = regex.match(file)
        if match:
                core_num_u302 = match.group(2)
                u301_core_list.append(core_num_u302)
#-----------------------------------------------------------#

headings = ('Core ID','Images')
data = tuple(zip(u301_core_list,u301_image_list))

#data1= u301_core_list
#data2= u301_image_list

app = Flask(__name__, template_folder='templates')
@app.route("/")

def table():
	return render_template("table.html", headings = headings, data=data)

if __name__ == "__main__":
	app.run(debug=True)
