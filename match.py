import glob
import re
import os
import jinja2
import pandas as pd
from IPython.display import Image,HTML
import numpy as np

list_files=glob.glob("**", recursive=True) 

new_list=[]

for file in list_files:
	#head,tail = os.path.split(file)
	#new_list.append(tail)
	new_list.append(file)
#print(new_list)

regex = re.compile('(.*)/u301_density_6_c(\d{4}).png')

u301_image_list=[]
u301_core_list = []

for file in new_list:
	match = regex.match(file)
	if match:
		u301_image_list.append(file)	
		found = match
		#print(file)

for file in u301_image_list:
	match = regex.match(file)
	if match:
		core_num_u302 = match.group(2)
		u301_core_list.append(core_num_u302)		

#print(u301_core_list)


df = pd.DataFrame(list(zip(u301_core_list,u301_image_list)), columns = ['Core ID', 'Image'])

#df = pd.DataFrame(core_list,columns=['Core ID'])
#df['Image'] = image_list

def path_to_image_html(path):
	return '<a href "http://www.google.com"><img src="' + path + '" width= "120"></a>'

pd.set_option('display.max_colwidth', None)

image_cols = ['Image']

format_dict = {}
for image_col in image_cols:
	format_dict[image_col] = path_to_image_html


df.to_html('u301_table.html',escape=False, formatters=format_dict)



#------------------------------------------------------------------

#--------------------------- u302 table----------------------------#


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

#print(u302_image_list)
#print(u302_core_list)
df = pd.DataFrame(list(zip(u302_core_list,u302_image_list)), columns = ['Core ID', 'Image'])

def path_to_image_html1(path):
	return '<a href "http://www.google.com"><img src="' + path + '" width= "120"></a>'

pd.set_option('display.max_colwidth', None)

image_cols1 = ['Image']

format_dict = {}
for image_col in image_cols1:
	format_dict[image_col] = path_to_image_html1


df.to_html('u302_table.html',escape=False, formatters=format_dict)


#--------------------------------------------------------------------------u303 table--------------------------------------------------#


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

df = pd.DataFrame(list(zip(u303_core_list,u303_image_list)), columns = ['Core ID', 'Image'])

def path_to_image_html2(path):
        return '<a href "http://www.google.com"><img src="' + path + '" width= "120"></a>'

pd.set_option('display.max_colwidth', None)

image_cols2 = ['Image']

format_dict = {}
for image_col in image_cols2:
        format_dict[image_col] = path_to_image_html2


df.to_html('u303_table.html',escape=False, formatters=format_dict)
