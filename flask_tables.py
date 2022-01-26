import glob
import re
import os
import jinja2
import pandas as pd
from IPython.display import Image,HTML
import numpy as np
from flask import Flask,request,render_template,session,redirect,send_from_directory
from itertools import cycle



list_files=glob.glob("**", recursive=True)                      # create list of all files

new_list=[]

for file in list_files:
        #head,tail = os.path.split(file)
        #new_list.append(tail)
        new_list.append(file)
#print(new_list)

#-------------------------------------------------------------- density_time tables ----------------------------------------------#
#---U301---#
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

#---U302---#

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


#---------------------------------------------------Proj_x_density tables-----------------------------#
#u301
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

#u302
regex_u302_1 = re.compile('(.*)/u302_peak_p(\d{4})_34_Projection_x_density.png')

u302_proj_x_image_list = []
u302_proj_x_peakid_list = []

for file in new_list:
        match = regex_u302_1.match(file)
        if match:
                u302_proj_x_image_list.append(file)
                found = match
for file in u302_proj_x_image_list:
        match = regex_u302_1.match(file)
        if match:
                u302_proj_x_peakid = match.group(2)
                u302_proj_x_peakid_list.append(u302_proj_x_peakid)


#---------------------------------------------------- Peak Split All Tables--------------------------------#

