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

#-------------------------------------------------------------- u301 density_time table-----------------------------------------------#

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
                core_num_u301 = match.group(2)
                u301_core_list.append(core_num_u301)

#-------------------------------------------------------u302 density_time table--------------#
regex1 = re.compile('(.*)/u302_density_6_c(\d{4}).png')

u302_image_list = []
u302_core_list = []

for file in new_list:
        match = regex1.match(file)
        if match:
                u302_image_list.append(file)
                found = match


for file in u302_image_list:
        match = regex1.match(file)
        if match:
                core_num_u302 = match.group(2)
                u302_core_list.append(core_num_u302)


#--------------------------------------------------------u303 density_time table----------------------------#


regex2 = re.compile('(.*)/u303_density_6_c(\d{4}).png')

u303_image_list = []
u303_core_list = []

for file in new_list:
        match = regex2.match(file)
        if match:
                u303_image_list.append(file)
                found = match

for file in u303_image_list:
        match = regex2.match(file)
        if match:
                core_num_u303 = match.group(2)
                u303_core_list.append(core_num_u303)


#---------------------------------------------------U301 Proj_x_density-----------------------------#

regex3 = re.compile('(.*)/u301_peak_p(\d{4})_34_Projection_x_density.png')

u301_proj_x_image_list = []
u301__proj_x_peakid_list = []

for file in new_list:
        match = regex3.match(file)
        if match:
                u301_proj_x_image_list.append(file)
                found = match

for file in u301_proj_x_image_list:
        match = regex3.match(file)
        if match:
                u301_peakid_num = match.group(2)
                u301__proj_x_peakid_list.append(u301_peakid_num)

print(u301__proj_x_peakid_list)

#-----------------------------------------------Flask app/data-----------------------------------#
headings = ('Core ID','Density_time')
data = tuple(zip(u301_core_list,u301_image_list))

data1 = tuple(zip(u302_core_list, u302_image_list))

data2 = tuple(zip(u303_core_list, u303_image_list))

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
	return render_template("home.html")	

@app.route('/u301')
def u301_table():
	return render_template("table_u301.html", headings = headings, data=data)

@app.route('/u302')
def u302_table():
	return render_template("table_u302.html", headings=headings, data1=data1)

@app.route('/u303')
def u303_table():
	return render_template("table_u303.html", headings=headings, data2=data2)


if __name__ == "__main__":
	app.run(debug=True)