#----U301----
regex4 = re.compile('(.*)/u301_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex5 = re.compile('(.*)/u301_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_y_density.png')
u301_peak_split_proj_x_list = []
u301_peak_split_proj_y_list = []
excluded_core_list =['0015-0016','0017-0019','0040-0042','0042-0043','0108-0111','0166-0167','0194-0196','0197-0200','0202-0203','0261-0262','0261-0263','0262-0263']


for file in new_list:
        match=regex4.match(file)
        match1=regex5.match(file)
        if match:
                u301_peak_split_proj_x_list.append(file)
                found = match
        if match1:
                u301_peak_split_proj_y_list.append(file)
                found=match1

#----U302----
regex_u302_2 = re.compile('(.*)/u302_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex_u302_3 = re.compile('(.*)/u302_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_y_density.png')

u302_peak_split_proj_x_list = []
u302_peak_split_proj_y_list =[]
excluded_core_list1 = ['0006-0023','0011-0014','0018-0019','0018-0065','0018-0066','0018-0092','0020-0023','0020-0024','0020-0025','0021-0022','0023-0024','0023-0025','0026-0027','0026-0029','0027-0029','0029-0030','0033-0034','0033-0035','0033-0046','0034-0035','0034-0046','0035-0044','0035-0045','0035-0046','0043-0045','0043-0046','0045-0046','0046-0052','0046-0053','0046-0062','0050-0053','0050-0056',
'0052-0053','0053-0056','0053-0057','0055-0056','0055-0057','0056-0057','0072-0073','0085-0086','0087-0088','0087-0095','0091-0092','0093-0104','0110-0111','0194-0195','0194-0196',
'0200-0201','0208-0209','0212-0213','0273-0275','0273-0277','0275-0277','0285-0286','0349-0350','0362-0363','0366-0367','0366-0368','0366-0369','0366-0370','0366-0371','0366-0372','0367-0368','0367-0369','0367-0371','0367-0372','0368-0369','0368-0371','0369-0371','0369-0372','0371-0372','0379-0380']

for file in new_list:
        match = regex_u302_2.match(file)
        match1= regex_u302_3.match(file)
        if match:
                u302_peak_split_proj_x_list.append(file)
                found = match
        if match1:
                u302_peak_split_proj_y_list.append(file)
                found=match1

#------------------------------------------------- U301 Peak_split_corestack table --------------------------------#
regex6 = re.compile('(.*)/u301_peak_split_corestack_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex7 = re.compile('(.*)/u301_peak_split_corestack_c(\d{4})_c(\d{4})_Projection_x_density.png')
u301_peak_split_corestack_x_list = []
u301_peak_split_corestack_y_list = []
corestack_list = ['0015-0016','0017-0019','0040-0042','0042-0043','0108-0111','0166-0167','0194-0196','0197-0200','0202-0203','0261-0262','0261-0263','0262-0263']

for file in new_list:
        match = regex6.match(file)
        match1 = regex7.match(file)
        if match:
                u301_peak_split_corestack_x_list.append(file)
                found=match
        if match1:
                u301_peak_split_corestack_y_list.append(file)
                found=match1

#----------------------------------------- U301_peak_split_new clump table-------------------------#
regex8 = re.compile('(.*)/u301_peak_split_newclump_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex9 = re.compile('(.*)/u301_peak_split_newclump_c(\d{4})_c(\d{4})_Projection_y_density.png')

u301_peak_split_newclump_x_list = []
u301_peak_split_newclump_y_list = []
newclump_list = ['0015-0016','0017-0019','0040-0042','0042-0043','0108-0111','0166-0167','0194-0196','0197-0200','0202-0203','0261-0262','0261-0263','0262-0263']

for file in new_list:
        match = regex8.match(file)
        match1 = regex9.match(file)
        if match:
                u301_peak_split_newclump_x_list.append(file)
                found=match
        if match1:
                u301_peak_split_newclump_y_list.append(file)
                found=match1
                
#-------------------------------------------U301_peak_split_orig -------------------------------------#

regex10 = re.compile('(.*)/u301_peak_split_orig_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex11 = re.compile('(.*)/u301_peak_split_orig_c(\d{4})_c(\d{4})_Projection_y_density.png')

u301_peak_split_orig_x_list =[]
u301_peak_split_orig_y_list = []
orignum_list = ['0015-0016','0017-0019','0040-0042','0042-0043','0108-0111','0166-0167','0194-0196','0197-0200','0202-0203','0261-0262','0261-0263','0262-0263']

for file in new_list:
        match = regex10.match(file)
        match1 = regex11.match(file)
        if match:
                u301_peak_split_orig_x_list.append(file)
                found=match
        if match1:
                u301_peak_split_orig_y_list.append(file)
                found=match1

#----------------------------------------------U301 _core_zoom_annotate..._projection_x

regex12 = re.compile('(.*)/u301_core_zoom_annotate_c(\d{4})_n(\d{4})_Projection_x_density.png')
u301_core_zoom_image_list=[]
u301_core_zoom_corenum_list=[]

for file in new_list:
        match = regex12.match(file)
        if match:
                u301_core_zoom_image_list.append(file)
                found = match
for file in u301_core_zoom_image_list:
        match = regex12.match(file)
        if match:
                u301_core_zoom_num = match.group(2)
                u301_core_zoom_corenum_list.append(u301_core_zoom_num)

        
#print(u301_core_zoom_corenum_list)


#-----------------------------------------------Flask app/data-----------------------------------#
headings = ('Core ID','Density_time')
headings1 = ('Peak ID', 'Projection_x')
headings2 = ('Excluded Core Number', 'Peak_Split_All_Projection_X', 'Peak_Split_All_Projection_Y')
headings3 = ('Corestack Core Number', 'Peak_Split_Corestack_Projection_X', 'Peak_Split_Corestack_Projection_Y')
headings4 = ('NewClump Core Number', 'Peak_Split_NewClump_Projection_X','Peak_Split_NewClump_Projection_Y')
headings5 = ('Orig Core Number', 'Peak_Split_Orig_Projection_X','Peak_Split_Orig_Projection_Y')
headings6 = ('Core ID', 'Core_Zoom_Annotate_Projection_X')
#-------U301 Data ------------#
data = tuple(zip(u301_core_list,u301_image_list))    #u301 density_time

data2 = tuple(zip(u303_core_list, u303_image_list))  # u303 density_time

data3 = tuple(zip(u301_proj_x_image_list, u301__proj_x_peakid_list))  #u301 projection_x

data4= tuple(zip(u301_peak_split_proj_x_list,u301_peak_split_proj_y_list,excluded_core_list))

data5 = tuple(zip(u301_peak_split_corestack_x_list, u301_peak_split_corestack_y_list, corestack_list))

data6 =tuple(zip(u301_peak_split_newclump_x_list,u301_peak_split_newclump_y_list,newclump_list))

data7 = tuple(zip(u301_peak_split_orig_x_list,u301_peak_split_orig_y_list,orignum_list))

data8 = tuple(zip(u301_core_zoom_image_list,u301_core_zoom_corenum_list))  #u301 core_zoom_annotate list

def getKey(item):
        return item[0]
data8_sort = sorted(data8,key=getKey)
data8_every14 = data8_sort[0::14]

#------U302 Data---------------#
data1 = tuple(zip(u302_core_list, u302_image_list))  #u302 density_time

data9 = tuple(zip(u302_proj_x_peakid_list, u302_proj_x_image_list))
data9_sort = sorted(data9,key=getKey)
data9_every3 = data9_sort[0::3]

data10 = tuple(zip(u302_peak_split_proj_x_list,u302_peak_split_proj_y_list,excluded_core_list1)) #U302 Peak_split_Exclude_all







app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
	return render_template("home.html")	

@app.route('/u301')
def u301_tables():
	return render_template("table_u301.html", headings=headings, headings1=headings1, data=data, data3=data3, headings2=headings2, data4=data4, headings3=headings3, data5=data5, headings4=headings4, data6=data6, data7=data7, headings5=headings5, data8_every14=data8_every14, headings6=headings6)

@app.route('/u302')
def u302_table():
	return render_template("table_u302.html", headings=headings, headings1=headings1,headings2=headings2, data1=data1, data9_every3=data9_every3, data10=data10)

@app.route('/u303')
def u303_table():
	return render_template("table_u303.html", headings=headings, data2=data2)


if __name__ == "__main__":
	app.run(debug=True)
